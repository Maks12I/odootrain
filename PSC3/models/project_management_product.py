# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectManagementProduct(models.Model):
    _name = 'project.management.product'
    _description = 'Project Management Product'

    name = fields.Char(string='Name', required=True)
    author_ids = fields.Many2many('project.management.employee', 'project_management_product_author_rel', 'product_id', 'employee_id', string='Authors')
    task_ids = fields.Many2many('project.management.task', 'project_management_product_task_rel', 'product_id', 'task_id', string='Tasks')
    parent_id = fields.Many2one('project.management.product', string='Parent Product')
    child_ids = fields.One2many('project.management.product', 'parent_id', string='Child Products')