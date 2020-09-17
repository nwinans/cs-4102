from closest_pair import *
import time

"""
* This file is here to help you to verify that your algorithm is correct. You should not modify anything in this file.
* We have provided 7 tests for you. In here, we run all 7 test cases on both your D&C implementation as well as a quadratic impelmentation.
* If your algorithm is correct, you should see that both algorithms give the same answer, 
* but the D&C implementation will run faster for larger inputs. 
* The "big.txt" test ran approximately 10x longer for quadratic than for D&C on our machines.
* If the answers to the two problems are different (by more than floating-point error) then your algorithm does not produce the correct answer.
* If the running times are close for large inputs then your algorithm is not actually nlogn time.
* After you submit, we'll re-run your code on similar (but different) tests.
* If you get the correct answer, the running times seem reasonable, and you follow directions, then you can expect full marks on this assignment.
"""

tests = ["small.txt", "medium.txt", "vertical.txt", "horizontal.txt", "runway.txt", "exponential.txt", "big.txt"]

# Test case descriptions:
# small.txt: a small number of random points
# medium.txt: a medium number of random points
# vertical.txt: all points have the same x coordinate
# horizontal.txt: all points have the same y coordinate
# runway.txt: points near to each other in the x dimension, but distant in the y dimension
# exponential.txt: points are arranged in columns with exponentially-large gaps between columns
# big.txt: a large number of random points

def read_file(name):
    f = open(name)
    points = []
    for line in f:
        if len(line) == 0:
            break
        x,y = line.split()
        x = float(x)
        y = float(y)
        points.append((x,y))
    return points

def test_all():
    for test in tests:
        print("running", test)
        test_points = read_file(test)

        print("input size:", len(test_points))
        t_before = time.perf_counter()
        d = closest_pair(test_points)
        t_after = time.perf_counter()
        print("divide and conquer")
        print("distance:", d, "time:", t_after - t_before)
        t_before = time.perf_counter()
        d = quadratic_closest(test_points)[0]
        t_after = time.perf_counter()
        print("quadratic")
        print("distance:", d, "time:", t_after - t_before)
        print('\n')

test_all()

