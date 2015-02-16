from datetime import datetime, timedelta

from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib import messages

import icalendar

from . import forms


class IndexView(FormView):
    template_name = 'base.html'
    form_class = forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        msg = "We have received your message, we will now decide your fate"
        messages.add_message(self.request, messages.INFO, msg)
        return super(IndexView, self).form_valid(form)


class ICSView(View):

    def get(self, *args):
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

        return HttpResponse(content=calendar.to_ical())
