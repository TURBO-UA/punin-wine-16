from odoo import api, fields, models


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    date_of_issue = fields.Date(string='Date of issue', help='Passport issue date')
    date_of_expiry = fields.Date(string='Date of expiry', help='Passport expiration date')
    authority = fields.Char(string='Authority')
