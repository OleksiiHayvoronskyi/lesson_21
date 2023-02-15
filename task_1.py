# Завдання 1. Написати клас для роботи з матрицями.
# Клас повинен створювати об’єкт матриць з вкладених списків,
# виводити матриці на друк, виконувати операції додавання, віднімання,
# множення на число, множення на матрицю, транспонування.
# Передбачити можливість приведення матриць для операцій додавання
# і віднімання.


print('--- Task 1 ---')


# Створюю клас для роботи з матрицями.
class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    # Метод для створення матриці.
    def get_matrix(self, n, m):
        num = 1
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    # Метод для читання матриці.
    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    # Метод для транспонування.
    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def get_transpose(self):
        return self.get_readable_matrix_string(self.transpose(self.matrix))

    # Метод для множення матриці на матрицю.
    def multiply(self, matrix):
        mtrx_mult = [[0 for j in range(len(matrix[i]))] for i in
                     range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    mtrx_mult[i][j] += self.matrix[i][k] * matrix[k][j]
        return mtrx_mult

    def get_multiply(self, matrix):
        return self.get_readable_matrix_string(self.multiply(matrix))

    # Метод для ділення матриці на матрицю.
    def divide(self, matrix):
            mtrx_div = [[0 for j in range(len(matrix[i]))] for i in
                        range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(matrix[0])):
                    for k in range(len(matrix)):
                        mtrx_div[i][j] += self.matrix[i][k] / matrix[k][j]
            return mtrx_div

    def get_divide(self, matrix):
        return self.get_readable_matrix_string(self.divide(matrix))

    # Метод для додавання матриць.
    def addition(self, matrix):
        try:
            mtrx_add = [[0 for j in range(len(matrix[i]))] for i in
                        range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(matrix[0])):
                    mtrx_add[i][j] += self.matrix[i][j] + matrix[i][j]
            return mtrx_add
        except Exception as err:
            print('Unexpected value', err)

    def get_addition(self, matrix):
        return self.get_readable_matrix_string(self.addition(matrix))

    # Метод для віднімання матриць.
    def subtracting(self, matrix):
        mtrx_sub = [[0 for j in range(len(matrix[i]))] for i in
                    range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                mtrx_sub[i][j] += self.matrix[i][j] - matrix[i][j]
        return mtrx_sub

    def get_subtracting(self, matrix):
        return self.get_readable_matrix_string(self.subtracting(matrix))

    # Метод для множення матриці на число.
    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string(
            [[num * other for num in row] for row in self.matrix])


if __name__ == '__main__':
    # Створюю матрицю 1.
    mtrx_1 = Matrix(5, 6)
    print('Matrix 1:')
    print(mtrx_1)

    # Транспонування матриці.
    print('\nTranspose matrix 1:')
    print(mtrx_1.get_transpose())

    # Створюю матрицю 2.
    mtrx_2 = Matrix(5, 6)
    print('\nMatrix 2:')
    print(mtrx_2)

    # Множення матриці на матрицю.
    print('\nMultiplication (mtrx_2 * mtrx_1):')
    print(mtrx_2.get_multiply(mtrx_1))

    # Ділення матриці на матрицю.
    print('\nDivide (mtrx_2 / mtrx_1):')
    print(mtrx_2.get_divide(mtrx_1))

    # Додаваня матриці 2 до матриц 1.
    print('\nAddition (mtrx_2 + mtrx_1):')
    print(mtrx_2.get_addition(mtrx_1))

    # Віднімання матриці 2 від матриці 1.
    print('\nSubtracting (mtrx_2 - mtrx_1):')
    print(mtrx_2.get_subtracting(mtrx_1))

    # Множення матриці на число.
    print('\nMatrix 1 multiplication by 3:')
    print(mtrx_1 * 3)
