# -*- coding: utf-8 -*-
"""."""

from odoo import api, fields, models
from odoo.exceptions import MissingError
import datetime


class ChurchAttendanceLineAbstractModel(models.AbstractModel):
    """PledgesReport."""

    _name = 'report.ng_church.church_attendance_report'

    def attendance_line_mutator(self, model):
        """Mutate the state of the original report(s)."""
        attendance_name = model[0].attendance_id.attendance_line_ids
        return model, attendance_name[-1]

    def attendance_census(self, model):
        """."""
        male = 0
        female = 0
        children = 0
        guest = 0
        total = 0
        for population in model:
            male += population.male
            female += population.female
            children += population.children
            guest += population.guest
            total += population.total
        return ['Total:', male, female, children, guest, total]

    @api.model
    def render_html(self, docids, data=None):
        """."""
        name = 'ng_church.church_attendance_report'
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(name)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env['ng_church.attendance_line'].browse(docids),
            'attendance_line_mutator': self.attendance_line_mutator,
            'attendance_census': self.attendance_census
        }
        return report_obj.render(name, docargs)


class ChurchAttendanceLine(models.TransientModel):
    """."""

    _name = 'ng_church.attendance_wizard'

    attendance = fields.Many2one('ng_church.attendance', string="Service", required=True)
    date_from = fields.Date(string='Start Date')
    date_to = fields.Date(
        string='End Date', default=lambda self: datetime.datetime.now().strftime('%Y-%m-%d'))

    def _report_exist(self, report):
        # check if incomming report is empty, if true return MissingError
        if len(report) <= 0:
            raise MissingError('Attendance record does not exist for selected date range.')

    def check_report(self):
        """."""
        attendance = self.attendance
        report = self.env['ng_church.attendance_line'].search(
            [('attendance_id', '=', attendance.id)])
        self._report_exist(report)
        if self.date_from and self.date_to:
            attendance_line_from = report.filtered(lambda r: r.date >= self.date_from)
            attendance_line_to = attendance_line_from.filtered(lambda r: r.date <= self.date_to)
            self._report_exist(attendance_line_to)
            return self.env['report'].get_action(attendance_line_to, 'ng_church.church_attendance_report')
        elif self.date_from:
            attendance_line_from = report.filtered(lambda r: r.date >= self.date_from)
            self._report_exist(attendance_line_from)
            return self.env['report'].get_action(attendance_line_from, 'ng_church.church_attendance_report')
        elif self.date_to:
            attendance_line_to = report.filtered(lambda r: r.date <= self.date_to)
            self._report_exist(attendance_line_to)
            return self.env['report'].get_action(attendance_line_to, 'ng_church.church_attendance_report')
        return self.env['report'].get_action(report, 'ng_church.church_attendance_report')
