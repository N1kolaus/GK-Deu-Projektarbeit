from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f"Hello, my name is {self.name}")

    def say_time():
        print(f"Es ist {datetime.now().strftime('%H')} Uhr.")


if __name__ == "__main__":
    person1 = Person("Johannes", 29)
    person1.say_name()
    person1.say_time()
