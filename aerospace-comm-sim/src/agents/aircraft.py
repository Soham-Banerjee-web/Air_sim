class Aircraft:
    def __init__(self, identifier, position, speed, communication_range):
        self.identifier = identifier
        self.position = position  # Position should be a tuple (x, y, z)
        self.speed = speed  # Speed in units per second
        self.communication_range = communication_range  # Communication range in units
        self.state = "ground"  # Possible states: ground, airborne, landing

    def take_off(self):
        if self.state == "ground":
            self.state = "airborne"
            print(f"{self.identifier} is taking off.")
        else:
            print(f"{self.identifier} cannot take off from {self.state} state.")

    def land(self):
        if self.state == "airborne":
            self.state = "landing"
            print(f"{self.identifier} is landing.")
            self.state = "ground"
            print(f"{self.identifier} has landed.")
        else:
            print(f"{self.identifier} cannot land from {self.state} state.")

    def update_position(self, new_position):
        self.position = new_position
        print(f"{self.identifier} has moved to {self.position}.")

    def communicate(self, message):
        print(f"{self.identifier} sending message: {message}")

    def receive_message(self, message):
        print(f"{self.identifier} received message: {message}")