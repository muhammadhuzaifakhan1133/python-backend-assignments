from datetime import date, datetime


class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.bookings = []

    def add_new_room(self, name, no_of_beds, fare_per_day):
        room = Room(
            name=name,
            no_of_beds=no_of_beds,
            fare_per_day=fare_per_day,
        )
        self.rooms.append(room)

    def book_room(self, room_id, user_name, date):
        if (self._is_date_valid(date) == False):
            print("Date is not valid")
            return
        if (self.is_room_available(room_id, date) == False):
            print("Room is already booked on given date.")
            return
        booking = Booking(room_id=room_id, user_name=user_name, date=date)
        self.bookings.append(booking)

    def get_room(self, room_id):
        for room in self.rooms:
            if room.id == room_id:
                return room
            
    def get_booking(self, room_id, date):
        for booking in self.bookings:
            if booking.room_id == room_id and booking.date == date:
                return booking
            
    def _is_date_valid(self, _date):
        return _date >= date.today()
            
    def _is_room_exist(self, room_id):
        return self.get_room(room_id) != None

    def show_all_rooms(self):
        for room in self.rooms:
            print(room)

    def show_occupied_rooms(self, date):
        for booking in self.bookings:
            if (booking.date == date):
                print(self.get_room(booking.room_id))

    def show_available_rooms(self, date):
        for room in self.rooms:
            booking = self.get_booking(room.id, date)
            if (booking == None):
                print(room)

    def is_room_available(self, room_id, date):
        if not(self._is_room_exist(room_id)):
            raise Exception("Room is not exist")
        for booking in self.bookings:
            if booking.room_id == room_id and booking.date == date:
                return False
        return True


class Room:
    count = 0

    def __init__(self, name, no_of_beds, fare_per_day):
        Room.count += 1
        self.id = Room.count
        self.name = name
        self.no_of_beds = no_of_beds
        self.fare_per_day = fare_per_day

    def __str__(self):
        return f"Room(id={self.id}, name={self.name}, no_of_beds={self.no_of_beds}, fare_per_day={self.fare_per_day})"


class Booking:
    def __init__(self, room_id, user_name, date):
        self.room_id = room_id
        self.user_name = user_name
        self.date = date

hotel = Hotel(name="Shahi Darbar", address="Highway")
hotel.add_new_room(name="Room1", no_of_beds=3, fare_per_day=200)
hotel.add_new_room(name="Room2", no_of_beds=1, fare_per_day=75)
hotel.add_new_room(name="Room3", no_of_beds=5, fare_per_day=300)
hotel.book_room(2, "Huzaifa", date(2023, 9, 22))
hotel.book_room(2, "Huzaifa", date(2023, 9, 22))
print(hotel.is_room_available(2, date(2023, 9, 22)))
hotel.show_all_rooms()
print("Avaiable Rooms")
hotel.show_available_rooms(date(2023, 9, 22))
print("Occupied Rooms")
hotel.show_occupied_rooms(date(2023, 9, 22))