from odoo import models, fields, api, _




class SaleOrder(models.Model):
    _inherit = 'sale.order'



    family_pricing_disabled = fields.Boolean(compute='_compute_family_pricing_disabled')

    def _compute_family_pricing_disabled(self):
        # Get the parameter value (returns 'True' or 'False' as string)
        promo_active = self.env['ir.config_parameter'].get_param('dynamic_family_pricing.enable_family_pricing', 'False')
        
        # Convert to boolean (True if promo_active == 'True')
        is_active = promo_active == 'True'
        
        # Set promotion_disabled to opposite of is_active
        for order in self:
            order.family_pricing_disabled = not is_active


    
    def apply_family_pricing(self):
        if self.family_pricing_disabled == False:
            for order in self:
                print("//////////// INSIDE apply_family_pricing ////////////////////")
                
                # step 1: group lines bu family
                lines_by_family = {}
                for line in order.order_line:
                    family = line.product_template_id.categ_id
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
                    #for line in lines:
                    #    line.price_unit = line.product_template_id.price_colis
                        
                    for line in lines:

                        selected_qty = line.product_uom_qty

                        total_qty += selected_qty

                        #INITIALIWE PRICE
                        line.price_unit = line.product_template_id.list_price

                        if line.product_packaging_id.name == 'Palette':

                            if line.product_packaging_qty >= 10:
                                for l in lines:
                                    new_price_unit = l.product_template_id.price_palette_10
                                    l.price_unit = new_price_unit
                                promotion_found = True
                                break

                            elif line.product_packaging_qty >= 5:
                                for l in lines:
                                    new_price_unit = l.product_template_id.price_palette_5
                                    l.price_unit = new_price_unit
                                promotion_found = True
                                break

                            elif line.product_packaging_qty >= 1:
                                for l in lines:
                                    new_price_unit = l.product_template_id.price_palette
                                    l.price_unit = new_price_unit
                                promotion_found = True
                                break
                            
                    if promotion_found == False:
                        if total_qty >= family.seuil:
                            for l in lines:
                                new_price_unit = l.product_template_id.price_palette_mix
                                l.price_unit = new_price_unit
                            
                    #if promotion_found == False and total_qty >= 60:
                    #    for l in lines:
                    #        new_price_unit = l.product_template_id.units_per_colis * l.product_template_id.price_palette_mix
                    #        l.price_unit = new_price_unit
                        

                    
                
                


                    



    

    @api.onchange('order_line')
    def apply_family_pricing_onchange(self):
        self.apply_family_pricing()
    
    
    family_pricing_applied = fields.Boolean(
        compute="_compute_family_pricing_flag",
        store=True
    )
    @api.depends('order_line.product_template_id', 'order_line.product_uom_qty')
    def _compute_family_pricing_flag(self):
        for order in self:
            order.family_pricing_applied = True
        self.apply_family_pricing()

















class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'




    