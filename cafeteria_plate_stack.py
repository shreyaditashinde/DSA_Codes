# Cafeteria Plate Stack

class PlateStack:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.stack = []

    # Add Plate (Push)
    def add_plate(self, plate_type, plate_id):
        if len(self.stack) >= self.capacity:
            print("Stack is full! Cannot add more plates.")
            return
        if plate_type not in ["Steel", "Ceramic"]:
            print("Only Steel and Ceramic plates are allowed!")
            return
        for p in self.stack:
            if p["plate_id"] == plate_id:
                print("Plate with this ID already exists!")
                return
        self.stack.append({"type": plate_type, "plate_id": plate_id})
        print(f"{plate_type} Plate with ID {plate_id} added successfully.")

    # Remove Plate (Pop)
    def remove_plate(self):
        if not self.stack:
            print("Stack is empty! No plate to remove.")
            return
        plate = self.stack.pop()
        print(f"{plate['type']} Plate with ID {plate['plate_id']} removed.")

    # View Top Plate (Peek)
    def top_plate(self):
        if not self.stack:
            print("Stack is empty!")
            return
        plate = self.stack[-1]
        print(f"Top Plate: {plate['type']} with ID {plate['plate_id']}")

    # Display Plate Stack
    def display_stack(self):
        if not self.stack:
            print("Stack is empty!")
            return
        print("Plates currently in stack (bottom to top):")
        for p in self.stack:
            print(f"{p['type']} - {p['plate_id']}")


# Example usage

cafeteria_stack = PlateStack()

cafeteria_stack.add_plate("Steel", "P101")
cafeteria_stack.add_plate("Ceramic", "P102")
cafeteria_stack.add_plate("Steel", "P103")

cafeteria_stack.display_stack()
cafeteria_stack.top_plate()

cafeteria_stack.remove_plate()
cafeteria_stack.display_stack()
