# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementCompetency(models.Model):
    _name = 'project.management.competency'
    _description = 'Project Management Competency'

    name = fields.Char(string='Name', required=True)