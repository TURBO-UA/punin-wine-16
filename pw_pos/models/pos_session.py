
import base64
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class POS_Session(models.Model):
    _inherit = 'pos.session'

    def create_zreport(self):
        for session_id in self:
            report = self.env['ir.actions.report']._render_qweb_pdf("pw_pos.report_z_report_act", self.id)[0]
            filename = 'Z Report session[%s] %s.pdf' % (session_id.id, fields.Datetime.now())

            self.env['ir.attachment'].create({
                'name': filename,
                'type': 'binary',
                'datas': base64.b64encode(report).decode(),
                'res_model': 'pos.session',
                'res_id': session_id.id,
                'mimetype': 'application/x-pdf'
            })
            # Открыть сформированный отчет, только не так! Потому что так мы сформируем новый отчет!
            # return self.env.ref('point_of_sale.sale_details_report').report_action([], data=data)  #._render_qweb_pdf(r)

    def action_pos_session_close(self, balancing_account=False, amount_to_balance=0, bank_payment_method_diffs=None):
        res = super(POS_Session, self).action_pos_session_close(balancing_account, amount_to_balance, bank_payment_method_diffs)
        if res:
            self.create_zreport()
        return res


