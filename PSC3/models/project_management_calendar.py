# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementCalendar(models.Model):
    _name = 'project.management.calendar'
    _description = 'Project Management Calendar'

    name = fields.Char(string='Name', required=True)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('project.management.employee', string='Employee')
