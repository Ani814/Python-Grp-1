"""
Hotel Booking Agency — Back-End (Python)

Classes: Room, Customer, Hotel
Features: room management, booking, payment, dynamic seasonal pricing,
reward points, and logging (via the `logging` module + a log file).
"""

import logging
from datetime import datetime

# ---------------------------------------------------------------------------
# Logging configuration — every operation (booking / cancellation) is
# written to bookings.log and also echoed to the console.
# ---------------------------------------------------------------------------
logger = logging.getLogger("hotel_booking")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("bookings.log", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(console_handler)


# ---------------------------------------------------------------------------
# Dynamic pricing helper — seasonal multiplier
# ---------------------------------------------------------------------------
def seasonal_multiplier(month: int = None) -> float:
    """
    Returns a price multiplier based on the month:
    - High season (Jun-Aug, Dec): x1.5
    - Mid season (Apr-May, Sep-Oct): x1.2
    - Low season (everything else): x1.0
    """
    if month is None:
        month = datetime.now().month

    if month in (6, 7, 8, 12):
        return 1.5
    if month in (4, 5, 9, 10):
        return 1.2
    return 1.0


# ---------------------------------------------------------------------------
# Room
# ---------------------------------------------------------------------------
class Room:
    """A single room in the hotel."""

    def __init__(self, room_number: int, room_type: str, price_per_night: float,
                 max_guests: int, is_available: bool = True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.max_guests = max_guests

    def book_room(self):
        """Mark the room as booked."""
        self.is_available = False

    def release_room(self):
        """Mark the room as available again (used when a booking is cancelled)."""
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        """Total price for a stay, factoring in nights and the current season."""
        if nights <= 0:
            raise ValueError("Number of nights must be a positive integer")
        return round(self.price_per_night * nights * seasonal_multiplier(), 2)

    def __str__(self):
        status = "available" if self.is_available else "booked"
        return (f"Room #{self.room_number} | Type: {self.room_type} | "
                f"Price: {self.price_per_night} GEL/night | "
                f"Max guests: {self.max_guests} | Status: {status}")


# ---------------------------------------------------------------------------
# Customer
# ---------------------------------------------------------------------------
class Customer:
    """A customer making bookings."""

    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        """Add a room to the customer's list of bookings."""
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        """Remove a room from the customer's list of bookings."""
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        """
        Attempt payment: if the budget is sufficient, deduct the amount
        and award reward points (1 point per 10 GEL spent).
        """
        if total_price <= 0:
            return False
        if self.budget < total_price:
            return False

        self.budget -= total_price
        earned_points = int(total_price // 10)
        self.reward_points += earned_points
        return True

    def show_booking_summary(self) -> str:
        """String summary of the customer's booked rooms and remaining budget."""
        if not self.booked_rooms:
            return f"{self.name} has no active bookings."

        lines = [f"{self.name}'s bookings:"]
        for room in self.booked_rooms:
            lines.append(f"  - Room #{room.room_number} ({room.room_type})")
        lines.append(f"Remaining budget: {self.budget:.2f} GEL")
        lines.append(f"Reward points: {self.reward_points}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Hotel
# ---------------------------------------------------------------------------
class Hotel:
    """The hotel management class."""

    def __init__(self, name: str, rooms: list = None):
        self.name = name
        self.rooms = rooms if rooms is not None else []
        self.bookings_log = []

    def show_available_rooms(self, room_type: str = None) -> list:
        """Return the list of available rooms, optionally filtered by type."""
        available = [room for room in self.rooms if room.is_available]
        if room_type:
            available = [room for room in available if room.room_type.lower() == room_type.lower()]
        return available

    def _find_room(self, room_number: int) -> Room:
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def calculate_total_booking(self, room_number: int, nights: int) -> float:
        """Total price for a given room and number of nights."""
        room = self._find_room(room_number)
        if room is None:
            raise ValueError(f"Room #{room_number} was not found")
        return room.calculate_price(nights)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:
        """
        Book a specific room for a customer:
        - the room must exist and be available
        - the customer must have a sufficient budget
        """
        room = self._find_room(room_number)
        if room is None or not room.is_available:
            logger.info(f"Booking failed | Customer: {customer.name} | "
                        f"Room #{room_number} is not available")
            return False

        total_price = self.calculate_total_booking(room_number, nights)

        if not customer.pay_for_booking(total_price):
            logger.info(f"Payment failed | Customer: {customer.name} | "
                        f"Required: {total_price} GEL | Budget: {customer.budget} GEL")
            return False

        room.book_room()
        customer.add_room(room)
        self.log_booking(customer, room, total_price)
        return True

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        """Record the booking in the in-memory history and in the log file."""
        entry = {
            "customer": customer.name,
            "room_number": room.room_number,
            "room_type": room.room_type,
            "total_price": total_price,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
        self.bookings_log.append(entry)
        logger.info(f"Booking confirmed | Customer: {customer.name} | "
                    f"Room #{room.room_number} ({room.room_type}) | "
                    f"Total: {total_price} GEL")

    def cancel_booking(self, customer: Customer, room_number: int):
        """Cancel a booking — the room is released and unlinked from the customer."""
        room = self._find_room(room_number)
        if room is None:
            logger.info(f"Cancellation failed | Room #{room_number} was not found")
            return False

        if room not in customer.booked_rooms:
            logger.info(f"Cancellation failed | {customer.name} has no booking "
                        f"for room #{room_number}")
            return False

        room.release_room()
        customer.remove_room(room)
        logger.info(f"Booking cancelled | Customer: {customer.name} | "
                    f"Room #{room_number}")
        return True


# ---------------------------------------------------------------------------
# Sample data — 10 rooms
# ---------------------------------------------------------------------------
def create_sample_hotel() -> Hotel:
    rooms = [
        Room(101, "Single", 80, 1),
        Room(102, "Single", 80, 1),
        Room(103, "Single", 85, 2),
        Room(201, "Double", 130, 2),
        Room(202, "Double", 135, 2),
        Room(203, "Double", 140, 3),
        Room(301, "Suite", 250, 4),
        Room(302, "Suite", 260, 4),
        Room(401, "Suite", 400, 6),
        Room(402, "Double", 150, 2),
    ]
    return Hotel("Tbilisi Grand Hotel", rooms)


# ---------------------------------------------------------------------------
# Interactive CLI demo
# ---------------------------------------------------------------------------
def run_cli():
    hotel = create_sample_hotel()
    print(f"=== Welcome to {hotel.name} ===")

    name = input("Enter your name: ").strip()
    try:
        budget = float(input("Enter your budget (GEL): ").strip())
    except ValueError:
        budget = 1000.0
        print("Invalid value, budget set to 1000 GEL.")

    customer = Customer(name, budget)

    while True:
        print("\n--- Menu ---")
        print("1. View available rooms")
        print("2. Book a room")
        print("3. Cancel a booking")
        print("4. View my bookings")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            room_type = input("Type (Single/Double/Suite) or Enter for all: ").strip() or None
            available = hotel.show_available_rooms(room_type)
            if not available:
                print("No available rooms found.")
            for room in available:
                print(room)

        elif choice == "2":
            try:
                room_number = int(input("Room number: ").strip())
                nights = int(input("Number of nights: ").strip())
            except ValueError:
                print("Please enter valid numbers.")
                continue

            try:
                total = hotel.calculate_total_booking(room_number, nights)
            except ValueError as e:
                print(e)
                continue

            print(f"Total price: {total} GEL")
            success = hotel.book_room_for_customer(customer, room_number, nights)
            print("Booking successful!" if success else "Booking could not be completed.")

        elif choice == "3":
            try:
                room_number = int(input("Room number to cancel: ").strip())
            except ValueError:
                print("Please enter a valid number.")
                continue
            success = hotel.cancel_booking(customer, room_number)
            print("Cancelled." if success else "Cancellation failed.")

        elif choice == "4":
            print(customer.show_booking_summary())

        elif choice == "5":
            print("Thank you, have a great day!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    run_cli()
