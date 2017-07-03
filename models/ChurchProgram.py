# *-* coding:utf-8 -*-
"""."""
from odoo import fields
from odoo import models
from helper import parish


class ChurchProgram(models.Model):
    """ChurchService."""

    _name = 'ng_church.program'

    name = fields.Char('Name', required=True)
    days = fields.Selection([('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                             ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                             ('Sunday', 'Sunday')], string='Day')
    start = fields.Float(string='Start Time')
    end = fields.Float(string='End Time')
    meridiem = fields.Selection([('AM', 'AM'), ('PM', 'PM')], string='')
    parish_id = fields.Many2one('res.company', string='Parish', default=parish)
