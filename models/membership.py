# -*- coding: utf-8 -*-
"""."""

from odoo import fields, models, api, _
import re

DATETIME_FORMAT = "%Y-%m-%d"


class Associate(models.Model):
    """."""

    _name = 'ng_church.associate'
    name = fields.Char(string='Full Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')


class church_guarantor(models.Model):
    """."""

    _name = 'church.guarantor'

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender', required=False)
    marital = fields.Selection([('single', 'Single'), ('married', 'Married'), ('widower',
                                                                               'Widower'), ('divorced', 'Divorced')], string='Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection([('e', 'Employed'), ('s', ' Self Employed'),
                               ('u', 'Unemployed')], string='Work Status', required=False)
    state = fields.Selection(selection=[
        ('not_verify', 'Not Verified'),
        ('verify', 'Verified'),
        ('declined', 'Declined')],
        string='Status', readonly=False, required=True, default='not_verify')
    employer = fields.Char(string='Employer')
    notes = fields.Text(string='Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    @api.multi
    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        if self.email:
            if not email_re.match(self.email):
                raise Warning(_('Warning'), _('Please enter valid email address'))
        return True


class church_nextofkin(models.Model):
    _name = 'church.nextofkin'

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender', required=False)
    marital = fields.Selection([('single', 'Single'), ('married', 'Married'),
                                ('widower', 'Widower'), ('divorced', 'Divorced')], 'Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection([('e', 'Employed'), ('s', ' Self Employed'),
                               ('u', 'Unemployed')], 'Status', required=False)
    employer = fields.Char(string='Employer')
    notes = fields.Text(string='Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    @api.multi
    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        if self.email:
            if not email_re.match(self.email):
                raise Warning(_('Warning'), _('Please enter valid email address'))
        return True


class church_ref(models.Model):
    _name = 'church.refs'

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')], string='Gender', required=False)
    marital = fields.Selection(selection=[('single', 'Single'), ('married', 'Married'), (
        'widower', 'Widower'), ('divorced', 'Divorced')], string='Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection(selection=[(
        'e', 'Employed'), ('s', ' Self Employed'), ('u', 'Unemployed')], string='Work Status', required=False)
    state = fields.Selection(selection=[
        ('not_verify', 'Not Verified'),
        ('verify', 'Verified')],
        string='Status', default='not_verify', readonly=True)
    user = fields.Many2one('res.users', string='Verified By', required=False, readonly=True)
    employer = fields.Char('Employer')
    notes = fields.Text('Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    @api.multi
    def verify(self):
        return self.write({'state': 'verify', 'user': self._uid})

    @api.multi
    def notverify(self):
        return self.write({'state': 'not_verify', 'user': self._uid})

    @api.multi
    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        if self.email:
            if not email_re.match(self.email):
                raise Warning(_('Warning'), ('Please enter a valid email address'))
        return True
