import unittest
from unittest import skip

class InitializationTests(unittest.TestCase):

    def test_import_motorsports(self):
        """
        Ensure the test suite can import the motorsports module
        """
        try:
            import motorsports
        except ImportError:
            self.fail("Was not able to import motorsports")

    def test_import_buildings(self):
        """
        Ensure the test suite can import the buildings module
        """
        try:
            import motorsports.buildings
        except ImportError:
            self.fail("Was not able to import the buildings module")

    def test_import_vehicles(self):
        """
        Ensure the test suite can import the vehicles module
        """
        try:
            import motorsports.vehicles
        except ImportError:
            self.fail("Was not able to import the vehicles module")
