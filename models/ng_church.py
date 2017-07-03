# -*- coding: utf-8 -*-
"""Legacy code. As time goes on this should be incrementally refactored."""

from odoo import fields, models


class ChurchSection(models.Model):
    """."""

    _name = 'church.sections'

    name = fields.Char('Church Name', required=True)
    code = fields.Char('Code')
    notes = fields.Text('Notes')
    pastor_id = fields.Many2one('res.partner', string="Pastor")


class MembershipCategory(models.Model):
    """."""

    _name = 'membership.category'

    name = fields.Char('Name', required=True)
    start_age = fields.Integer('Age Start')
    end_age = fields.Integer('Age End')


class MembershipType(models.Model):
    """."""

    _name = 'membership.type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    notes = fields.Text('Notes')


class MembershipStatus(models.Model):
    """."""

    _name = 'membership.status'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    notes = fields.Text('Notes')


class Fellowship(models.Model):
    """."""

    _name = 'fellowship'

    name = fields.Char('Name', required=True)
    marital_status = fields.Selection([('single', 'Single'),
                                       ('married', 'Married'),
                                       ('widower', 'Widower'),
                                       ('divorced', 'Divorced')], string="Marital Status")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
