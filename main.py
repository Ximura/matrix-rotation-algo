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
        for i in range(dimension.rows):
            for j in range(dimension.cols):
                if j > i and j > 0:  # moving leftward
                    new_matrix[i][j-1] = self.matrix[i][j]
                elif j <= i < dimension.rows - 1:  # moving downward
                    new_matrix[i+1][j] = self.matrix[i][j]
                elif 0 < i <= j:  # moving upward
                    new_matrix[i-1][j] = self.matrix[i][j]

        self.matrix = new_matrix


def load_input(file_path: str) -> (str, str):
    input_file = open(file_path, 'r')
    dimensions = input_file.readline()
    matrix = input_file.read()
    return dimensions, matrix


def parse_input(file_path: str) -> (str, str):
    dimensions, matrix = load_input(file_path)
    return Dimension(dimensions), Matrix(matrix)


if __name__ == '__main__':
    filepath = "input-1"
    dimension, matrix = parse_input(filepath)
    print(dimension)
    print(matrix)

    matrix.rotate(dimension)
    print("---------------")
    print(matrix)
