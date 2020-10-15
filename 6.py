class Visitor:
    "A parameterized list visitor."

    def __init__(self, cb):
        self.cb = cb

    def __str__(self):
        return "Visitor with callback: {0}".format(self.cb)

    def visit(self, n):
        for i in range(0, len(n)):
            n[i] = self.cb.update(n[i])
        return n


class CallbackBase:
    "The basic callback"

    def __init__(self):
        self.f = lambda x: x + 1

    def __str__(self):
        return"basic callback"

    def shouldUpdate(self, i):
        return True

    def update(self, i):
        return self.f(i) if self.shouldUpdate(i) else i

class CallbackCube(CallbackBase):
    def __init__(self):
        self.f = lambda x: x ** 3

    def __str__(self):
        return"cube callback"

class CallbackOdd(CallbackBase):
    def shouldUpdate(self, i):
        return i % 2 == 1

    def __str__(self):
        return"odd callback"

class CallbackMult(CallbackOdd, CallbackCube):
    def __str__(self):
        return"multiple callback"

def test():
    # Inicio
    v = Visitor(CallbackBase())
    print(v)
    print(v.visit([2, 3, 4]))

    # Letra a)
    a = Visitor(CallbackCube())
    print(a)
    print(a.visit([2, 3, 4]))

    # Letra b)
    b = Visitor(CallbackOdd())
    print(b)
    print(b.visit([2, 3, 4]))

    # Letra c) Um objeto do tipo Visitor, parametrizado com um objeto do tipo
    # CallbackMult, ao visitar uma lista de n elementos inteiros, irá alterar
    # somente os elementos ímpares, atualizando estes com seu cubo.
    c = Visitor(CallbackMult())
    print(c)
    print(c.visit([2, 3, 4]))

test()