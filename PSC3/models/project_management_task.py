# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class ProjectManagementTask(models.Model):
    _name = 'project.management.task'
    _description = 'Project Management Task'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    planned_hours = fields.Float(string='Planned Hours', required=True)
    actual_hours = fields.Float(string='Actual Hours', compute='_compute_actual_hours') # changed this field to computed    
    competency_ids = fields.Many2many('project.management.competency', string='Required Competencies')
    min_start_date = fields.Date(string='Min Start Date')
    max_start_date = fields.Date(string='Max Start Date')
    min_end_date = fields.Date(string='Min End Date')
    max_end_date = fields.Date(string='Max End Date')
    actual_start_date = fields.Date(string='Actual Start Date')
    actual_end_date = fields.Date(string='Actual End Date')
    predecessor_ids = fields.Many2many('project.management.task', 'project_management_task_predecessor_rel', 'task_id', 'predecessor_id', string='Predecessors')
    product_ids = fields.Many2many('project.management.product', 'project_management_product_task_rel', 'task_id', 'product_id', string='Products')
    project_id = fields.Many2one('project.management.project', string='Project', required=True)
    employee_id = fields.Many2one('project.management.employee', string='Employee')

    @api.depends('actual_start_date')
    def _compute_actual_hours(self):
        for task in self:
            if task.actual_end_date:
                delta = task.actual_end_date - task.actual_start_date
                task.actual_hours = delta.days * 24  # assuming 24 hours per day
            else:
                today = datetime.today().date()
                delta = today - task.actual_start_date
                task.actual_hours = delta.days * 24  # assuming 24 hours per day
            
