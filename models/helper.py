"""Boilerplate code to avoid repetition."""


def parish(object):
    """return current user's church/parish."""
    parish_id = object.env.user.company_id.id
    return parish_id


daily_activities = [
    ('First Week Tuesday',    'First Week Tuesday'),
    ('First Week Wednesday',  'First Week Wednesday'),
    ('First Week Thursday ',  'First Week Thursday'),
    ('First Week Friday',     'First Week Friday'),
    ('First Week Saturday',   'First Week Saturday'),
    ('First Week Sunday',     'First Week Sunday'),
    ('Second Week Tuesday',   'Second Week Tuesday'),
    ('Second Week Wednesday', 'Second Week Wednesday'),
    ('Second Week Thursday ', 'Second Week Thursday'),
    ('Second Week Friday',    'Second Week Friday'),
    ('Second Week Saturday',  'Second Week Saturday'),
    ('Second Week Sunday',    'Second Week Sunday'),
    ('Third Week Tuesday',    'Third Week Tuesday'),
    ('Third Week Wednesday',  'Third Week Wednesday'),
    ('Third Week Thursday ',  'Third Week Thursday'),
    ('Third Week Friday',     'Third Week Friday'),
    ('Third Week Saturday',   'Third Week Saturday'),
    ('Third Week Sunday',     'Third Week Sunday'),
    ('Fourth Week Tuesday',   'Fourth Week Tuesday'),
    ('Fourth Week Wednesday', 'Fourth Week Wednesday'),
    ('Fourth Week Thursday ', 'Fourth Week Thursday'),
    ('Fourth Week Friday',    'Fourth Week Friday'),
    ('Fourth Week Saturday',  'Fourth Week Saturday'),
    ('Fourth Week Sunday',    'Fourth Week Sunday'),
    ('Fifth Week Tuesday',    'Fifth Week Tuesday'),
    ('Fifth Week Wednesday',  'Fifth Week Wednesday'),
    ('Fifth Week Thursday ',  'Fifth Week Thursday'),
    ('Fifth Week Friday',     'Fifth Week Friday'),
    ('Fifth Week Saturday',   'Fifth Week Saturday'),
    ('Fifth Week Sunday',     'Fifth Week Sunday')
]
month_list = [
    ('January', 'January'), ('February', 'February'), ('March', 'March'),
    ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'),
    ('August', 'August'), ('September', 'September'),
    ('October', 'October'), ('November', 'November'),
    ('December', 'December')
]
