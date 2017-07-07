# -*- coding:utf-8 -*-
"""Church followership."""
from datetime import date
from odoo import api, fields, models

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Low'),
    ('2', 'High'),
    ('3', 'Very High'),
]


class FollowUp(models.Model):
    """Manage church first timer untill they become full member."""

    _name = 'ng_church.followup'

    name = fields.Many2one('res.partner', string='Name', domain=[
                           ('membership_status_id', '=', 'First Timers')])

    email = fields.Char(related='name.email', string='Email')
    phone = fields.Char(related='name.mobile', string='Phone')
    next_activity_id = fields.Many2one('crm.activity', string='Next Activity')
    stage_id = fields.Many2one('ng_church.stage', string='Stage', index=True, default=1)
    priority = fields.Selection(AVAILABLE_PRIORITIES, string='Priority', default='1')
    date_action = fields.Date('Next Activity Date', index=True)
    color = fields.Integer('Color Index', default=0)
    kanban_state = fields.Selection([('grey', 'No next activity planned'), ('red', 'Next activity late'), ('green', 'Next activity is planned')],
                                    string='Activity State', compute='_compute_kanban_state')

    @api.multi
    def _compute_kanban_state(self):
        today = date.today()
        for followup in self:
            kanban_state = 'grey'
            if followup.date_action:
                followup_date = fields.Date.from_string(followup.date_action)
                if followup_date >= today:
                    kanban_state = 'green'
                else:
                    kanban_state = 'red'
            followup.kanban_state = kanban_state


class Stage(models.Model):
    """Model for case stages."""

    _name = "ng_church.stage"
    _description = "Stage of case"
    _rec_name = 'name'
    _order = "sequence, name, id"

    name = fields.Char('Stage Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    requirements = fields.Text(
        'Requirements', help="Enter here the internal requirements for this stage (ex: Offer sent to customer). It will appear as a tooltip over the stage's name.")
    team_id = fields.Many2one('crm.team', string='Team', ondelete='set null',
                              help='Specific team that uses this stage. Other teams will not be able to see or use this stage.')
    legend_priority = fields.Text('Priority Management Explanation',
                                  help='Explanation text to help users using the star and priority mechanism on stages or issues that are in this stage.')
    fold = fields.Boolean('Folded in Pipeline',
    help='This stage is folded in the kanban view when there are no records in that stage to display.')
