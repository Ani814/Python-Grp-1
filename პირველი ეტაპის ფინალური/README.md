# Tbilisi Grand Hotel — Booking Agency System

A full-stack hotel booking project built as a final assignment for a Python course.
It combines an object-oriented Python back-end with a semantic HTML/CSS front-end.

## Features

- **Room management** — add, book, and release rooms; filter by type and availability
- **Dynamic pricing** — price scales with number of nights and current season
  (high / mid / low season multipliers)
- **Customer accounts** — budget tracking, payment validation, reward points
  (1 point per 10 GEL spent)
- **Booking engine** — books only available rooms, rejects bookings that exceed budget
- **Logging** — every booking, failed payment, and cancellation is written to
  `bookings.log` via Python's `logging` module
- **Cancellations** — releases the room and unlinks it from the customer
- **Unit tested** — 11 `unittest` cases covering `Room`, `Customer`, and `Hotel`
- **Interactive CLI** — a simple text-based front end to the back-end logic
- **Front-end UI** — a static HTML/CSS/JS page that mirrors the room list,
  booking form, and booking status

## Project structure

```
.
├── backend/
│   ├── hotel_booking.py       # Room, Customer, Hotel classes + CLI
│   └── test_hotel_booking.py  # unittest suite (11 tests)
├── frontend/
│   └── index.html             # Booking UI (HTML + embedded CSS/JS)
└── README.md
```

## Architecture

### `Room`
| Attribute | Type | Description |
|---|---|---|
| `room_number` | `int` | Room number |
| `room_type` | `str` | `Single`, `Double`, or `Suite` |
| `price_per_night` | `float` | Base nightly rate |
| `is_available` | `bool` | Availability flag |
| `max_guests` | `int` | Occupancy limit |

Methods: `book_room()`, `release_room()`, `calculate_price(nights)`, `__str__()`

### `Customer`
| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | Customer name |
| `budget` | `float` | Available funds |
| `booked_rooms` | `list` | Rooms currently booked |
| `reward_points` | `int` | Loyalty points |

Methods: `add_room()`, `remove_room()`, `pay_for_booking(total_price)`, `show_booking_summary()`

### `Hotel`
| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | Hotel name |
| `rooms` | `list` | All `Room` objects |
| `bookings_log` | `list` | In-memory booking history |

Methods: `show_available_rooms(room_type=None)`, `book_room_for_customer(customer, room_number, nights)`,
`calculate_total_booking(room_number, nights)`, `log_booking(customer, room, total_price)`,
`cancel_booking(customer, room_number)`

## Getting started

### Requirements
- Python 3.8+
- No third-party packages — standard library only

### Run the CLI

```bash
cd backend
python3 hotel_booking.py
```

### Run the tests

```bash
cd backend
python3 -m unittest test_hotel_booking.py -v
```

### View the front-end

Open `frontend/index.html` directly in a browser. It runs entirely client-side
with a small embedded JavaScript booking simulation; it is not wired to the
Python back-end over a network (no server layer was required by the assignment).

## Notes

- All console/log output is in English to avoid encoding issues in terminals
  that don't support non-Latin character sets.
- `bookings.log` is generated at runtime and is git-ignored.
