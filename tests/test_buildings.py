# tests.test_buildings
# test module to evaluate the classes in the buildings module
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_buildings.py [] allen.leis@georgetown.edu $

"""
Test cases for buildings module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Garage
from motorsports.buildings import Car

##########################################################################
## Tests
##########################################################################

class GarageTests(unittest.TestCase):

    def test_has_name(self):
        """
        Ensure the garage returns the name provided at creation
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        self.assertEqual(name, g.name)

    def test_allows_cars_to_enter(self):
        """
        Ensure the garage allows Car object to enter
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('blue', 'Honda', 'Accord')
        g.enter(c)

    def test_ensure_cars_enter_fully(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('blue', 'Honda', 'Accord')
        g.enter(c)
        self.assertIn(c, g)

    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Garage('foo')
        with self.assertRaises(TypeError) as context:
            g.enter(c)

    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = { 'foo' : 42 }
        with self.assertRaises(TypeError) as context:
            g.exit(c)

    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles can leave the garage
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('white', 'Toyota', 'Camry')
        g.enter(c)
        g.exit(c)

    def test_ensure_cars_exit_fully(self):
        """
        Ensure vehicle is not in garage after it exits
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('white', 'Toyota', 'Camry')
        g.enter(c)
        g.exit(c)
        self.assertFalse(c in g)

    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c = Car('white', 'Toyota', 'Camry')
        with self.assertRaises(LookupError) as context:
            g.exit(c)

    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c1 = Car('white', 'Toyota', 'Camry')
        c2 = Car('black', 'Toyota', 'Camry')
        g.enter(c1)
        g.enter(c2)
        self.assertIn(c1, g)
        self.assertIn(c2, g)

    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number of vehicles parked in it
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        c1 = Car('white', 'Toyota', 'Camry')
        c2 = Car('black', 'Toyota', 'Camry')
        g.enter(c1)
        g.enter(c2)
        self.assertEquals(2, len(g))
