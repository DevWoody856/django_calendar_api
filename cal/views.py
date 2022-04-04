import os

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView
from googleapiclient.discovery import build
from cal.forms import BookingForm
from google.oauth2 import service_account


# Google service account
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service_account_email = os.getenv('service_account_email')

credentials = service_account.Credentials.from_service_account_file(os.getenv('credentials'))
scoped_credentials = credentials.with_scopes(SCOPES)
calendarId = os.getenv('calendarId')

def build_service(request):

    service = build("calendar", "v3", credentials=scoped_credentials)
    return service


class HomeView(FormView):
    form_class = BookingForm
    template_name = 'cal/home.html'


    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):

        eventTitle = form.cleaned_data.get("eventTitle")
        start_date_data = form.cleaned_data.get("startDateTime")
        end_date_data = form.cleaned_data.get("endDateTime")

        if start_date_data > end_date_data:
            messages.add_message(self.request, messages.INFO, 'Please enter the correct period.')
            return HttpResponseRedirect(reverse("cal:home"))

        service = build_service(self.request)

        event = (
            service.events().insert(
                calendarId=calendarId,
                body={
                    "summary": eventTitle,
                    "start": {"dateTime": start_date_data.isoformat()},
                    "end": {"dateTime": end_date_data.isoformat()},
                },
            ).execute()
        )

        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = BookingForm()
        booking_event = []
        service = build_service(self.request)
        events = (
            service.events().list(
                calendarId=calendarId,
            ).execute()
        )

        for event in events['items']:

            event_title = event['summary']

            # Deleted the last 6 characters (deleted UTC time)
            start_date_time = event["start"]["dateTime"]
            start_date_time = start_date_time[:-6]

            # Deleted the last 6 characters (deleted UTC time)
            end_date_time = event['end']["dateTime"]
            end_date_time = end_date_time[:-6]

            booking_event.append([event_title, start_date_time, end_date_time])

        context = {
            "form":form,
            "booking_event" : booking_event,
        }

        return context

    def get_success_url(self):

        messages.add_message(self.request, messages.INFO, 'Form submission success!!')

        return reverse('cal:home')