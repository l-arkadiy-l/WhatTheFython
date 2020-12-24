class Tuple:
    def __init__(self, tuple_create: tuple):
        self.tuple_create = tuple_create

    def __sub__(self, other):
        self_create = [i for i in self.tuple_create]
        other_create = [i for i in other.tuple_create]
        for i in range(len(self_create)):
            try:
                self_create[i] -= int(other_create[i])
            except IndexError:
                return tuple(self_create)
            except ValueError:
                tmp = [j for j in other_create[i] if j.isnumeric()]
                if tmp:
                    self_create[i] -= int(''.join(tmp))
        return tuple(self_create)

    def __add__(self, other):
        self_create = [i for i in self.tuple_create]
        other_create = [i for i in other.tuple_create]
        for i in range(len(self_create)):
            try:
                self_create[i] += int(other_create[i])
            except IndexError:
                return tuple(self_create)
            except ValueError:
                tmp = [j for j in other_create[i] if j.isnumeric()]
                if tmp:
                    self_create[i] += int(''.join(tmp))
        return tuple(self_create)
