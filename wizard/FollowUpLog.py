# -*- coding:utf-8 -*-
"""Church followership."""
from odoo import fields, models


class FollowupLog(models.TransientModel):
    """."""

    def _default_activity_id(self):
        return self._context['active_ids'][0]

    _name = 'ng_church.followup_log'

    activity_id = fields.Many2one('crm.activity', string='Next Activity',
                                  default=_default_activity_id)
    summary = fields.Char('Summary')
    note = fields.Html('Note')

    def log_and_schedule(self):
        """log and schedule next activity for both."""
        print """log and schedule next activity for both."""

    def log(self):
        """log next activity for both."""
        print """log next activity for both."""
