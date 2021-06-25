# получить атрибуты класса - имя класса.__dict__
# dic = range.__dict__
# for i in dic:
#     print(f"{i}:{dic[i]}")

class Person:
    age = 44
    sex = 'female'
    profession = 'teacher'


ira = Person
print(ira.__dict__)
Person.profession
print(getattr(Person, 'sexa'))