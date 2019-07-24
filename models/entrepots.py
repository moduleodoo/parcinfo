# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Entrepot(models.Model):
    _name = 'parcinfo.entrepot'
    _description = 'entrepot de stockage du matériels informatique'

    name = fields.Char(string="Name", reqiured=True)
    code = fields.Char(string="Code", required=True)
    adresse = fields.Char(string="Adresse", required=False, )
    description = fields.Text(string="Description", )
    articles_ids = fields.One2many(comodel_name="product.template", inverse_name="entrepot_id",
                                   string="produits", required=False, )
    allee_ids = fields.One2many(comodel_name="parcinfo.allee.entrepot", inverse_name="entrepot_id",
                                string="Allées", required=False, )
    rangée_ids = fields.One2many(related="allee_ids.rangee_ids")


class Etage(models.Model):
    _name = 'parcinfo.etage.entrepot'
    _rec_name = 'num'
    _description = 'diférents niveaux de stockages dans un entrepot'

    num = fields.Integer(string="Numéro d'étage", required=True, )
    description = fields.Text(string="Description", )
    rangee_id = fields.Many2one(comodel_name="parcinfo.rangee.entrepot", string="Rangée", required=False, )



class Allee(models.Model):
    _name = 'parcinfo.allee.entrepot'
    _rec_name = 'num'
    _description = 'différents couloir dans un entrepot'

    num = fields.Integer(string="Numéro de Couloir", required=True, )
    description = fields.Text(string="Description", )
    rangee_ids = fields.One2many(comodel_name="parcinfo.rangee.entrepot", inverse_name="allee_id",
                                 string="Rangées", required=False, )
    entrepot_id = fields.Many2one(comodel_name="parcinfo.entrepot", string="Entrepot", required=False, )


class Rangees(models.Model):
    _name = 'parcinfo.rangee.entrepot'
    _description = 'New Description'

    name = fields.Char(string="Nom de la ranée", required=True, )
    num = fields.Char(string="Numéro de Rangée")
    description = fields.Text(string="Description", )
    allee_id = fields.Many2one(comodel_name="parcinfo.allee.entrepot", string="Couloir", required=False, )
    etage_ids = fields.One2many(comodel_name="parcinfo.etage.entrepot", inverse_name="rangee_id",
                                string="Etages", required=False, )



