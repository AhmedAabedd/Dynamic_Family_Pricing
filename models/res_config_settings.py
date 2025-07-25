from odoo import models, fields, api, _




class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'





    family_pricing_active = fields.Boolean(
        string="Family Pricing",
        help="Activate or deactivate the family pricing system",
        config_parameter='dynamic_family_pricing.enable_family_pricing'
    )