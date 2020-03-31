# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

class Clientes(models.Model):
    _name = 'clientes'
    _description = 'Clientes'

    casas = fields.Many2many('casas', string='Casas en posesión')
    dni = fields.Char('Dni', required=True)
    name = fields.Char('Nombre', required=True)
    address = fields.Char('Direccion')
    tlf = fields.Char('Telefono')
    pisos = fields.Many2many('pisos', string='Pisos en posesión')


    @api.model
    def get_casas(self, casas):
        return casas.mapped('casas.cod')

    sql_constraints = [('cliente_uniq', 'UNIQUE (dni)', 'Ya hay un cliente con ese dni')]

