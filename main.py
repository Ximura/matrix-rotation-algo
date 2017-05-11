from copy import deepcopy


class Dimension(object):
    def __init__(self, text: str):
        dimensions = [int(s) for s in text.split(' ')]
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.rotation = dimensions[2]

    def __str__(self):
        return "%i %i %i" % (self.rows, self.cols, self.rotation)


class Matrix(object):
    def __init__(self, text: str):
        self.matrix = [[int(num) for num in line.split(' ')] for line in text.splitlines()]

    def __str__(self):
        format = '\n'.join([row.__str__() for row in self.matrix])
        return format

    ''' 
     | <- ^
     v -> |
    '''
    def rotate(self, dimension: Dimension):
        new_matrix = deepcopy(self.matrix)

        new_matrix[:][0] = self.matrix[1:][0]

        circles = min(dimension.cols // 2, dimension.rows // 2)

        # move downwards
        for j in range(circles):
            for i in range(j, dimension.rows - 1 - j):
                    new_matrix[i+1][j] = self.matrix[i][j]

        # move upwards
        for j in range(circles):
            for i in range(j, dimension.rows - j - 1):
                    new_matrix[i][dimension.cols - j - 1] = self.matrix[i+1][dimension.cols - j - 1]

        # move leftwards
        for i in range(circles):
            for j in range(i, dimension.cols - i - 1):
                new_matrix[i][j] = self.matrix[i][j+1]

        # move rightwards
        for i in range(circles):
            for j in range(i, dimension.cols - i - 1):
                new_matrix[dimension.rows - i - 1][j+1] = self.matrix[dimension.rows - i - 1][j]

        self.matrix = new_matrix


def load_input(file_path: str) -> (str, str):
    input_file = open(file_path, 'r')
    dimensions = input_file.readline()
    matrix = input_file.read()
    return dimensions, matrix


def parse_input(file_path: str) -> (str, str):
    dimensions, matrix = load_input(file_path)
    return Dimension(dimensions), Matrix(matrix)


def main():
    filepath = "input"
    dimension, matrix = parse_input(filepath)
    print(dimension)
    print(matrix)

    for r in range(dimension.rotation):
        matrix.rotate(dimension)
        print("---------------")
        print(matrix)

if __name__ == '__main__':
    main()
