# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


class Clientes(models.Model):
    _name = 'clientes'
    _description = 'Clientes'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade', string='Cliente')
    casas = fields.Many2many('casas', string='Casas en posesión')
    dni = fields.Char('Dni',related='partner_id.vat')
    street = fields.Char('Calle',related='partner_id.street')
    city = fields.Char('Ciudad',related='partner_id.city')
    state_id = fields.Many2one(string='Estado-Provincia',related='partner_id.state_id')
    zip = fields.Char('C. Postal',related='partner_id.zip')
    country_id = fields.Many2one(string='País',related='partner_id.country_id')
    tlf = fields.Char('Telefono',related='partner_id.phone')
    image = fields.Binary('Imagen',related='partner_id.image')
    pisos = fields.Many2many('pisos', string='Pisos en posesión')

    @api.model
    def get_casas(self, casas):
        return casas.mapped('casas.cod')

