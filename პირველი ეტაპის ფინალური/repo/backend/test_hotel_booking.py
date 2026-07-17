"""
Tests for hotel_booking.py (unittest).
Run with: python -m unittest test_hotel_booking.py -v
"""

import unittest
from hotel_booking import Room, Customer, Hotel, seasonal_multiplier


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(101, "Single", 100, max_guests=1)

    def test_book_and_release_room(self):
        self.assertTrue(self.room.is_available)
        self.room.book_room()
        self.assertFalse(self.room.is_available)
        self.room.release_room()
        self.assertTrue(self.room.is_available)

    def test_calculate_price(self):
        price = self.room.calculate_price(3)
        expected = round(100 * 3 * seasonal_multiplier(), 2)
        self.assertEqual(price, expected)

    def test_calculate_price_invalid_nights(self):
        with self.assertRaises(ValueError):
            self.room.calculate_price(0)


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice", budget=500)
        self.room = Room(201, "Double", 100, max_guests=2)

    def test_pay_for_booking_success_reduces_budget(self):
        result = self.customer.pay_for_booking(150)
        self.assertTrue(result)
        self.assertEqual(self.customer.budget, 350)
        self.assertEqual(self.customer.reward_points, 15)

    def test_pay_for_booking_insufficient_budget(self):
        result = self.customer.pay_for_booking(9999)
        self.assertFalse(result)
        self.assertEqual(self.customer.budget, 500)

    def test_add_and_remove_room(self):
        self.customer.add_room(self.room)
        self.assertIn(self.room, self.customer.booked_rooms)
        self.customer.remove_room(self.room)
        self.assertNotIn(self.room, self.customer.booked_rooms)


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.rooms = [
            Room(101, "Single", 80, max_guests=1),
            Room(102, "Single", 80, max_guests=1, is_available=False),
            Room(201, "Double", 130, max_guests=2),
        ]
        self.hotel = Hotel("Test Hotel", self.rooms)
        self.customer = Customer("Bob", budget=1000)

    def test_show_available_rooms(self):
        available = self.hotel.show_available_rooms()
        self.assertEqual(len(available), 2)
        self.assertNotIn(self.rooms[1], available)

    def test_show_available_rooms_filtered_by_type(self):
        available = self.hotel.show_available_rooms("Single")
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].room_number, 101)

    def test_book_room_for_customer_only_available_rooms(self):
        # Booking an available room should succeed
        success = self.hotel.book_room_for_customer(self.customer, 101, nights=2)
        self.assertTrue(success)
        self.assertFalse(self.rooms[0].is_available)

        # Booking an already-booked room should fail
        already_booked = self.hotel.book_room_for_customer(self.customer, 102, nights=1)
        self.assertFalse(already_booked)

    def test_book_room_fails_with_insufficient_budget(self):
        poor_customer = Customer("Charlie", budget=10)
        success = self.hotel.book_room_for_customer(poor_customer, 201, nights=5)
        self.assertFalse(success)
        self.assertTrue(self.rooms[2].is_available)

    def test_cancel_booking(self):
        self.hotel.book_room_for_customer(self.customer, 101, nights=1)
        cancelled = self.hotel.cancel_booking(self.customer, 101)
        self.assertTrue(cancelled)
        self.assertTrue(self.rooms[0].is_available)
        self.assertNotIn(self.rooms[0], self.customer.booked_rooms)


if __name__ == "__main__":
    unittest.main()
