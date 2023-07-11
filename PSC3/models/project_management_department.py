# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementDepartment(models.Model):
    _name = 'project.management.department'
    _description = 'Project Management Department'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    manager_id = fields.Many2one('project.management.employee', string='Manager', required=True)
    employee_ids = fields.One2many('project.management.employee', 'department_id', string='Employees')
    project_ids = fields.One2many('project.management.project', 'department_id', string='Projects')