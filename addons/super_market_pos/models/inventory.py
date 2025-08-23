from odoo import fields, models

class Inventory(models.Model):
    _name = "supermarket.inventory"
    _description = "Supermarket Inventory"

    name = fields.Char(string = "product name", required = True)
    cost_price = fields.Float(string = "Cost price")
    max_stock = fields.Integer(string = "Maximum Stock")
    reorder_level = fields.Integer(string = "Reoder level")
    expiry_date = fields.Date(string = "Expiry Date")


