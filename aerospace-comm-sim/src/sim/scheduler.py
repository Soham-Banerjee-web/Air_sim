from datetime import datetime
import heapq

class Scheduler:
    def __init__(self):
        self.events = []

    def schedule_event(self, event_time, event):
        heapq.heappush(self.events, (event_time, event))

    def run(self):
        while self.events:
            event_time, event = heapq.heappop(self.events)
            current_time = datetime.now()
            if event_time <= current_time:
                event()
            else:
                # If the event time is in the future, reschedule it
                self.schedule_event(event_time, event)
                break

    def clear(self):
        self.events.clear()