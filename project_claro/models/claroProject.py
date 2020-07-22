#-*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models

class Project(models.Model):
    _inherit = ['project.project']
    

     

class ProjectTaskType(models.Model):
    _inherit = ['project.task.type']


class Task(models.Model):
    _inherit = ['project.task]

