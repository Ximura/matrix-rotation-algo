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

    def rotate(self, dimension: Dimension):

        pass


def load_input(file_path: str) -> (str, str):
    input_file = open(file_path, 'r')
    dimensions = input_file.readline()
    matrix = input_file.read()
    return dimensions, matrix


def parse_input(file_path: str) -> (str, str):
    dimensions, matrix = load_input(file_path)
    return Dimension(dimensions), Matrix(matrix)


if __name__ == '__main__':
    filepath = "input"
    dimension, matrix = parse_input(filepath)
    print(dimension)
    print(matrix)
