# Acceptable values of the status field
new = 'NW'
pending = 'PD'
accepted = 'AC'
rejected = 'AC'

STATUS = [
    (new, 'New'),
    (pending, 'Pending'),
    (accepted, 'Accepted'),
    (rejected, 'Rejected')
]

# Difficulty level of the pass at different
LEVEL = [
    ('A1', 'Simple'),
    ('A2', 'Simple rocks'),
    ('2A', 'Rocky up to 50°'),
    ('2B', 'Cool over 45°'),
    ('3A', 'Cool from 45° to 65°'),
    ('ZB', 'Of great length'),
]

# times of the year
SPRING = 'SP'
SUMMER = 'SU'
AUTUMN = 'AU'
WINTER = 'WI'

SEASONS = [
    (SPRING, 'Spring'),
    (SUMMER, 'Summer'),
    (AUTUMN, 'Autumn'),
    (WINTER, 'Winter'),
]