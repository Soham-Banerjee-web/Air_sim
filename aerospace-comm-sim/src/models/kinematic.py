class Kinematic:
    def __init__(self, speed=0.0, direction=0.0):
        self.speed = speed  # Speed of the aircraft in units per time
        self.direction = direction  # Direction of the aircraft in degrees

    def update_position(self, position, time):
        """
        Update the position of the aircraft based on its speed and direction.

        :param position: A tuple (x, y) representing the current position of the aircraft.
        :param time: Time duration for which the aircraft has been moving.
        :return: A tuple (new_x, new_y) representing the updated position.
        """
        radians = self.direction * (3.141592653589793 / 180)  # Convert degrees to radians
        new_x = position[0] + self.speed * time * cos(radians)
        new_y = position[1] + self.speed * time * sin(radians)
        return new_x, new_y

    def set_speed(self, speed):
        """
        Set the speed of the aircraft.

        :param speed: New speed of the aircraft.
        """
        self.speed = speed

    def set_direction(self, direction):
        """
        Set the direction of the aircraft.

        :param direction: New direction of the aircraft in degrees.
        """
        self.direction = direction

    def get_speed(self):
        """
        Get the current speed of the aircraft.

        :return: Current speed of the aircraft.
        """
        return self.speed

    def get_direction(self):
        """
        Get the current direction of the aircraft.

        :return: Current direction of the aircraft in degrees.
        """
        return self.direction