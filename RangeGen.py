#Generates a range of numbers, interation, and a dog speaks

class Dog():
    name = 'Fido'

    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Woof, woof! My name is {0}".format(self.name))


bob = Dog('Bob')
sally = Dog('Sally')

sally.talk()
bob.talk()


class MyRange():
    def __init__(self, start, end, step):
        self.counter = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.end:
            current_number = self.counter
            self.counter += self.step
            return current_number
        else:
            raise StopIteration

for i in MyRange(0, 10, 1):
    print(i)
