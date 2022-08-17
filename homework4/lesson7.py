#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор.
#Функция вызывается следующим образом: for el in fact(n).
#Она отвечает за получение факториала числа.
#В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)