class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
        self.Radius = float(input("Enter a radius of circle : "))

    def CalculateArea(self):

        self.Area = Circle.PI * self.Radius ** 2
        

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        

    def Display(self):
        
        print("Radius is : ", self.Radius)
        print("Area is : ", self.Area)
        print("Circumference is : ", self.Circumference)

objcircle = Circle()

objcircle.Accept()
objcircle.CalculateArea()
objcircle.CalculateCircumference()
objcircle.Display()

