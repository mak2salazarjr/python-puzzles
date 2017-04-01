from collections import namedtuple

Point = namedtuple('Point', 'x y')
Triangle = namedtuple('Triangle', 'A B C')


def checkio(data):
    # decompose into triangles and compute with 3-point-area formula
    points = []
    for x_and_y in data:
        x, y = x_and_y
        points.append(Point(x, y))

    triangles = []
    p1 = points[0]
    for p2, p3 in zip(points[1:-1], points[2:]):
        triangles.append(Triangle(p1, p2, p3))

    total = 0
    for triangle in triangles:
        total += abs((triangle.A.x * (triangle.B.y - triangle.C.y) +
                      triangle.B.x * (triangle.C.y - triangle.A.y) +
                      triangle.C.x * (triangle.A.y - triangle.B.y)) / 2)
    return total


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return abs(checked - correct) < precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(
        checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
