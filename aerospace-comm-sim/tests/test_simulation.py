import unittest
from src.sim.simulation import Simulation
from src.agents.aircraft import Aircraft
from src.environment.region import Region

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.region = Region(boundaries=(0, 0, 100, 100))
        self.simulation = Simulation(region=self.region)
        self.aircraft1 = Aircraft(id="A1", position=(10, 10), speed=250)
        self.aircraft2 = Aircraft(id="A2", position=(20, 20), speed=300)
        self.simulation.add_aircraft(self.aircraft1)
        self.simulation.add_aircraft(self.aircraft2)

    def test_initialization(self):
        self.assertEqual(len(self.simulation.aircraft), 2)
        self.assertEqual(self.simulation.region.boundaries, (0, 0, 100, 100))

    def test_run_simulation(self):
        self.simulation.run()
        # Add assertions to verify the expected state after running the simulation
        self.assertTrue(self.aircraft1.position[0] > 0)
        self.assertTrue(self.aircraft2.position[0] > 0)

    def test_aircraft_communication(self):
        self.aircraft1.send_message("Hello from A1")
        received_message = self.aircraft2.receive_message()
        self.assertEqual(received_message, "Hello from A1")

if __name__ == "__main__":
    unittest.main()