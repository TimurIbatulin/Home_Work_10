# Задача 2. Доработаем задания 5-6. Создайте класс-фабрику. 
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 

# Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.Задача

# class Fabrica(Animal: class, name, age):

class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                name: str,
                age: int,
                color: str,
                breed: str,
                is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

        def __str__(self):
            if self.is_domestic:
                return f'Dog {self.color} {self.breed} домашняя'
            return f'Dog {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
                age: int,
                name: str,
                number_heads: int = 2) -> None:
                super().__init__(name, age)
                self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads},\
        Возраст: {self.age}, не женат '


class Fish(Animal):

    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
         return f'{self.name} пресноводная'

def fabric(class_animal, * args):
    return class_animal(*args)
    
if __name__ == "__main__":
    dog =  fabric(Dog, 'Бобик', 3, "рыжий", "спаниель", True)
    f1 = fabric(Fish, "Дори", 1, True, 0.5)
    kt1 = fabric(Kotopes, 3, "котопес", 2)
    print(dog)
    print(f1)
    print(kt1)
    kt1.birthday()
    print(kt1)