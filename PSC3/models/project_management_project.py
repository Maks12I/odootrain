# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementProject(models.Model):
    _name = 'project.management.project'
    _description = 'Project Management Project'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    task_ids = fields.One2many('project.management.task', 'project_id', string='Tasks')
    employee_ids = fields.Many2many('project.management.employee', 'project_management_project_employee_rel', 'project_id', 'employee_id', string='Employees')
    max_budget = fields.Float(string='Max Budget', required=True)
    status = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('done', 'Done'), ('cancel', 'Cancel')], string='Status', default='draft')
    planned_cost = fields.Float(string='Planned Cost', compute='_compute_planned_cost')
    actual_cost = fields.Float(string='Actual Cost', compute='_compute_actual_cost')
    department_id = fields.Many2one('project.management.department', string='Department', required=True)

    @api.depends('task_ids.planned_hours', 'task_ids.employee_id.hour_rate')
    def _compute_planned_cost(self):
        for project in self:
            project.planned_cost = sum(task.planned_hours * task.employee_id.hour_rate for task in project.task_ids)

    @api.depends('task_ids.actual_hours', 'task_ids.employee_id.hour_rate')
    def _compute_actual_cost(self):
        for project in self:
            project.actual_cost = sum(task.actual_hours * task.employee_id.hour_rate for task in project.task_ids)