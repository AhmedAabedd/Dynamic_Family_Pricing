from odoo import models, fields, api, _




class ProductTemplate(models.Model):
    _inherit = 'product.template'





    ################### TARIFS ##############################

    price_palette = fields.Float(string="")
    price_palette_5 = fields.Float(string="")
    price_palette_10 = fields.Float(string="")
    price_palette_mix = fields.Float(string="")