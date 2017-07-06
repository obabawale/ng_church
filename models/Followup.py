# -*- coding:utf-8 -*-
"""Church followership."""

from odoo import api, fields, models


class FollowUp(models.Model):
    """Manage church first timer untill they become full member."""

    _name = 'ng_church.followup'

    name = fields.Many2one('res.partner', string='Name', domain=[
                           ('membership_status_id', '=', 'First Timers')])

    email = fields.Char(related='name.email', string='Email')
    phone = fields.Char(related='name.phone', string='Phone')
    next_activity_id = fields.Many2one('crm.activity', string='Next Activity')
    membership_status = fields.Selection(selection=[
        ('First Timers', 'First Timer'),
        ('Members', 'Full Member')], string='Membership Status', default='new')
    priority = fields.Selection(
        selection=[('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority', default='1')
    date_action = fields.Date('Next Activity Date', index=True)

    @api.onchange('state')
    def _onchange_membership_status(self):
        print '***********************************************print'
