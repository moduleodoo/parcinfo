# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Request(models.Model):
    _name = 'parcinfo.request'
    _description = 'requête parc informatique'
    _inherit = 'mail.thread'

    name = fields.Char(string="Intitulé", )
    description = fields.Text(string="Description du besoin",)
    articles = fields.Char(string="Article",)
    date_request = fields.Date(string="Date de la requete", default=fields.date.today())
    artilces = fields.Char(string="Article à retourner",)
    description_return = fields.Text(string="description du comportement",)
    state = fields.Selection(string="", selection=[('initialisation', 'initialisation'), ('valider', 'valider'),
                                                   ('process', 'process'),('recus', 'recus'),
                                                   ('confirmer', 'confirmer'), ], default='initialisation',
                             track_visibility="onchange")


