class WTF(object):
    def __init__(self):
        self.a = [1,2]

    def b(self):
        return self.a.pop(0)

    def c(self):
        print(self.a)


huehue = WTF()
print(huehue.b())
huehue.c()
#
# a = []
# for x in range(3):
#     b = []
#     for y in range (3):
#         b.append(y)
#     a.append(b)
#
# print(a)