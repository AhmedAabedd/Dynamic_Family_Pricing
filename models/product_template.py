from odoo import models, fields, api, _




class ProductTemplate(models.Model):
    _inherit = 'product.template'




    family_id = fields.Many2one('product.family', string="Product Family")
    units_per_colis = fields.Float(string="Units Per Colis")
    colis_per_palette = fields.Float(string="Colis per Palette")

    ################### TARIFS ##############################

    price_colis = fields.Float(string="")
    price_palette = fields.Float(string="")
    price_palette_5 = fields.Float(string="")
    price_palette_10 = fields.Float(string="")
    price_palette_mix = fields.Float(string="")