from odoo import models, fields, api

class SalesInventory(models.Model):
    _name = 'sales.inventory'
    _description = 'Sales Inventory'

    product_id = fields.Many2one('product.product', string="Product", required=True)
    cost_price = fields.Float(string="Cost Price")
    maximum_stock = fields.Integer(string="Maximum Stock")
    reorder_level = fields.Integer(string="Reorder Level")
    expiry_date = fields.Date(string="Expiry Date")
    name = fields.Char(string="Name", compute="_compute_name", store=True)

    @api.depends('product_id')
    def _compute_name(self):
        for record in self:
            record.name = record.product_id.name or "Unknown"