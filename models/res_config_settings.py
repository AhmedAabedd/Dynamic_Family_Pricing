from odoo import models, fields, api, _




class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'





    family_pricing_active = fields.Boolean(
        string="Family Pricing",
        help="Activate or deactivate the family pricing system",
        config_parameter='dynamic_family_pricing.enable_family_pricing'
    )

    apply_when = fields.Selection([
        ('auto', 'Modifying Content'),
        ('button', 'Clicking Button'),
        ('both', 'Both'),
    ],default="auto", string="Apply Pricing When", required=True, config_parameter='family_pricing.apply_when')  # This saves to ir.config_parameter