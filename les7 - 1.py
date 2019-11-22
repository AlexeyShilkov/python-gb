class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


    def __add__(self, other):
        a =[]
        b = []
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                a.append(self.matrix[i][n] + other.matrix[i][n])
                if len(a) == len(self.matrix):
                    b.append(a)
                    a = []

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in b]))


matrix_1 = Matrix([[1, 12, 23], [23, 44, 90], [67, -5, 19]])
matrix_2 = Matrix([[15, 175, -9], [3, 414, 1], [-55, -5, -19]])
print(f'{matrix_1}\n')
print(f'{matrix_2}\n')
print(matrix_1 + matrix_2)
