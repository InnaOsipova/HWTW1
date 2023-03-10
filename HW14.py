# В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# Из условий видно что у нас есть один возможный вариант выигрыша из всех сочетаний 2 по 100

from math import factorial


# Нужно найти вероятность, это отношение благоприятных событий к числу всех  событий

def probability (m, n):
    return m/n

# функция по расчету сочетаний
def combinations (k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))

# Решение
print(f" Вероятность купить 2 выигрышных билета из 100 = {round(probability(1, combinations(2,100))*100,2)} %")