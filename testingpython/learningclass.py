
class Person:
    school = "ABC University"
    def __init__(self,name,age,cost):
        self.name = name
        self.age = age
        self.__cost = cost
    
    def great(self):
        return f"Hello, my name is {self.name} and I am {slf.age} years old"
    
    def get_cost(self):
        return self.__cost

class Student(Person):
    def __init__(self,name,age,cost,grade):
        super().__init__(name,age,cost)
        self.grade = grade

p1 = Person("john", 36 , 500)
print(p1.great())
print(p1.school)

s1 = Student("jane", 25, 1000,"A")
print(s1.great())
print(s1.grade)
print(s1.get_cost())