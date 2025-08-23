from odoo import models, fields, api, _

class SalesOrder(models.Model):
    _name = "sales.order"
    _description = "Sales Order"

    name = fields.Char(string="Order Reference", required=True, copy=False, readonly=True, default="New")
    customer_name = fields.Char(string="Customer Name", required=True)
    order_date = fields.Datetime(string="Order Date", default=fields.Datetime.now)
    order_line_ids = fields.One2many("sales.order.line", "order_id", string="Order Lines")
    amount_total = fields.Float(string="Total Amount", compute="_compute_amount_total", store=True)

    @api.depends("order_line_ids.subtotal")
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(order.order_line_ids.mapped("subtotal"))

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("sales.order") or ""
        return super().create(vals)


class SalesOrderLine(models.Model):
    _name = "sales.order.line"
    _description = "Sales Order Line"

    order_id = fields.Many2one("sales.order", string="Order", ondelete="cascade")
    inventory_id = fields.Many2one('sales.inventory', string="Product", required=True)
    quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Unit Price", related="inventory_id.cost_price", store=True, readonly=False)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends("quantity", "price_unit")
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
