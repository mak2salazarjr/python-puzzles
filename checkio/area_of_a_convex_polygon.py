"""
    Problem statement:
        https://py.checkio.org/mission/area-of-a-convex-polygon/
"""


def polygon_area(data):
    """
    Reference: http://www.mathopenref.com/coordpolygonarea2.html
        Note this works with concave (simple) polygons as well
    :param data: list of polygon vertices
    :return: area
    """
    data.append(data[0])
    return abs(sum([(x1 + x2) * (y2 - y1) for (x1, y1), (x2, y2) in zip(data, data[1:])])) / 2


checkio = polygon_area

if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return abs(checked - correct) < precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(
        checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(
        checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
