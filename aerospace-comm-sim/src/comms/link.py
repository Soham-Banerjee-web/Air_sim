class Link:
    def __init__(self, aircraft_a, aircraft_b, range_limit):
        self.aircraft_a = aircraft_a
        self.aircraft_b = aircraft_b
        self.range_limit = range_limit
        self.messages = []

    def send_message(self, message):
        if self.is_within_range():
            self.messages.append(message)
            self.aircraft_b.receive_message(message)
        else:
            print(f"Message from {self.aircraft_a.id} to {self.aircraft_b.id} failed: out of range.")

    def is_within_range(self):
        distance = self.calculate_distance()
        return distance <= self.range_limit

    def calculate_distance(self):
        # Placeholder for actual distance calculation logic
        return ((self.aircraft_a.position[0] - self.aircraft_b.position[0]) ** 2 + 
                (self.aircraft_a.position[1] - self.aircraft_b.position[1]) ** 2) ** 0.5

    def get_messages(self):
        return self.messages