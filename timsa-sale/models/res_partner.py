from odoo import fields, models

class partnerSubcontratista(models.Model):

    
    subcontractor = fields.Boolean(
        string='Es subcontratista',
    )

    
    
    
    #Aqui debo sumar un campo bool que indique que si es o no subcontratista
    #En base a ese campo puedo generar en la vista como tag
    #Tengo que pensarlo mejor ya que no creo que lo haga de esta manera, aunque el 
    #campo booleano lo voy a necesitar de todos modos