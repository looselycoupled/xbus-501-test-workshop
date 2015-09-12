# tests.test_vehicles
# test module to evaluate the classes in the vehicles module
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_vehicles.py [] allen.leis@georgetown.edu $

"""
Test cases for vehicles module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Car, BaseVehicle

##########################################################################
## Tests
##########################################################################

class VehicleTests(unittest.TestCase):

    def test_description(self):
        """
        Ensure the car description return a string of: "color, make model"
        """
        color = 'white'
        make = 'Ford'
        model = 'Bronco'
        c = Car(color, make, model)
        self.assertEquals(c.description, '{} {} {}'.format(color, make, model))

    def test_initial_state_is_stopped(self):
        """
        Ensure the a car's initial state is "stopped"
        """
        c = Car('Black', 'BMW', '335i')
        self.assertEquals('stopped', c.state)

    def test_state_after_start(self):
        """
        Ensure the car's state is "started" after using start method
        """
        c = Car('Black', 'BMW', '335i')
        c.start()
        self.assertEquals('started', c.state)

    def test_state_after_stop(self):
        """
        Ensure the car's state is "stopped" after using shutdown method
        """
        c = Car('Black', 'BMW', '335i')
        c.start()
        c.shutdown()
        self.assertEquals('stopped', c.state)

    def test_str_builtin(self):
        """
        Ensure the car evaluates to a string of
        "I am a <car color>, <car make>, <car model>."
        """
        color = 'white'
        make = 'Ford'
        model = 'Bronco'
        c = Car(color, make, model)
        self.assertEquals(str(c), 'I am a {} {} {}.'.format(color, make, model))

    def test_color_requirement(self):
        """
        Ensure the car requires a color argument during instantiation
        """
        make = 'Ford'
        model = 'Bronco'
        with self.assertRaises(TypeError) as context:
            c = Car(make=make, model=model)

    def test_make_requirement(self):
        """
        Ensure the car requires a make argument during instantiation
        """
        color = 'red'
        model = 'Bronco'
        with self.assertRaises(TypeError) as context:
            c = Car(color=color, model=model)

    def test_model_requirement(self):
        """
        Ensure the car requires a model argument during instantiation
        """
        color = 'red'
        make = 'Ford'
        with self.assertRaises(TypeError) as context:
            c = Car(make=make, color=color)

    def test_state_read_only(self):
        """
        Ensure the car state attribute is read only and throws
        AttributeError if someone tries to assign a value directly
        """
        c = Car('Black', 'BMW', '335i')
        with self.assertRaises(AttributeError) as context:
            c.state = 'foo'

    def test_car_is_a_vehicle(self):
        """
        Ensure a car object is also an instance of BaseVehicle
        """
        c = Car('Black', 'BMW', '335i')
        self.assertIsInstance(c, BaseVehicle)
