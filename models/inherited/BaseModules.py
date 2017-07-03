# *-* coding:utf-8 -*-
"""Inplace inherited model."""
import re

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
from ..helper import parish
import odoo.addons.decimal_precision as dp


class AccountVoucherLine(models.Model):
    """Overide account.voucher line_ids, from readonly=True to False."""

    _inherit = 'account.voucher.line'
    price_unit = fields.Float(string='Unit Price', required=True,
                              digits=dp.get_precision('Product Price'))


class AccountVoucher(models.Model):
    """Overide account.voucher line_ids, from readonly=True to False."""

    _inherit = 'account.voucher'
    line_ids = fields.One2many('account.voucher.line', 'voucher_id', 'Voucher Lines',
                               readonly=False, copy=True,
                               states={'draft': [('readonly', False)]})


class AccountInvoice(models.Model):
    """AccountInvoice."""

    _inherit = 'account.invoice'

    # church_section_id = fields.Many2one('church.sections', string="Church Section")
    # fee_category_id = fields.Many2one('church.fees.category', string="Collection Source")
    # church_service_id = fields.Many2one('ng_church.service', 'Service')
    church_id = fields.Many2one('res.company', string='Church')
    partner_id = fields.Many2one('res.partner', string='Partner', store=True, readonly=True)


class Company(models.Model):
    """Add fields to inherited odoo based model class: res.company."""

    _inherit = 'res.company'

    account = [('user_type_id', '=', 14)]
    journal = [('type', '=', 'sale')]

    name = fields.Char(string='Church Name', required=True)
    rml_header1 = fields.Char(string='Church Tagline ')
    pastor_id = fields.One2many('ng_church.pastor', 'church_id', string='Pastor(s) in Charge')
    program_ids = fields.One2many('ng_church.program', 'parish_id', string='Church Services')
    member_ids = fields.One2many('res.partner', 'parish_id', string='Church Member')
    tithe_ids = fields.One2many('ng_church.tithe', 'church_id', string='Church Tithes')

    tithe_journal = fields.Many2one('account.journal', string="Journal", domain=journal)
    tithe_account = fields.Many2one('account.account', string="Account", domain=account)
    donation_journal = fields.Many2one('account.journal', string="Journal", domain=journal)
    donation_account = fields.Many2one('account.account', string="Account", domain=account)
    offering_journal = fields.Many2one('account.journal', string="Journal", domain=journal)
    offering_account = fields.Many2one('account.account', string="Account", domain=account)
    pledge_journal = fields.Many2one('account.journal', string="Journal", domain=journal)
    pledge_account = fields.Many2one('account.account', string="Account", domain=account)
    transit_account = fields.Many2one(
        'account.account', string='Account', required=True, domain=[('user_type_id', '=', 5)])

    @api.constrains('email')
    def _check_valid_email(self):
        if self.email:
            result = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            if result.match(self.email) is None:
                raise ValidationError('Please enter a valid email address')

    @api.constrains('phone')
    def _check_valid_phone(self, limit=11):
        if self.phone:
            if len(self.phone) > 11:
                raise ValidationError('Please enter a valid phone number')
            result = re.compile(r"\d{11}")
            if result.match(self.phone) is None:
                raise ValidationError('Please enter a valid phone number')


class ResPartner(models.Model):
    """Add the bolow fields to res.partner model."""

    _inherit = 'res.partner'

    member_uniq_id = fields.Char('Member ID')
    is_pastor = fields.Boolean(string='Pastor/Minister')
    is_born_again = fields.Boolean('Born Again?')
    is_spirit_filled = fields.Boolean('Spirit Filled?')
    born_again_date = fields.Date('Born Again Date')
    spirit_filled_date = fields.Date('Spirit Filled Date')
    is_church_member = fields.Boolean('Church Member')
    is_preacher = fields.Boolean('Is Preacher Member?')
    church_section_id = fields.Many2one('church.sections', string="Church Section")
    membership_category_id = fields.Many2one('membership.category', string="Members Category")
    membership_type_id = fields.Many2one('membership.type', string="Membership Type")
    membership_status_id = fields.Many2one('membership.status', string="Membership Status")
    fellowship_id = fields.Many2one('fellowship', string="Fellowship")
    lead_pastor_id = fields.Many2one('res.partner', "Leader Pastor")
    ref_ids = fields.One2many('church.refs', 'emp_id', string='References')
    gua_ids = fields.One2many('church.guarantor', 'emp_id', string='Guarantors')
    kin_ids = fields.One2many('church.nextofkin', 'emp_id', string='Next of Kin')
    dob = fields.Date('Date of Birth')
    joined_date = fields.Date(string='Joined Date')
    parish_id = fields.Many2one('res.company', string='Parish', default=parish)

    _sql_constraints = [
        ('member_id_uniq', 'unique(member_uniq_id)', 'Member ID must be unique!'),
    ]

    @api.onchange('is_pastor')
    def _onchange_is_pastor(self):
        if self.is_pastor == True:
            self.is_church_member = True
