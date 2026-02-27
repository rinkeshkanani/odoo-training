# -*- coding: utf-8 -*-
from odoo.http import Controller, route, request


class OwlDashboard(Controller):

    @route('/apply/filter', type='json', auth='public', csrf=False)
    def apply_filter(self, date):
        domain = [('date', '=', date)] if date else []
        partner_data = request.env['real.estate'].read_group(
            domain=domain,
            fields=['amount'],
            groupby=['partner_id'],
            lazy=False,
        )
        result = [{
            'partner': data['partner_id'][1],
            'total_records': data['__count'],
            'total_amount': data['amount'],
        } for data in partner_data]
        return result

    
    