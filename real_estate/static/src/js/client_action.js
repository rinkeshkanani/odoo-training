/** @odoo-module */
import { registry } from '@web/core/registry';
import { Component, onWillStart, useState, onMounted, useEffect } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";
export class Realestate extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            records: [],
            selectedRecord: null,
            date: false,
            chartType: null,
            viewType: null,
        });
        onWillStart(this.onWillStart);
        onMounted(this._renderGraph);
        useEffect(() => {
            this._renderGraph()
        }, () => [this.state.date, this.state.chartType])
    }
    async onWillStart() {
        this.state.records = await this.orm.searchRead(
            "real.estate",
            ['|', ['active', '=', true], ['active', '=', false]],
            ['name', 'state', 'description', 'active', 'date', 'amount', 'company_id', 'user_id']
        );
        const savedRecordId = localStorage.getItem("real_estate_selected_record");
        if (savedRecordId) {
            const savedId = parseInt(savedRecordId, 10);
            this.state.selectedRecord = this.state.records.find(record => record.id === savedId) || null;
        }
    }
    async _renderGraph() {
            var response = await rpc('/apply/filter',  {
            'date': this.state.date,
        })
        if (this.state.chartType == 'pie_chart') {
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
                var chartData = [['Partner', 'Name']];
                response.forEach(function(item) {
                    chartData.push([item.partner, item.total_records]);
                });
                var data = google.visualization.arrayToDataTable(chartData);
                var options = {
                title: 'Pie Chart',
                sliceVisibilityThreshold: 0,
                pieSliceText: 'value',
                pieSliceTextStyle: {
                    color: 'black',
                },
                };
                var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }
        } else if (this.state.chartType == 'donut_chart') {
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
                var chartData = [['Partner', 'Name']];
                response.forEach(function(item) {
                    chartData.push([item.partner, item.total_records]);
                });
                var data = google.visualization.arrayToDataTable(chartData);
                var options = {
                title: 'Donut Chart',
                sliceVisibilityThreshold: 0,
                pieHole: 0.4,
                pieSliceText: 'value',
                pieSliceTextStyle: {
                    color: 'black',
                },
                };
                var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }
        } else if (this.state.chartType == 'curved_chart') {
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
                var chartData = [['Partner', 'Total Amount', 'Total Count']];
                response.forEach(function(item) {
                    chartData.push([item.partner, item.total_amount, item.total_records]);
                });
                var data = google.visualization.arrayToDataTable(chartData);
                var options = {
                    title: 'Line Chart',
                    curveType: 'function',
                    legend: { position: 'bottom' }
                };
                var chart = new google.visualization.LineChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }
        } else if (this.state.chartType == 'line_chart') {
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {
                var chartData = [['Partner', 'Total Amount', 'Total Count']];
                response.forEach(function(item) {
                    chartData.push([item.partner, item.total_amount, item.total_records]);
                });
                var data = google.visualization.arrayToDataTable(chartData);
                var options = {
                    title: 'Line Chart',
                    legend: { position: 'bottom' }
                };
                var chart = new google.visualization.LineChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }
        }
    }
    onSelectRecord(event) {
        this.state.viewType = 'record_table'
        this.state.chartType = null
        const selectedId = event.target.value ? parseInt(event.target.value, 10) : null;
        this.state.selectedRecord = this.state.records.find(record => record.id === selectedId) || null;
        localStorage.setItem("real_estate_selected_record", selectedId || "");
    }
    onSelectChart(event) {
        this.state.viewType = 'graph_view'
        this.state.chartType = event.target.value
    }
}
Realestate.template = "real_estate.Realestate";
registry.category("actions").add("real_estate.real_estate", Realestate);