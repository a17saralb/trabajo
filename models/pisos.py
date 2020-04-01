# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta, date

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _



class Pisos(models.Model):
    _name = 'pisos'
    _description = 'pisos'
    #_inherits = {'res.partner': 'partner_id'}

    #partner_id = fields.Many2one('res.partner', ondelete='cascade')

    cod = fields.Char('Codigo', required=True)
    address = fields.Char('Direccion', required=True)
    date_rent = fields.Date('Fecha de alquiler', default=lambda*a:datetime.now().strftime('%Y-%m-%d'))
    numMeses = fields.Integer('Periodo de tiempo')
    category_id = fields.Many2one('categorias', string='Categoria')
    parking = fields.Boolean("Garaje")
    lift = fields.Boolean("Ascensor")


    #pone res.users
    pricePmonth = fields.Float('Precio por mes')
    totalPrice = fields.Float('Precio total', compute='_total')

    state = fields.Selection([
        ('alquilado', 'Alquilado'),
        ('disponible', 'Disponible'),
        ('vendido', 'Vendido')],
        'State', default="disponible")

    @api.one
    @api.depends('numMeses', 'pricePmonth')
    def _total(self):
        self.totalPrice = self.numMeses * self.pricePmonth


    #validacion estado
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('disponible', 'vendido'),
                   ('disponible', 'alquilado'),
                   ('alquilado', 'disponible'),
                   ('alquilado', 'vendido')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for piso in self:
            if piso.is_allowed_transition(piso.state, new_state):
                piso.state = new_state
            else:
                message = _('Cambiar de %s a %s no está permitido') % (piso.state, new_state)
                raise UserError(message)

    #cambio estado
    def disponible(self):
        self.change_state('disponible')

    def alquilado(self):
        self.change_state('alquilado')

    def vendido(self):
        self.change_state('vendido')

    _sql_constraints = [('piso_uniq', 'UNIQUE (cod)', 'Ya hay un piso con ese codigo')]

    @api.constrains('date_rent')
    def _check_release_date(self):
        for record in self:
            if  record.date_rent < fields.Date.today():
                raise models.ValidationError('La fecha de alquiler o venta no puede ser en el pasado')


class pisosMember(models.Model):
    _name = 'pisos.member'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')