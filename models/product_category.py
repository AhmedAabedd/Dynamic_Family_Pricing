from odoo import models, fields, api, _




class ProductCategory(models.Model):
    _inherit = 'product.category'




    seuil = fields.Float(string="seuil", required=True)