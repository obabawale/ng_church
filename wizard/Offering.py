# -*- coding: utf-8 -*-
"""Church offering report wizard."""

import datetime
from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError


class ChurchTitheLineAbstractModel(models.AbstractModel):
    """Church TitheLine Abstract Model."""

    _name = 'report.ng_church.church_offering_report'

    def offering_caculator(self, model):
        """offering_caculator."""
        return sum(offering.amount for offering in model)

    @api.model
    def render_html(self, docids, data=None):
        """."""
        name = 'ng_church.church_offering_report'
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(name)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env['ng_church.offering_line'].browse(docids),
            'offering_caculator': self.offering_caculator
        }
        return report_obj.render(name, docargs)


class OfferingReportWizard(models.Model):
    """."""

    _name = 'ng_church.offering_wizard'

    date_from = fields.Date(string='Date from')
    date_to = fields.Date(
        string='Date to', default=lambda self: datetime.datetime.now().strftime('%Y-%m-%d'))
    offering = fields.Many2one('ng_church.program', required=True)

    def _report_range(self, model, after, before):
        if after > before:
            raise UserError('Date from is ahead of date to')
        if after and before:
            model = model.filtered(lambda r: r.date >= after)
            model = model.filtered(lambda r: r.date <= before)
            return model
        elif after:
            model = model.filtered(lambda r: r.date >= after)
            return model
        model = model.filtered(lambda r: r.date <= before)
        return model

    def check_report(self):
        """."""
        query = self.offering
        church = ('church_id', '=', self.env.user.company_id.id)
        services = self.env['ng_church.offering'].search([('service_id', '=', query.id), church])
        offering_line = self.env['ng_church.offering_line']
        for offering in services:
            offering_line += offering_line.search([('offering_id', '=', offering.id), church])
        offerings = self._report_range(offering_line, self.date_from, self.date_to)
        if len(offerings) > 0:
            return self.env['report'].get_action(offerings, 'ng_church.church_offering_report')
        raise MissingError('Record not found')
