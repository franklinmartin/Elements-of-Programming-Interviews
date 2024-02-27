import math
from collections import namedtuple

from matplotlib import pyplot as plt

#fig = plt.figure(frameon=False)
#fig.set_size_inches(10, 10)
#ax = plt.Axes(fig, [0., 0., 1., 1.])
#ax.set_axis_off()
#fig.add_axes(ax)

rectangle = namedtuple("Rectangle", "x y width height")


#normalized coordinates
#x1 < width
#y1 < height
#x2 < width
#y2 < height
def intersect_rectangle(R1, R2):
    x = max(R1.x, R2.x)
    y = max(R1.y, R2.y)
    width = min(R1.width, R2.width)
    height = min(R1.height, R2.height)
    return rectangle(x, y, width, height)


point = namedtuple("Point", "x y")


# top right, top left, btm left, btm right


def construct_rectangle(P, A=0):
    P1 = P[0]
    P2 = P[1]
    P3 = P[2]
    P4 = P[3]

    def is_rectangle(P1, P2, P3, P4):
        c1 = P1.y == P2.y and P2.x == P3.x and P3.y == P4.y and P4.x == P1.x
        c2 = math.isclose(abs(P1.x - P2.x), abs(P4.x - P3.x)) and math.isclose(abs(P3.x - P2.x), abs(P4.x - P1.x))
        c3 = math.isclose(abs(P1.y - P2.y), abs(P4.y - P3.y)) and math.isclose(abs(P2.y - P3.y), abs(P1.y - P4.y))
        c2 = c2 and c3
        return c1 or c2

    if not is_rectangle(P1, P2, P3, P4):
        return rectangle(0, 0, -1, -1)
    return rectangle(P3.x, P3.y, abs(P1.x - P2.x), abs(P1.y - P4.y))


def deconstruct_rectangle(R1):
    P1 = point(R1.x + R1.width, R1.y + R1.height)
    P2 = point(R1.x, R1.y + R1.height)
    P3 = point(R1.x, R1.y)
    P4 = point(R1.x + R1.width, R1.y)
    return [P1, P2, P3, P4]


def move_rectangle(R1, x, y):
    return rectangle(x, y, R1.width, R1.height)


def rotate_point(P, A=0):
    return point(
        P.x * math.cos(A) - P.y * math.sin(A), P.x * math.sin(A) + P.y * math.cos(A)
    )


def rotate_rectangle(R1, A=0):
    points = deconstruct_rectangle(R1)
    for i in range(0, len(R1)):
        points[i] = rotate_point(points[i], A)
    return points


# x1 < x2   y1 < y2
r1 = rectangle(1, 2, 4, 2)
r2 = rectangle(1, 1, 1, 1)
print(intersect_rectangle(r1, r2))
#a = math.radians(45)



""" 
x = []
y = []


temp = rectangle(0, 0, -1, -1)
for j in range(0, 4):
    example_rectangle = rectangle(j, j, j, j)

    example_points = rotate_rectangle(example_rectangle, 90)
    result = intersect_rectangle(temp, construct_rectangle(example_points))
    temp = example_rectangle
    print(result)
    x = []
    y = []

    for i in range(0, len(example_points)):
        x.append(example_points[i].x)
        y.append(example_points[i].y)
    x.append(example_points[0].x)
    y.append(example_points[0].y)
    plt.plot(x, y)

plt.show()
 """