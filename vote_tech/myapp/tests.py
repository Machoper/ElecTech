# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class Tests(TestCase):

	def test_smoke_test(self):
		x = 99
		assert(x == 99)