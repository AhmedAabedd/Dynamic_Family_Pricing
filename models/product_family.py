from odoo import models, fields, api, _




class ProductFamily(models.Model):
    _name = 'product.family'




    name = fields.Char(string="Name")
    seuil = fields.Float(string="Seuil")

    product_count = fields.Integer(compute="_compute_product_count")


    def _compute_product_count(self):
        for rec in self:
            rec.product_count = self.env['product.template'].search_count([('family_id', '=', rec.id)])
    
    def action_view_product(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'View Product',
            'res_model': 'product.template',
            'view_mode': 'list,form',
            'target': 'current', #to open in new view
            'domain': [('family_id', '=', self.id)],
            'context': {
                'default_family_id': self.id,
            }
        }

    