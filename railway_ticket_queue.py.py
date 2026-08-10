# Railway Ticket Counter Queue

class TicketQueue:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.queue = []

    # Add Passenger (Enqueue)
    def add_passenger(self, ticket_id, status):
        if len(self.queue) >= self.capacity:
            print("Queue is full! No new passenger can enter.")
            return
        if status != "Confirmed":
            print("Only confirmed passengers can join the queue!")
            return
        for p in self.queue:
            if p["ticket_id"] == ticket_id:
                print("Passenger with this Ticket ID already exists!")
                return
        self.queue.append({"ticket_id": ticket_id, "status": status})
        print(f"Passenger with Ticket ID {ticket_id} added successfully.")

    # Serve Passenger (Dequeue)
    def serve_passenger(self):
        if not self.queue:
            print("Queue is empty! No passenger to serve.")
            return
        passenger = self.queue.pop(0)
        print(f"Passenger with Ticket ID {passenger['ticket_id']} served and removed from queue.")

    # View First Passenger (Front)
    def first_passenger(self):
        if not self.queue:
            print("Queue is empty!")
            return
        passenger = self.queue[0]
        print(f"First Passenger: Ticket ID {passenger['ticket_id']} ({passenger['status']})")

    # Display Passenger Queue
    def display_queue(self):
        if not self.queue:
            print("Queue is empty!")
            return
        print("Passengers currently in queue (front to back):")
        for p in self.queue:
            print(f"Ticket ID: {p['ticket_id']} - Status: {p['status']}")


# Example usage

railway_queue = TicketQueue()

railway_queue.add_passenger("T101", "Confirmed")
railway_queue.add_passenger("T102", "Confirmed")
railway_queue.add_passenger("T103", "Confirmed")

railway_queue.display_queue()
railway_queue.first_passenger()

railway_queue.serve_passenger()
railway_queue.display_queue()
