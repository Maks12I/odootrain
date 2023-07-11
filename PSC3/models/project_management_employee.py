# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementEmployee(models.Model):
    _name = 'project.management.employee'
    _description = 'Project Management Employee'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    department_id = fields.Many2one('project.management.department', string='Department', required=True)
    position = fields.Char(string='Position', required=True)
    competency_ids = fields.Many2many('project.management.competency', string='Competencies')
    availability_calendar_id = fields.Many2one('project.management.calendar', string='Availability Calendar')
    hour_rate = fields.Float(string='Hour Rate', required=True)
    user_id = fields.Many2one('res.users', string='User')
    task_ids = fields.One2many('project.management.task', 'employee_id', string='Tasks')
    product_ids = fields.Many2many('project.management.product', 'project_management_product_author_rel', 'employee_id', 'product_id', string='Products')