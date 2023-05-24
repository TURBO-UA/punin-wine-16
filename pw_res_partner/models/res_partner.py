from odoo import api, fields, models


class HrEmployeeInherit(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    birthday = fields.Date(string='Date of birth')
