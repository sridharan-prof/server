from odoo import fields, models, api

class Products(models.Model):
    _name = "supermarket.product"
    _description = "Product Master"

    name = fields.Char(string="Product Name", required=True)
    price = fields.Float(string="Unit Price", required=True)
    inventory_id = fields.Many2one('supermarket.inventory', string="Inventory")
    stock_qty = fields.Integer(string="Stock Quantity", required=True)
    available = fields.Boolean(string="Available", compute="_compute_available", store=True)

    @api.depends('inventory_id')
    def _compute_available(self):
        for rec in self:
            rec.available = rec.inventory_id and rec.inventory_id.max_stock > 0
