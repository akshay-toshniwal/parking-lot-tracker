class ParkingLot:
    def __init__(self):
        self.parking_lot = {}  # Dictionary to store parking spots

    def assign_parking_spot(self, vehicle_number):
        if len(self.parking_lot) >= 40:
            return "Parking lot is full"
        
        if vehicle_number in self.parking_lot:
            return "Vehicle already parked"
        
        level = 'A' if len(self.parking_lot) < 20 else 'B'
        spot_number = len(self.parking_lot) % 20 + 1
        self.parking_lot[vehicle_number] = {'level': level, 'spot': spot_number}
        return f"Assigned parking spot: {{'level': {level}, 'spot': {spot_number}}}"

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.parking_lot:
            return f"Parking spot for {vehicle_number}: {self.parking_lot[vehicle_number]}"
        else:
            return f"No parking spot found for {vehicle_number}"


if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("Options:")
        print("1. Assign a parking spot to a vehicle")
        print("2. Retrieve parking spot for a vehicle")
        print("Type 'exit' to exit the program")

        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter the vehicle number: ")
            print(parking_lot.assign_parking_spot(vehicle_number))
        elif choice == '2':
            vehicle_number = input("Enter the vehicle number: ")
            print(parking_lot.retrieve_parking_spot(vehicle_number))
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")
