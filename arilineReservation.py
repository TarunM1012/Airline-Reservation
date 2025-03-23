import heapq
import networkx as net
#airline reservation system

class Booking:
    def __init__(self):
        self.seat_queue = []  # Priority queue
        self.referenceNumber = 0   # Unique ID for each booking

    def book_seat(self, passenger_name, priority):
        self.referenceNumber += 1
        heapq.heappush(self.seat_queue, (priority, self.referenceNumber, passenger_name))
        print(f"Seat booked for {passenger_name} with priority {priority}")

    def process_bookings(self):
        print("\nProcessing seat bookings:")
        while self.seat_queue:
            priority, referenceNumber, passenger_name = heapq.heappop(self.seat_queue)
            print(f"Assigned seat to {passenger_name} (Reference Number: {referenceNumber}, Priority: {priority})")

class AirlineReservationSystem:
    def __init__(self):
        self.flight_graph = net.DiGraph()
        self.booking_system = Booking()

    def add_flight(self, source, destination, cost):
        self.flight_graph.add_edge(source, destination, weight=cost)

    def find_shortest_path(self, start, end):
        return shortest_path(self.flight_graph, start, end)

    def book_passenger(self, passenger_name, priority, path, cost):
        if path:
            self.booking_system.book_seat(passenger_name, priority)
        else:
            print(f"No flight path exists for {passenger_name}.")

    def process_bookings(self):
        self.booking_system.process_bookings()

# Dijkstra's algorithm to find the shortest path
def shortest_path(graph, start, end):
    try:
        path = net.dijkstra_path(graph, start, end, weight="weight")
        cost = net.dijkstra_path_length(graph, start, end, weight="weight")
        return path, cost
    except net.NetworkXNoPath:
        return None, float('inf')  # No path exists, return None and infinity

# Main program
if __name__ == "__main__":
    # Create the airline reservation system
    airline_system = AirlineReservationSystem()

    # Add destinations and flights
    destinations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    for city in destinations:
        airline_system.flight_graph.add_node(city)

    airline_system.add_flight("New York", "Chicago", 150)
    airline_system.add_flight("Los Angeles", "Houston", 250)
    airline_system.add_flight("Chicago", "Miami", 200)
    airline_system.add_flight("Houston", "Miami", 100)

    # Display available destinations
    print("Available Origins and Destinations:")
    print("\n".join(destinations))

    # Get user input for origin and destination
    start_city = input("Enter origin: ")
    end_city = input("Enter destination: ")

    # Find the shortest path and cost for the user's input
    path, cost = airline_system.find_shortest_path(start_city, end_city)

    if path:
        print(f"Shortest path from {start_city} to {end_city}: {' -> '.join(path)}")
        print(f"Total cost: ${cost}")
    else:
        print(f"No path exists from {start_city} to {end_city}.")

    # Book seats for Tarun, Vandan, and Juan
    airline_system.book_passenger("Tarun", 1, path, cost)
    airline_system.book_passenger("Vandan", 2, path, cost)
    airline_system.book_passenger("Juan", 3, path, cost)

    # Process bookings
    airline_system.process_bookings()