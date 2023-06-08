from django.test import TestCase
from scheduler.models import Schedule, Timeslot
from django.utils.timezone import datetime

# # Create your tests here.

class ScheduleModelClass(TestCase):
    @classmethod

    def setUpTestData(cls):
       Schedule.objects.create(name = 'name', description = 'description')

    def test_name_label(self):
        schedule = Schedule.objects.get(id = 1)
        field_label = schedule._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        schedule = Schedule.objects.get(id = 1)
        field_label = schedule._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

class TimeslotModelClass(TestCase):
    @classmethod

    def setUpTestData(cls):
       Timeslot.objects.create(start = "2023-06-07" , end = "2023-06-09")

    def test_start_label(self):
        timeslot = Timeslot.objects.get(id = 1)
        # current_date = datetime.now()
        current_date = timeslot.end
        
        if(current_date > timeslot.start):
            print("works")
        else:
            print("past")
        field_label = timeslot._meta.get_field('start').verbose_name
        self.assertEqual(field_label, 'start')

    def test_end_label(self):
        timeslot = Timeslot.objects.get(id = 1)
        field_label = timeslot._meta.get_field('end').verbose_name
        self.assertEqual(field_label, 'end')