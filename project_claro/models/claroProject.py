#-*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models

class Project(models.Model):
    _inherit = ['project.project']
    
    IsAClaroProject = fields.Boolean(
        string='Es el proyecto de Claro?',
    )
    

     

class ProjectTaskType(models.Model):
    _inherit = ['project.task.type']


class Task(models.Model):
    _inherit = ['project.task]
    
    gerencia_claro = fields.Char(
        string='Gerencia Claro',
        help='Gerencia a la cual se certificará la tarea'        
    )
    
    supervisor_ids = fields.Many2many(
        string='Supervisor Claro',
        comodel_name='res.partner',
        relation='model.name_this_model_rel',
        column1='model.name_id',
        column2='this_model_id',
    )
    
    
    ticket = fields.Char(
        string='Ticket',
    )
    
    
    UT =
    help='Ubicación técnica' fields.Char(
        string='UT',
        help='Ubicación técnica'
    )

    
    sytex = fields.Char(
        string='Sytex',
        help='link a formulario Sytex'
    )

    
    ejecutor_id_ids = fields.Many2many(
        string='Ejecutores',
        comodel_name='res.partner',
        relation='model.name_this_model_rel',
        column1='model.name_id',
        column2='this_model_id',
    )
    
    
    """Material_ids = fields.Many2many(
        string='Material',
        comodel_name='product.product',
        relation='model.name_this_model_rel',
        column1='model.name_id',
        column2='this_model_id',
    )
    """
    
    
    
