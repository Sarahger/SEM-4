class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passenger_list = []

    def flight_details(self):
        print(f"Flight Details :\nRoute: {self.origin} --> {self.destination}\nDeparture: {self.departure_time}\nArrival: {self.arrival_time}\n")

    def book_seat(self, passenger_name):
        if self.available_seats > 0:
            self.passenger_list.append(passenger_name)
            self.available_seats -= 1
            print(f"\n------Seat booked for {passenger_name} on flight {self.flight_number}-------\n")
        else:
            print("Sorry, no available seats on this flight.\n")

    def get_available_seats(self):
        return self.available_seats

class Passenger:
    def __init__(self, name, age, passport_number):
        self.name = name
        self.age = age
        self.passport_number = passport_number

class ReservationSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def book_seat(self, flight_number, passenger_name):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            flight.book_seat(passenger_name)
        else:
            print("Flight not found.")

    def display_available_seats(self, flight_number):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            print(f"Available seats on flight {flight_number}: {flight.get_available_seats()}")
        else:
            print("Flight not found.")

    def add_to_waitlist(self, flight_number, passenger_name):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            flight.add_to_waitlist(passenger_name)
        else:
            print("Flight not found.")


flight1 = Flight("ABC123", "New York", "Los Angeles", "8:00", "11:00", 100)
flight2 = Flight("PQR678","Dubai","India","9:00","12:00",200)
flight3 = Flight("XYZ111","India","New York","1:00","12:00",150)

reservation_system = ReservationSystem()
reservation_system.add_flight(flight1)
reservation_system.add_flight(flight2)
reservation_system.add_flight(flight3)

print("                    Flight Reservation System")

reservation_system.book_seat("PQR678","Kevin")
reservation_system.display_available_seats("PQR678")
flight2.flight_details()

reservation_system.book_seat("XYZ111","Aishwarya")
reservation_system.display_available_seats("XYZ111")
flight3.flight_details()