class ConsCell:
    def __init__(self, h, t):
        """ Creates a new cell with head == h, and tail == t."""
        self.head = h
        self.tail = t


class List:
    """ Describes a simple list data type ."""

    def __init__(self, n):
        """ creates a new list with n as the first element ."""
        self.start = n

    def cons(self, e):
        """ Adds a new element into the list ; hence , procuding a new list"""
        return List(ConsCell(e, self.start))

    def __str__(self):
        """ Returns a textual representation of this list ."""
        ans = "["
        cell = self.start
        while cell != 0:
            ans = ans + repr(cell.head)
            cell = cell.tail
            if cell != 0:
                ans = ans + ", "
        ans = ans + "]"
        return ans

    def length(self):
        size = 0
        cell = self.start
        while cell != 0:
            size += 1
            cell = cell.tail
        return size

    def contains(self, n):
        cell = self.start
        while cell != 0:
            if cell.head == n:
                return True
            cell = cell.tail
        return False

    def sum(self):
        result = 0
        cell = self.start
        while cell != 0:
            if isinstance(cell.head, int):
                result += cell.head
            cell = cell.tail
        return result

    def concatAux(self, result, cell):
        if cell == 0:
            return result

        result = self.concatAux(result, cell.tail)

        return result.cons(cell.head)

    def concat(self, l):
        result = List(0)
        result = self.concatAux(result, l.start)
        cell = self.start
        while cell != 0:
            result = result.cons(cell.head)
            cell = cell.tail
        return result


def test():
    a = List(0)
    b = a.cons(2)
    c = b.cons("Hi!")
    d = b.cons(True)
    e = d.cons(False)
    print(" List a = ", a.__str__())
    print(" List b = ", b.__str__())
    print(" List c = ", c.__str__())
    print(" List d = ", d.__str__())
    print(" List e = ", e.__str__())

    print("1)\n")
    a = List(0)
    b = a.cons(2)
    print("Length(a) = ", a.length())
    print("Length(b) = ", b.length())

    print("2)\n")
    a = List(0)
    b = a.cons(2)
    c = b.cons("hi")
    print(b.contains(1))
    print(b.contains(2))
    print(c.contains("hi"))

    print("3)\n")
    a = List(0)
    b = a.cons(2)
    c = b.cons("hi")
    d = c.cons(1)
    print(d.sum())

    print("4)\n")
    a = List(0)
    b = a.cons(2)
    c = b.cons("Hi")
    d = b.cons("hello")
    print(c)
    print(d)
    print(c.concat(d))


test()
