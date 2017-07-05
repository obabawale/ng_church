# -*- coding: utf-8 -*-
"""Church donation report wizard."""
from odoo.exceptions import UserError


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
