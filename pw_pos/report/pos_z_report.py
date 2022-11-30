
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class ZReport(models.AbstractModel):
    _name = 'report.pw_pos.report_zreport'
    _inherit = 'report.point_of_sale.report_saledetails'
    _description = 'Z Report'

    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False):
        res = super(ZReport, self).get_sale_details(date_start, date_stop, config_ids, session_ids)
        session_id = self.env['pos.session'].browse(session_ids)
        res.update({
            'session_number': session_id[0].name,
            'receipt_number': len(session_id[0].order_ids),
        })
        return res

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})
        if 'config_ids' not in data:
            # Run from Print menu
            session_id = self.env['pos.session'].browse(docids)
            data.update({
                'session_ids': session_id.ids,
                'config_ids': session_id.mapped('config_id').ids,
                'date_start': session_id.start_at,
                'date_stop': session_id.stop_at,
            })

        configs = self.env['pos.config'].browse(data['config_ids'])
        data.update(self.get_sale_details(
            data['date_start'],
            data['date_stop'],
            configs.ids,
            data['session_ids']))
        return data
