##class vehicle:
##    curr_speed = 0
##
##    def __init__(self,name,model):
##    
##        self.name = name
##        self.model = model
##
##    def start (self, start_speed):
##        self.curr_speed = start_speed
##        print("vehicle has started ")
##
##    def acc(self, acc_speed):
##        self.curr_speed = self.curr_speed + acc_speed
##
##    def brake(self, brake_speed):
##        self.curr_speed = self.curr_speed - brake_speed
##
##    def stop(self):
##        self.curr_speed = 0
##        print("vehicle has stopped")
##
##    def print_status(self):
##        print("vehicle name is " + self.name)
##        print("vehhicle model si " + str(self.model))
##        print("vehicle's current speed id " + str(self.curr_speed))
##        print("--------------------------------------------------")
##
##
##v1 = vehicle("verna" , 2016)
##v1.start(20)
##v1.acc(50)
##v1.acc(50)
##v1.print_status()
##
##
##
##class car(vehicle):
##    def rev(self, rev_speed):
##        curr_speed = -(curr_speed-rev_speed)
##        print("car is getting reversed")
##c1 = car("city" , "2019")
##c1.start(30)
##c1.acc(60)
##c1.brake(30)
##c1.rev(30)
##c1.print_ststus()



class number:
    def __init__(self,x):
        self.x = x
    def __add__(first , second):
        res = first.x - second.x
        print(res)
num1 = number(20)
num2 = number(10)
num1 + num2
    
