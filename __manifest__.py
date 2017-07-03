# -*- coding: utf-8 -*-
{
    'name': 'Church Management',
    'version': '0.1',
    'author': 'Matt \'O Bell',
    'website': 'www.mattobell.com',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
Church Management
=================
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
temporincididunt ut labore et dolore magna aliqua.Ut enim ad minim
veniam, quisnostrud exercitation ullamco laboris nisi utaliquip
ex ea commodo consequat.
Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia
deserunt mollit anim id est laborum
        """,
    'data': [
            'views/actions.xml',
            'views/menus.xml',
            'security/ng_church_security.xml',
            'security/ir.model.access.csv',
            'views/membership_view.xml',
            'views/inherited/account_invoice_view.xml',
            'views/inherited/res_company_view.xml',
            'data/ng_church_data.xml',
            'data/member_sequence.xml',
            'wizard/ng_church_collections_wizard_view.xml',
            'report/reports.xml',
            'report/print_pledge_report.xml',
            'data/church_pledge_email.xml',
            'views/ng_church_pastor_view.xml',
            'views/ng_church_attendance_view.xml',
            'views/ng_church_church_collections_view.xml',
            'report/church_pledges_report.xml',
            'report/church_attendance_report.xml',
            'report/church_tithe_report.xml',
            'report/church_offering_report.xml',
            'views/ng_church_program.xml',
            'views/ng_church_lodgement.xml'
    ],
    'depends': [
        'account',
        'account_accountant',
        'event',
        'marketing_campaign',
        'sale',
        'purchase',
        'crm',
        'project',
        'account_voucher'
    ],
    'category': 'Human Resources',
    'application': True,
    'installable': True,
    'auto_install': False
}
