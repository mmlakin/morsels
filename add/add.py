def add(*lists):
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*lists)
    ]

"""
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
matrix3 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix4 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
matrix5 = [[1, 0], [2, 1]]
"""
