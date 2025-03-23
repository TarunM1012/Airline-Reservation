Welcome to the Airline Reservation System project! This project is a Python-based implementation of an airline reservation system that models 
flight routes as a graph and uses advanced data structures and algorithms to find the shortest path between cities and manage seat bookings efficiently. 

Graph-Based Flight Routes:

Cities are modeled as vertices.

Flights are modeled as edges with weights representing cost or time.

Built using the networkx library for graph operations.

Shortest Path Calculation:

Implements Dijkstra's Algorithm to find the cheapest or fastest route between two cities.

Handles cases where no path exists between cities.

Priority Queue for Seat Bookings:

Uses Python's heapq module to manage seat bookings.

Assigns seats based on priority (e.g., booking time or passenger status).


Required libraries - networkx (install with - pip install networkx)
