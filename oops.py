# # from abc import ABC, abstractmethod
# import keyboard as k
# print(k)

# # # class vehical (ABC):
# # #     @abstractmethod
# # #     def start (self):

# # #         pass
# # #     @abstractmethod
# # #     def wheeel(self,no_of_weels):
# # #         pass


# # # class car(vehical):
# # #     def start(self):
# # #         print("car is start with key")
# # #     def wheeel(self, no_of_weels):
# # #         print("no/of",no_of_weels)
# # # class bike(vehical):
# # #     def start(self):
# # #         print("car is start with key")
# # #     def wheeel(self, no_of_weels):
# # #         print("no/of",no_of_weels)


# # # car_obj=car()
# # # car_obj.start()
# # # car_obj.wheeel(4)
# # # print("+++++++++++++")


# # # bike_obj=bike()
# # # bike_obj.start()
# # # bike_obj.wheeel(3)

# # class animal(ABC):
# #     @abstractmethod
# #     def speck(self,animal_voice):
# #         pass
   
# # class dog(animal):
# #     def speck(self,animal_voice):
# #         print("dog",animal_voice)
# # class cat(animal):
# #     def speck(self, animal_voice):
# #         print("cat",animal_voice)
# # dog_obj=dog()
# # dog_obj.speck("bow bow")

# # print("--------------")

# # cat_obj=cat()
# # cat_obj.speck("meow meow")


# # class employ:
# #     def set1(self,name_of_emp):
# #         self.name=name_of_emp
# #     def get1(self):
# #         return self.name
# #     def set2(self,emp_salary):
# #         self.salary=emp_salary
# #     def get2(self):
# #         return self.salary
# #     def set3(self,emp_pin):
# #         self.pin=emp_pin
# #     def get3(self):
# #         return self.pin
# # obj=employ()
# # obj.set1("nani")
# # obj.set2(11234)
# # print(obj.get1())
# # print(obj.get2())



# class india:
#     def capital(self):
#         self.name="delhi"
#         print(self.name)
#     def N_language(self):
#         self.lang="hindi"
#         print(self.lang)
# class america:
#     def capital(self):
#         self.name="washing tondc"
#     def N_language(self):
#         self.lang="english"

# def method(data):
#     data.capital()
#     data.N_language()
# obj=india()
# method(obj)
# print()


class default:
    def __init__(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print(a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print(a+c+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print( "enater any two numbers")
obj=default(12,23)

class Bank:
    def createaccount(self,user,accontno):
        self.user=user
        self.accont=accontno
        self.money=0
        
    def deposite(self,accontno,money):
        if self.accont==accontno:
            self.money+=money
            print(self.money)


obj=Bank()
obj.createaccount("nani",123)
obj.deposite(123,11223)


        


