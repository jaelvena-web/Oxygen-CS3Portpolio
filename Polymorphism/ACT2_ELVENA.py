class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

start_trip(car1)
start_trip(boat1)
start_trip(drone1)