import unittest
from src.agents.aircraft import Aircraft
from src.comms.link import Link
from src.comms.protocol import Protocol

class TestCommunication(unittest.TestCase):

    def setUp(self):
        self.aircraft1 = Aircraft(id="A1", position=(0, 0))
        self.aircraft2 = Aircraft(id="A2", position=(1, 1))
        self.link = Link(self.aircraft1, self.aircraft2)
        self.protocol = Protocol()

    def test_message_sending(self):
        message = "Hello from A1"
        self.link.send_message(self.aircraft1, message)
        received_message = self.aircraft2.receive_message()
        self.assertEqual(received_message, message)

    def test_message_receiving(self):
        message = "Hello from A2"
        self.link.send_message(self.aircraft2, message)
        received_message = self.aircraft1.receive_message()
        self.assertEqual(received_message, message)

    def test_protocol_handling(self):
        self.protocol.register_aircraft(self.aircraft1)
        self.protocol.register_aircraft(self.aircraft2)
        self.assertIn(self.aircraft1, self.protocol.aircrafts)
        self.assertIn(self.aircraft2, self.protocol.aircrafts)

if __name__ == '__main__':
    unittest.main()