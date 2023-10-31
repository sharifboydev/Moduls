# import math

# x = 400
# print(math.sqrt(x))
# print(pow(5, 4))

# from math import pi
# print(pi)

# print(math.log2(8))
# print(math.log10(100))

# a = 5.21
# print(math.ceil(a))
# print(math.floor(a))

import random as r

# son = r.randint(0, 100)
# print(son)

# ismlar = ['olim', 'anvar', 'hasan', 'husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))


# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)


# import math

# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi, 10))

# product = lambda x, y: x ** y
# print(product(3, 2))


# def daraja(n):
#     return lambda x: x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# from math import sqrt
#
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
#
# print(ildizlar)


# sonlar = list(range(11))

# def daraja2(x):
# return x * x


# print(list(map(daraja2, sonlar)))


# kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)

# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son * son)
# print(kvadratlar)
#
# a = [4, 5, 6]
# b = [7, 8, 9]
# a__plus__b = list(map(lambda x, y: x + y, a, b))
# print(a__plus__b)


ismlar = ['hasan', 'husan', 'olim', 'umid']
print(list(map(lambda matn:matn.upper(),ismlar)))