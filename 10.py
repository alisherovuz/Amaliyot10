#1-masala

# class Talaba:
#      def __init__(self,ism,familiya,birth):
#          self.ism = ism
#          self.familiya = familiya
#          self.birth = birth
#
#      def __str__(self):
#         return f"Ism: {self.ism}\nFamiliya: {self.familiya}\nTug'ilgan yil: {self.birth}"
#
#      def get_name(self):
#          return f"Ism: {self.ism}"
#      def get_last_name(self):
#          return f"Familiya: {self.familiya}"
#      def get_full_name(self):
#          return f"To'liq ism: {self.ism} {self.familiya}"
#      def age(self):
#          return f"Yili: {self.birth}"
#2-masala

#print(Talaba("Nurbek","Alisherov",2008))

# 3-masala
# talaba1 = Talaba("Bobur", "Bozorboyev",2008)
# print(talaba1.get_name())
# talaba2 = Talaba("Sarvarbek", "Alisherov",2008)
# print(talaba2.get_last_name())
# talaba3 = Talaba("Abduvosid","Abdufattoyev",2008)
# print(talaba3.get_full_name())
# print(talaba3.age())


#4-masala

class Car:
    def __init__(self,model, color, weight, high_speed):
        self.model = model
        self.color = color
        self.weight = weight
        self.high_speed = high_speed
    def get_model(self):
        return f"Modeli: {self.model}"
    def get_color(self):
        return f"Rangi: {self.color}"
    def get_weight(self):
        return f"Og'irligi: {self.weight}"
    def get_high_speed(self):
        return f"Maksimal tezligi: {self.high_speed}"
    def get_info(self):
        return f"Modeli: {self.model}\nRangi: {self.color}\nOg'irligi: {self.weight}\nMaksimal tezligi: {self.high_speed}"

# car1 = Car("Cobalt","Oq",1200,180)
# print(car1.get_info())



#5-masala

import math
class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
    def get_color(self):
        return f"Rangi: {self.color}"
    def set_color(self):
        yangi_rang = input("yangi rangni kiriting:  ")
        self.color = yangi_rang
        return f"Yangi rang: {self.color}"

    def get_radius(self):
        return f"Radiusi: {self.radius}"

    def set_radius(self):
        yangi_radius = input("yangi radiusni kiriting:  ")
        self.radius = yangi_radius
        return  f"Yangi radius: {self.radius}"

    def get_area(self):
        yuza = self.radius ** 2 * 3.14
        return yuza
    def get_circumference(self):
        uzunlik = math.pi
        return uzunlik * 2 * self.radius

    def get_info(self):

        return f"Rangi: {self.color}\nRadiusi:{self.radius}\n"


# circle1 = Circle(5,"ko'k")
# print(circle1.get_info())

class Recentagle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def get_height(self):
        return f"Bo'yi: {self.height}"
    def get_width(self):
        return f"Eni: {self.width}"
    def set_height(self):
        yangi_boy = input("Yangi bo'yni kirting:  ")
        self.height = yangi_boy
        return f"Yangi bo'yi: {self.height}"
    def set_width(self):
        yangi_eni = input("Yangi enni kiriting:  ")
        self.width = yangi_eni
        return f"Yangi eni: {self,width}"
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimetr(self):
        perimetr = (self.width + self.height) * 2
        return perimetr
    def get_info(self):
        return f"Bo'yi: {self.height}\nEni: {self.width}"


# num = Recentagle(5,20)
# print(num.get_perimetr())