
#################
# BINARY SEARCH #
#################

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

####################
# HEAPQ - MIN HEAP #
####################
heap = []
    
# push
heapq.heappush(heap, k)
heapq.heappush(heap, (k, v))

# pop
heapq.heappop(heap)

# max heap
heapq.heappush(heap, -1*k)


#######
# SET #
#######
my_set = {1, 2, 3}

# add an element
my_set.add(2)

# remove an element
my_set.remove(3)



