# Parking Garage 
class ParkingGarage:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.garage = []

    # Park Vehicle (Push)
    def park_vehicle(self, vehicle_type, reg_number):
        if len(self.garage) >= self.capacity:
            print("Garage is full! Cannot park more vehicles.")
            return
        if vehicle_type not in ["Car", "Bike"]:
            print("Only Car and Bike are allowed!")
            return
        for v in self.garage:
            if v["reg_number"] == reg_number:
                print("Vehicle with this registration number already exists!")
                return
        self.garage.append({"type": vehicle_type, "reg_number": reg_number})
        print(f"{vehicle_type} with Reg No {reg_number} parked successfully.")

    # Exit Vehicle (Pop)
    def exit_vehicle(self):
        if not self.garage:
            print("Garage is empty! No vehicle to exit.")
            return
        vehicle = self.garage.pop()
        print(f"{vehicle['type']} with Reg No {vehicle['reg_number']} exited.")

    # Top Vehicle (Peek)
    def top_vehicle(self):
        if not self.garage:
            print("Garage is empty!")
            return
        vehicle = self.garage[-1]
        print(f"Top Vehicle: {vehicle['type']} with Reg No {vehicle['reg_number']}")

    # Display Parked Vehicles
    def display_vehicles(self):
        if not self.garage:
            print("Garage is empty!")
            return
        print("Vehicles currently parked (from front to back):")
        for v in self.garage:
            print(f"{v['type']} - {v['reg_number']}")


garage = ParkingGarage()

garage.park_vehicle("Car", "MH12AB1234")
garage.park_vehicle("Bike", "MH14XY5678")
garage.park_vehicle("Car", "MH01CD4321")

garage.display_vehicles()
garage.top_vehicle()

garage.exit_vehicle()
garage.display_vehicles()
