from odoo import fields, models

class saleOrdertimsa(models.Model):

    _inherit = "sale.order"
    certificate_name = fields.Char(string='Nombre', required=True)
    oc_code = fields.Char(string='OC')
    code = fields.Char(string='Código', required=False)
    ruta = fields.Text(string='Ruta a certificado')
    

    
    # field_name_ids = fields.Many2many(
    #     string='Subcontratistas',
    #     comodel_name='', buscar el nombre exacto purchase
    # )
    

    #Pendientes:
    #task_id: tareas que se certifican
    #partner_id : subcontratista.
    #purchase_id: Tareas a certificar a subcontratista
    #etiquetas analíticas
    #materiles
    #Checklist
    #