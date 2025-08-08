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




    @api.model
    def set_values(self):
        super().set_values()

        menu_main = self.env.ref('dynamic_family_pricing.menu_product_familys', raise_if_not_found=False)

        is_active = self.family_pricing_active

        if menu_main:
            menu_main.active = is_active