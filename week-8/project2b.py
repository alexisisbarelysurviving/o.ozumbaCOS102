class Location():

    def __init__(self, location):
        self.location = location
        self.location_verification = False

    location_names = ["PAU", "Epe"]
    
    def check_location(self):
        if self.location in Location.location_names:
            print('location accessible')
            self.location_verification = True
            
so = Location(input('What is your location: '))
 
so.check_location()

class weight():