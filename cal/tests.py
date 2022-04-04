from django.test import TestCase, Client
from django.urls import reverse

from cal.forms import BookingForm


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_context_data(self):
        response = self.client.get('')
        form_data =  ['Foo 2', '2022-03-02T07:00:00', '2022-03-02T09:30:00']
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookingForm)
        self.assertEqual(response.context['booking_event'][0], form_data)

    def test_post(self):
        form_data = {'eventTitle':'Foo 2', 'startDateTime':'2022-03-02T07:00:00','endDateTime':'2022-03-02T09:30:00'}
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())


