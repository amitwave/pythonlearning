class AnimalActions:
    def quack(self): return self.strings['quack']
    def bark(self): return self.strings['bark']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        bark = "The duck cannot bark.",
    )


class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        bark = "Arf!",
    )
    @staticmethod
    def teststatic():
        print('static')

def in_the_doghouse(dog):
    print(dog.bark())

def in_the_forest(duck):
    print(duck.quack())

def printSquares(start, end):
    for n in range(start, end):
        yield n**2

def main():

    Dog.teststatic()

    donald = Duck()
    fido = Dog()

    print("- In the forest:")
    for o in ( donald, fido ):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in ( donald, fido ):
        in_the_doghouse(o)

    from util.math import add;

    print(add(5, 5));


    print("array");
    arr = [0,1,2,3,4,5]

    print(arr[:])

    import numpy as np
    X = np.array([[3,2], [4,5], [5, 6]])





    minX, maxX = X[:,0].min() -1, X[:,0].max() +1,
    minY, maxY = X[:,1].min() -1, X[:,1].max() +1,

    print("minX ")
    print(minX)
    print("maxX ")
    print(maxX)

    xx, yy = 3,4

    print(xx)
    print(yy)

    mesh_size = 0.1

    x_vals, y_vals = np.meshgrid(np.arange(minX, maxX, mesh_size), np.arange(minY, maxY, mesh_size))




if __name__ == "__main__": main()
