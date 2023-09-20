# The task is simple. Through some critical points in 2D, you have to draw a wave like curve. Your goal is to include as many points as possible.

# - There will be an imaginary line y = a, which we call the major axis for the curve.
# - All the points on the curve should have different x coordinates. Their y coordinates should be of form a-1 or a+1.

# Two consecutive points on the curve should have a difference of 2 in their y coordinate.


# Input:

# There will be no more than 222 test cases. Each test case starts with an integer N, the number of points in the test case. In the next N lines, there will be N pair of integers giving the x and y coordinate of the points. There will be no more than 1000 points in each test case. All coordinates are integers -- they'd fit in a signed 2 byte integer data type. The data must be read of default input.


# Output:

# For each test case print a number -- the maximum number of critical points that can be included in a curve drawn from the given points.


# Input Sample:

# 10
# 0 1
# 1 0
# 1 -1
# 2 -2
# 3 1
# 3 -1
# 3 -2
# 4 1
# 4 -1
# 5 -1
# 10
# 0 2
# 2 0
# 1 -1
# 2 -2
# 3 1
# 3 -1
# 3 -2
# 4 1
# 4 -1
# 5 –1


# Output Sample:

# 4
# 3


# Status: (Runtime error)

for i in range(222):
    count = 0
    ncoords = int(input())
    xs = []
    ys = []

    for _ in range(ncoords):
        x, y = map(int, input().split())
        if y == 1 or y == -1:
            xs.append(x)
            ys.append(y)

    xs.sort()

    index = 0
    for x in xs:
        if index == 0:
            count += 1
        else:
            if x - 2 == xs[index - 1]:
                count += 1
        index += 1

    print(count)
