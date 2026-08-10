# Food Delivery Order Queue

class OrderQueue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = []

    # Place Order (Enqueue)
    def place_order(self, order_id, status):
        if len(self.queue) >= self.capacity:
            print("Queue overflow! Cannot accept more orders.")
            return
        if status != "Confirmed":
            print("Only confirmed orders are accepted!")
            return
        for o in self.queue:
            if o["order_id"] == order_id:
                print("Order with this ID already exists!")
                return
        self.queue.append({"order_id": order_id, "status": status})
        print(f"Order {order_id} placed successfully.")

    # Prepare Order (Dequeue)
    def prepare_order(self):
        if not self.queue:
            print("Queue is empty! No order to prepare.")
            return
        order = self.queue.pop(0)
        print(f"Order {order['order_id']} prepared and removed from queue.")

    # View Next Order (Peek)
    def next_order(self):
        if not self.queue:
            print("Queue is empty!")
            return
        order = self.queue[0]
        print(f"Next Order: {order['order_id']} ({order['status']})")

    # Display Order Queue
    def display_queue(self):
        if not self.queue:
            print("Queue is empty!")
            return
        print("Orders currently in queue (front to back):")
        for o in self.queue:
            print(f"Order ID: {o['order_id']} - Status: {o['status']}")


# Example usage

orders = OrderQueue()

orders.place_order("O101", "Confirmed")
orders.place_order("O102", "Confirmed")
orders.place_order("O103", "Confirmed")

orders.display_queue()
orders.next_order()

orders.prepare_order()
orders.display_queue()
