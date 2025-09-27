import random
from agents.aircraft import Aircraft
from sim.scheduler import Scheduler
from environment.region import Region

class Simulation:
    def __init__(self, region, num_aircraft):
        self.region = region
        self.aircraft = [Aircraft(f"Aircraft-{i}", self.region) for i in range(num_aircraft)]
        self.scheduler = Scheduler()
        self.time = 0

    def initialize_aircraft(self):
        for aircraft in self.aircraft:
            aircraft.initialize()

    def schedule_events(self):
        for aircraft in self.aircraft:
            self.scheduler.schedule_event(aircraft.takeoff, self.time + random.randint(1, 5))

    def run(self, duration):
        self.initialize_aircraft()
        self.schedule_events()
        
        while self.time < duration:
            self.scheduler.execute_events(self.time)
            self.time += 1

if __name__ == "__main__":
    region = Region("Test Region", boundaries=(0, 100, 0, 100))
    simulation = Simulation(region, num_aircraft=5)
    simulation.run(duration=10)