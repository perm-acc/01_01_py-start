from functools import reduce
gen_list = [el for el in range(100, 1000, 2)]
def m_list(x, y):
    return x * y
print(reduce(m_list, gen_list))