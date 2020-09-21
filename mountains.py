def peak(heights, start, end):
    length = end - start
    if length == 0:
        return heights[start]
    elif length == 1:
        return max(heights[start], heights[end])
    
    # we have 3 or more elements, perform the mid comparison
    # grab the mid index by finding the midpoint between start and end
    mid_index = (start + end) // 2
    # grab the left index by finding the midpoint between the left and mid indices
    left_index = (start + mid_index) // 2
    # grab the right index by finding the midpoint between the mid and end indices
    right_index = (mid_index + end + 1) // 2

    mid = heights[mid_index]
    left = heights[left_index]
    right = heights[right_index]

    # if the left value is greater than the mid value, we are guarenteed to have a
    # peak somewhere on the left side of the mid index
    if left > mid:
        return peak(heights,start,mid_index)
    elif right > mid: # similar for right side
        return peak(heights,mid_index,end)
    # if we have a 3 element list where the mid is not less than the first or last
    # element, then we have a peak in the middle
    if length == 2:
        return heights[mid_index]
    # arbitrarily pick the right side to continue, there has to be a peak on the
    # right side since we cannot have consecutive values and the mid equals the right
    return peak(heights,mid_index,end)

def peak_runner(heights):
    return peak(heights, 0, len(heights)-1)

assert(peak_runner([1,2,3]) == 3)
assert(peak_runner([1,2,3,4,5]) == 5)
assert(peak_runner([1,2,3,2,5]) in [3,5])
assert(peak_runner([1,4,3,4,5]) in [4,5])
assert(peak_runner([1,2,3,4]) == 4)
assert(peak_runner([1,3,4,5,4,6,4,3,2,6,7,8]) in [5,6,8])
assert(peak_runner([6,5,4,3,2,1]) == 6)
assert(peak_runner([1,2,1,2,1]) == 2)
assert(peak_runner([1,2,3,2,1,4]) in [3,4])
assert(peak_runner([2,1,2]) == 2)
assert(peak_runner([1,2,1,2,1,2,1,2,1,2,1,2,1,2]) == 2)
assert(peak_runner([1,4,10,29,239,294,2,4,5,3,2894,392,393,291,3,2,6,3,1,6,9,0,6,4,3,8]) in [294,5,2984,393,6,9,8])