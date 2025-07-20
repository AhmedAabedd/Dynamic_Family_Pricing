from odoo import models, fields, api, _




class SaleOrder(models.Model):
    _inherit = 'sale.order'




    
    def apply_family_pricing(self):
        for order in self:
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            # step 1: group lines bu family
            lines_by_family = {}
            for line in order.order_line:
                family = line.product_template_id.family_id
                if not family:
                    continue
                if family not in lines_by_family:
                    lines_by_family[family] = self.env['sale.order.line']
                lines_by_family[family] += line
            
            # step 2: Loop through grouped lines and change item price dependying on seleted quantity
            for family, lines in lines_by_family.items():
                total_qty = 0
                promotion_found = False

                #Initialize unit price to all lines
                for line in lines:
                    line.price_unit = line.product_template_id.price_colis
                
                for line in lines:

                    selected_qty = line.product_uom_qty
                    colis_per_palette = line.product_template_id.colis_per_palette or 1

                    total_qty += selected_qty

                    if selected_qty >= colis_per_palette * 10:
                        for l in lines:
                            new_price_unit = l.product_template_id.units_per_colis * l.product_template_id.price_palette_10
                            l.price_unit = new_price_unit
                        promotion_found = True
                        break
                    elif selected_qty >= colis_per_palette * 5:
                        for l in lines:
                            new_price_unit = l.product_template_id.units_per_colis * l.product_template_id.price_palette_5
                            l.price_unit = new_price_unit
                        promotion_found = True
                        break
                    elif selected_qty >= colis_per_palette:
                        for l in lines:
                            new_price_unit = l.product_template_id.units_per_colis * l.product_template_id.price_palette
                            l.price_unit = new_price_unit
                        promotion_found = True
                        break
                    
                if promotion_found == False and total_qty >= 60:
                    for l in lines:
                        new_price_unit = l.product_template_id.units_per_colis * l.product_template_id.price_palette_mix
                        l.price_unit = new_price_unit
                    

                    
                
                


                    



    

    @api.onchange('order_line')
    def apply_family_pricing_onchange(self):
        self.apply_family_pricing()
    
    
    family_pricing_applied = fields.Boolean(
        compute="_compute_family_pricing_flag",
        store=True
    )
    @api.depends('order_line.product_template_id', 'order_line.product_uom_qty')
    def _compute_family_pricing_flag(self):
        self.apply_family_pricing()
        for order in self:
            order.family_pricing_applied = True

















class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'



    family_id = fields.Many2one('product.family', related="product_template_id.family_id")
    line_unit = fields.Char(string="Unit", default="Coli")
    