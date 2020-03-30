# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Categorias(models.Model):
    _name = 'categorias'

    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Categoria')
    description = fields.Text('Description')
    parent_id = fields.Many2one(
        'categorias',
        string='Categoria padre',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'categorias', 'parent_id',
        string='Subcategorias')
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('No puedes crear categorias recursivas')