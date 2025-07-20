from odoo import models, fields, api, _





class ProductFamily(models.Model):
    _name = 'product.family'



    name = fields.Char(string="Family Name")
    description = fields.Text(string="Description")