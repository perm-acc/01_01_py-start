class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        NumStr = len(self.a)
        NumCol = len(other.a[0])
        for i in range(NumStr):
            for j in range(NumCol):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            Result = self.a
        return Matrix(Result)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 0], [1, 2]])


print(matrix_1 + matrix_2)