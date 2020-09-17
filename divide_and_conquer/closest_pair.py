"""
* Implement the "dc_closest" function below to match the closest pair of points algorithm discussed in class.
* Your algorithm must be divide an conquer, with the base case, divide, conquer, and combine steps clearly marked.
* Your implementation must have nlogn running time.
* There is an accompanying file provided to help you verify correctness and running time of your implementation.
* You may submit only this file. Do not leave any lingering print statements in any methods.
* Do not import any additional packages.
"""

def distance(p1, p2):
    # a function to compute the distance between two points
    # Do not modify this function
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

    
def quadratic_closest(points):
    # A quadratic procedure for finding closest pair of points. Use this for timing comparison.
    # This can also serve as your base case if you'd like
    # It returns a pair of values: the distance of the closest pair and the list of points re-sorted by y.
    # Do not modify this function
    closest = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if closest > dist:
                closest = dist
    return closest, sorted(points, key=lambda point: point[1])


def get_runway(ysorted_points, medianx, delta):
    # A procedure to extract all points in the runway
    # I found this function to be useful, but you're not required to implement and use it if you don't want to
    runway = []
    return runway
    
    
def merge(left, right):
    # A procedure to merge the points by y value
    # You'll almost certainly need to use this one, but it's ok if you don't use it.
    merged = []
    return merged


def dc_closest(xsorted_points):
    #The divide and conquer closest pair of points algorithm
    # The input is a list of points sorted by x value
    # The output is a pair comprised of the closest pair of points from among the given points, and the given points re-sorted by y
    # Your assignment is to implement this function. It's required that your algorithm runs in nlogn time, and that it follow the divide and conquer format.
    
    #BASE CASE
    # You'll need to have a base case. I've provided one, but you may change it if you prefer something else
    # We will not run your code on any test cases with fewer than 2 points.
    if len(xsorted_points) < 2:
        return quadratic_closest(xsorted_points)
        
    #DIVIDE STEP
    # For the divide step, split the list of points into two sub-lists of length n/2
    # Save the median x coordinate, you'll need that later for COMBINE
    
    #CONQUER STEP
    # For this step, recursively solve closest pair of points on the two halves
    # You'll need both the distance returned as well as the points sorted by y value
    
    #COMBINE STEP
    # For this step, you'll need to merge points by y value, identify the points in the "runway", and find the closest pair which crosses the divide
    
    #RETURN VALUE
    # The return value will be the distance of the closest pair found and all points sorted by y value
    delta = 0
    y_sorted = []
    return delta, y_sorted

    
def closest_pair(points):
    # Helper function to hide the recursion since the recursive function needs a second return value
    # All this does is sort the points by x, invoke the D&C algorithm, and return only the distance
    points = sorted(points)
    dist, points = dc_closest(points)
    return dist
    
def main():
    points = [(1.0, 2.1), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (6.0, 5.0), (5.0, 6.0)]
    print(closest_pair(points)) # example invocation of D&C algorithm
    print(quadratic_closest(points)[0]) # example invocation of quadratic algorithm
    
if __name__ == '__main__':
    main()

