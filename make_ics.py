from datetime import datetime, timedelta
import icalendar

dates = [
    datetime(2015, 2, 16, 18, 0, 0),
    datetime(2015, 3,  2, 18, 0, 0),
    datetime(2015, 3, 16, 18, 0, 0),
    datetime(2015, 3, 30, 18, 0, 0),
    datetime(2015, 4, 13, 18, 0, 0),
    datetime(2015, 4, 27, 18, 0, 0),
    datetime(2015, 5, 11, 18, 0, 0),
    datetime(2015, 5, 25, 18, 0, 0),
]

calendar = icalendar.Calendar()

for date in dates:
    event = icalendar.Event()
    event.add('summary', 'Django School')
    event.add('dtstart', date)
    event.add('dtend', date + timedelta(hours=3))
    calendar.add_component(event)

with open('django_school.ics', 'wb') as f:
    f.write(calendar.to_ical())
