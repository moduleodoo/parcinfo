# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Articles(models.Model):
    _inherit = 'product.template'

    n_serie = fields.Char(string="Num Série",)
    n_parc = fields.Char(string="Num Parc", )
    entrepot_id = fields.Many2one(comodel_name="parcinfo.entrepot'", string="Entrepot", required=False, )
