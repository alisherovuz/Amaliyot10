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

car1 = Car("Cobalt","Oq",1200,180)
print(car1.get_info())



