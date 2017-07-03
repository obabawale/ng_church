# -*- coding: utf-8 -*-
"""Church tithe report wizard."""

import datetime
from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError


class ChurchTitheLineAbstractModel(models.AbstractModel):
    """Church TitheLine Abstract Model."""

    _name = 'report.ng_church.church_tithe_report'

    def tithe_caculator(self, model):
        """tithe_caculator."""
        return sum(tithe.amount for tithe in model)

    @api.model
    def render_html(self, docids, data=None):
        """."""
        name = 'ng_church.church_tithe_report'
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(name)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env['ng_church.tithe_lines'].browse(docids),
            'tithe_caculator': self.tithe_caculator
        }
        return report_obj.render(name, docargs)


class TitheReportWizard(models.Model):
    """."""

    _name = 'ng_church.tithe_wizard'

    date_from = fields.Date(string='Date from')
    date_to = fields.Date(
        string='Date to', default=lambda self: datetime.datetime.now().strftime('%Y-%m-%d'))
    tithe = fields.Selection(selection=[('all', 'All'), ('members', 'Members'), ('pastor', 'Pastor'),
                                        ('minister', 'Minister')], string='Category', default='all', required=True)

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
        query = self.tithe
        church = ('church_id', '=', self.env.user.company_id.id)
        domain = [('tithe_type', '=', query), church] if self.tithe != 'all' else [church]
        tithes = self._report_range(self.env['ng_church.tithe_lines'].search(
            domain), self.date_from, self.date_to)
        if len(tithes) > 0:
            return self.env['report'].get_action(tithes, 'ng_church.church_tithe_report')
        raise MissingError('Record not found')
