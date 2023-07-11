# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Management',
    'version': '3.0',
    'category': 'Project',
    'summary': 'Manage projects, tasks and products',
    'description': """
This module allows you to create and manage projects, tasks and products in your organization.
You can assign tasks to employees, set deadlines and budgets, track progress and costs, and generate reports.
""",
    'depends': ['base'],
    'data': [
        #'security/project_management_security.xml',
        'security/ir.model.access.csv',
        'views/project_management_menus.xml',
        'views/project_management_views.xml',

        # 'report/project_management_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
