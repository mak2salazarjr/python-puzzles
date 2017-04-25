"""
Input: List of all rectangles heights in histogram
Output: Area of the biggest rectangle
Example:
largest_histogram([5]) == 5
largest_histogram([5, 3]) == 6
largest_histogram([1, 1, 4, 1]) == 4
largest_histogram([1, 1, 3, 1]) == 4
largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
How it is used: There is no way the solution you come up with will be any useful in a real life.
Just have some fun here.
Precondition:
0 < len(data) < 1000
"""


def largest_histogram(histogram):
    maximum = 0
    for width in range(1, len(histogram)+1):
        for start in range(len(histogram)+1-width):
            chunk = histogram[start:start+width]
            minimum_value_in_chunk = min(chunk)
            area = width * minimum_value_in_chunk
            if area > maximum:
                maximum = area
    return maximum

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
