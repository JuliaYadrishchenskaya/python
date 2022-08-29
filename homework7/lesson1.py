#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#который должен принимать данные (список списков)
#для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
#Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)


l1 = [[1,2,4],[3,4,5],[5,6,6]]
l2 = [[11,21,41],[31,41,51],[51,61,61]]
m = Matrix(l1)
s = Matrix(l2)
print(m)
z = m + s
print('z ')
print(z)
print(type(z))