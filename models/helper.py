"""Boilerplate code to avoid repetition."""
import datetime
from odoo.exceptions import MissingError


def parish(object):
    """return current user's church/parish."""
    parish_id = object.env.user.company_id.id
    return parish_id


def default_date(self):
    """Return today's current date."""
    return datetime.datetime.now().strftime('%Y-%m-%d')


month_list = [
    ('January', 'January'), ('February', 'February'), ('March', 'March'),
    ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'),
    ('August', 'August'), ('September', 'September'),
    ('October', 'October'), ('November', 'November'),
    ('December', 'December')
]


def program_default_date(self, date=datetime.date.today()):
    """ISO weekday."""
    if self.name.days is False:
        raise MissingError('Service day is not set on the selected Church Program')
    day = self.name.days
    isoweekday = {
        'monday': 1, 'tuesday': 2, 'wednesday': 3,
        'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7
    }
    program_day = int(isoweekday[day.lower()])  # program day of the week
    today = int(datetime.date.isoweekday(date))  # current day of the week
    days = program_day - today
    if days > 0:
        days = datetime.timedelta(7 - days)
        program_date = date - days
        return program_date
    days = datetime.timedelta(abs(days))
    program_date = date - days
    return program_date


def program_default_date_tithe(self, date=datetime.date.today()):
    """ISO weekday."""
    if self.service_id.days is False:
        raise MissingError('Service day is not set on the selected Church Program')
    day = self.service_id.days
    isoweekday = {
        'monday': 1, 'tuesday': 2, 'wednesday': 3,
        'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7
    }
    program_day = int(isoweekday[day.lower()])  # program day of the week
    today = int(datetime.date.isoweekday(date))  # current day of the week
    days = program_day - today
    if days > 0:
        days = datetime.timedelta(7 - days)
        program_date = date - days
        return program_date
    days = datetime.timedelta(abs(days))
    program_date = date - days
    return program_date
