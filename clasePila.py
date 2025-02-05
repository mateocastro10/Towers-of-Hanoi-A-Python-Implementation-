class Pila:
    def __init__(self, xcant):
        self.cant = xcant
        self.tope = -1
        self.items = [0] * self.cant

    def vacia(self):
        return self.tope == -1

    def insertar(self, x):
        if self.tope < self.cant - 1:
            self.tope += 1
            self.items[self.tope] = x
            return x
        else:
            return None

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            x = self.items[self.tope]
            self.tope -= 1
            return x

    def mostrar(self):
        if not self.vacia():
            for i in range(self.tope, -1, -1):
                print(self.items[i])