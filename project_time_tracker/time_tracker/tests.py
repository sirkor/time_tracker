from django.test import TestCase
import datetime


class ActivitiesTest(TestCase):

    def end_less_then_start(self):
        start = datetime.datetime(2016, 1, 1)
        end = datetime.datetime(2015, 1, 1)
        during = end - start
        self.assertLess(during, datetime.timedelta(0), msg='True')