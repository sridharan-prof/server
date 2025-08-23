/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class SalesDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            orders: [],
            filteredOrders: [],
            totalRevenue: 0,
            totalOrders: 0,
            currentPage: 1,
            pageSize: 5,
        });

        onWillStart(async () => {
            let orders = await this.orm.searchRead(
                "sales.order",
                [],
                ["id", "name", "customer_name", "order_date", "amount_total"]
            );
            this.state.orders = orders;
            this.state.filteredOrders = orders;
            this.state.totalOrders = orders.length;
            this.state.totalRevenue = orders.reduce((sum, o) => sum + (o.amount_total || 0), 0);
        });
    }

    get paginatedOrders() {
        let start = (this.state.currentPage - 1) * this.state.pageSize;
        let end = start + this.state.pageSize;
        return this.state.filteredOrders.slice(start, end);
    }

    get pageCount() {
        return Math.ceil(this.state.filteredOrders.length / this.state.pageSize);
    }

    onSearch(ev) {
        let query = ev.target.value.toLowerCase();
        this.state.filteredOrders = this.state.orders.filter(
            o =>
                (o.name && o.name.toLowerCase().includes(query)) ||
                (o.customer_name && o.customer_name.toLowerCase().includes(query)) ||
                (o.order_date && o.order_date.toLowerCase().includes(query)) ||
                (o.amount_total && o.amount_total.toString().includes(query))
        );
        this.state.currentPage = 1;
    }

    goToPreviousPage() {
        if (this.state.currentPage > 1) {
            this.state.currentPage -= 1;
        }
    }

    goToNextPage() {
        if (this.state.currentPage < this.pageCount) {
            this.state.currentPage += 1;
        }
    }
}

SalesDashboard.template = "sales_management.SalesDashboard";
registry.category("actions").add("sales_dashboard_action", SalesDashboard);
