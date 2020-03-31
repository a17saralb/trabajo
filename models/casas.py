# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class Casas(models.Model):
    _name = 'casas'
    _description = 'Casas'

    cod = fields.Char('Codigo', required=True)
    name = fields.Char('Direccion', required=True)
    date_rent = fields.Date('Fecha de alquiler', default=lambda*a:datetime.now().strftime('%Y-%m-%d'))
    numMeses = fields.Integer('Periodo de tiempo')
    category_id = fields.Many2one('categorias', string='Categoria')


    pricePmonth = fields.Float('Precio por mes')
    totalPrice = fields.Float('Precio total', compute='_total')
    state = fields.Selection([
        ('alquilada', 'Alquilada'),
        ('disponible', 'Disponible'),
        ('vendida', 'Vendida')],
        'State', default="disponible")

    @api.one
    @api.depends('numMeses', 'pricePmonth')
    def _total(self):
        self.totalPrice = self.numMeses * self.pricePmonth

    #validacion estado
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('disponible', 'vendida'),
                   ('disponible', 'alquilada'),
                   ('alquilada', 'disponible'),
                   ('alquilada', 'vendida')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for casa in self:
            if casa.is_allowed_transition(casa.state, new_state):
                casa.state = new_state
            else:
                message = _('Cambiar de %s a %s no está permitido') % (casa.state, new_state)
                raise UserError(message)

    #cambio estado
    def disponible(self):
        self.change_state('disponible')

    def alquilada(self):
        self.change_state('alquilada')

    def vendida(self):
        self.change_state('vendida')

    sql_constraints = [('casa_uniq', 'UNIQUE (cod)', 'Ya hay una casa con ese código')]

    @api.constrains('date_rent')
    def _check_release_date(self):
        for record in self:
            if record.date_rent < fields.Date.today():
                raise models.ValidationError('La fecha de alquiler o venta no puede ser en el pasado')
