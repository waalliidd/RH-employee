# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rh_employee(models.Model):
    _inherit = 'RH-employee'
    mode_de_travaill = fields.Selection(string='mode de travaill',)
    années_dexpérience = fields.Iteger()