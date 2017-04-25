"""
Input: Coordinates as a string..
Output: The equation of the circle as a string.
Precondition: All three given points do not lie on one line.
0 < xi, yi, r < 10
"""


from collections import namedtuple
from math import sqrt
from ast import literal_eval

Point = namedtuple('Point', 'x y')


def precision(value):
    if round(value, 0) == round(value, 1) == round(value, 2):
        return 0
    elif round(value, 1) == round(value, 2):
        return 1
    else:
        return 2


def checkio(data):
    data = literal_eval(data)
    point_1 = Point(*data[0])
    point_2 = Point(*data[1])
    point_3 = Point(*data[2])

    try:
        slope_a = (point_2.y - point_1.y) / (point_2.x - point_1.x)
        slope_b = (point_3.y - point_2.y) / (point_3.x - point_2.x)
    except ZeroDivisionError:
        point_2, point_3, point_1 = point_1, point_2, point_3
        try:
            slope_a = (point_2.y - point_1.y) / (point_2.x - point_1.x)
            slope_b = (point_3.y - point_2.y) / (point_3.x - point_2.x)
        except ZeroDivisionError:
            point_2, point_3, point_1 = point_1, point_2, point_3
            slope_a = (point_2.y - point_1.y) / (point_2.x - point_1.x)
            slope_b = (point_3.y - point_2.y) / (point_3.x - point_2.x)

    center_x = (slope_a * slope_b * (point_1.y - point_3.y) +
                slope_b * (point_1.x + point_2.x) -
                slope_a * (point_2.x + point_3.x)) / (2 * (slope_b - slope_a))

    if slope_a:
        center_y = -1 * (center_x - (point_1.x + point_2.x) / 2) / slope_a + (point_1.y +
                                                                              point_2.y) / 2
    else:
        center_y = -1 * (center_x - (point_2.x + point_3.x) / 2) / slope_b + (point_2.y +
                                                                              point_3.y) / 2

    radius = sqrt((center_x - point_1.x) ** 2 + (center_y - point_1.y) ** 2)

    x_precision = precision(center_x)
    y_precision = precision(center_y)
    radius_precision = precision(radius)

    # replace this for solution
    s = '(x-{0:.{1}f})^2+(y-{2:.{3}f})^2={4:.{5}f}^2'.format(center_x, x_precision,
                                                             center_y, y_precision,
                                                             radius, radius_precision)
    return s


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
