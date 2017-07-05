# -*- coding:utf-8 -*-
"""."""
import datetime
from odoo import api
from odoo import fields
from odoo import models
from helper import parish
from helper import program_default_date
from helper import default_date


class ProgramAttendance(models.Model):
    """."""

    _name = 'ng_church.attendance'

    name = fields.Many2one('ng_church.program', string='Service')
    date = fields.Date(string='Date')
    parish_id = fields.Many2one('res.company', string='Parish', default=parish)
    attendance_line_ids = fields.One2many(
        'ng_church.attendance_line', 'attendance_id', string='Program Attendance')

    @api.onchange('name')
    def _onchange_name(self):
        date = program_default_date(self)
        self.date = date

    class AttendanceLine(models.Model):
        """."""

        _name = 'ng_church.attendance_line'
        date = fields.Date(string='Date', default=default_date)
        name = fields.Char(string='Name')
        male = fields.Integer(string='Male')
        female = fields.Integer(string='Female')
        guest = fields.Integer(string='Guest')
        total = fields.Integer(string='Total', compute='_compute_total')
        children = fields.Integer(string='Children')
        section_id = fields.Many2one('church.sections', string='Church Section')
        attendance_id = fields.Many2one('ng_church.attendance', string='Attendance')

        @api.onchange('date')
        def _onchange_name(self):
            if self.date:
                date = self.date.split('-')
                date.reverse()
                date = '/'.join(date)
                timestamps = datetime.datetime.strptime(date, '%d/%m/%Y')
                self.name = "{:%B %d, %Y}".format(timestamps)

        @api.onchange('male', 'female', 'guest', 'children')
        def _onchage_population(self):
            """Calcalate total number of male, female, and children."""
            sumamtion = abs(int(self.male)) + abs(int(self.female)) + abs(int(self.guest))
            self.total = sumamtion
            if self.children:
                sumamtion = 0
                sumamtion = abs(int(self.children))
                self.total = sumamtion

        @api.depends('male', 'female', 'guest', 'children')
        @api.one
        def _compute_total(self):
            """Calcalate total number of male, female, and children."""
            sumamtion = abs(int(self.male)) + abs(int(self.female)) + abs(int(self.guest))
            self.total = sumamtion
            if self.children:
                sumamtion = 0
                sumamtion = abs(int(self.children))
            self.total = sumamtion
