from odoo import models, fields, api, _




class ProductTemplate(models.Model):
    _inherit = 'product.template'





    ################### TARIFS ##############################

    price_palette = fields.Float(string="Price Palette")
    price_palette_5 = fields.Float(string="Price Palette 5")
    price_palette_10 = fields.Float(string="Price Palette 10")
    price_palette_mix = fields.Float(string="Price Palette Mixte")

    #########################################################



    family_pricing_disabled = fields.Boolean(compute='_compute_family_pricing_disabled')

    def _compute_family_pricing_disabled(self):
        # Get the parameter value (returns 'True' or 'False' as string)
        promo_active = self.env['ir.config_parameter'].get_param('dynamic_family_pricing.enable_family_pricing', 'False')
            
        # Convert to boolean (True if promo_active == 'True')
        is_active = promo_active == 'True'
            
        # Set promotion_disabled to opposite of is_active
        for rec in self:
                rec.family_pricing_disabled = not is_active