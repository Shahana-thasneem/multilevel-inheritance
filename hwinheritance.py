class areas:
    def __init__(self,len,brd):
        self.length=len
        self.breadth=brd
        self.pi=3.14

    def round(self,rad):
        self.radius=rad
        self.area=self.pi*self.radius*self.radius
        return self.area
    
    def tri(self,hi):
        self.height=hi
        self.area=0.5*self.length*self.height
        return self.area

class rectangle(areas):
    def __init__(self,len,brd):
        areas.__init__(self,len,brd)
        self.area=self.length*self.breadth

class square(rectangle):
    def __init__(self,len):
        super().__init__(len,len)
        self.area=self.length*self.length

class circle(areas):
    def __init__(self,rad):
        super().__init__(rad,rad)
        self.area=self.round(rad)

class triangle(areas):
    def __init__(self,len,hi):
        super().__init__(len,hi)
        self.area=self.tri(hi)
        
objct1=rectangle(2,3)
objct2=square(5)
objct3=circle(6)
objct4=triangle(4,6)
print("the area of rectangle is",objct1.area)
print("the area of square is",objct2.area)
print("the area of circle is",objct3.area)
print("the area of triangle is",objct4.area)


