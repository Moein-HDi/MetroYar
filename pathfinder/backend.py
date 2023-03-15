import heapq

class Stop:
    def __init__(self, name, line):
        self.name = name
        self.line = line

class Station:
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines

    def __repr__(self):
        return f"Station('{self.name}', {self.lines})"

    def __lt__(self, other):
        return self.name < other.name
        

class SubwaySystem:
    def __init__(self):
        self.stations = {}

    def add_station(self, station):
        self.stations[station] = {}

    def add_connection(self, station1, station2, distance):
        self.stations[station1][station2] = distance
        self.stations[station2][station1] = distance

    def shortest_path(self, start_station, end_station):
        # Initialize distances to all stations as infinity
        distances = {station: float('inf') for station in self.stations}
        distances[start_station] = 0

        # Initialize a priority queue to hold stations to be processed
        queue = [(0, start_station)]

        # Initialize a dictionary to keep track of the previous station in the shortest path
        prev_station = {}

        while queue:
            # Get the station with the smallest distance so far
            current_distance, current_station = heapq.heappop(queue)

            # If we've reached the end station, reconstruct and return the shortest path
            if current_station == end_station:
                path = []
                while current_station != start_station:
                    path.append(current_station)
                    current_station = prev_station[current_station]
                path.append(start_station)
                path.reverse()
                return (path, current_distance)

            # Otherwise, update the distances and add the station's neighbors to the queue
            for neighbor, distance in self.stations[current_station].items():
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
                    prev_station[neighbor] = current_station

        # If we get here, there's no path from start_station to end_station
        return None



