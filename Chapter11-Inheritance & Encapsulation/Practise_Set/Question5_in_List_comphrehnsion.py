class Vector:

    def __init__(self, values):
        self.values = values   # list of n dimensions

        # print(self.values)

    def __add__(self, other):
        result = [
            self.values[i] + other.values[i]
            for i in range(len(self.values))
        ]
        # Read it in simple English:
        # “Create a list of self.values[i] + other.values[i]
        # for every i in range(len(self.values))   this is list comphrension --In list/generator comprehensions → write WHAT first, HOW later”
        return Vector(result)

    def __mul__(self, other):
        # dot product
        return sum(
            self.values[i] * other.values[i]
            for i in range(len(self.values))
        )

    def __str__(self):
        return f"{tuple(self.values)}"


v1 = Vector([2, 3, 4])
v2 = Vector([4, 5, 6])
v3 = Vector([3, 4, 7])

print(v1 + v2)   # vector addition
print(v1 * v3)   # dot product
