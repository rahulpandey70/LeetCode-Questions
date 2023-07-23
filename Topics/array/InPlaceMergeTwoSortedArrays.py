"""
    Given two sorted arrays, X[] and Y[] of size m and n each, merge elements of X[] with elements of array Y[] by maintaining the sorted order, i.e., fill X[] with the first m smallest elements and fill Y[] with remaining elements.

    Example:-
    
    Input:
 
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]
    
    Output:
    
    X = [1, 2, 3, 4, 7]
    Y = [8, 9, 10]
    
    Consider each array element X[] and ignore it if it is already in the correct order (i.e., the element smallest among all remaining elements); otherwise, swap it with the smallest element, which happens to be the first element of Y[]. After swapping, move the element (now present at Y[0]) to its correct position in Y[] to maintain the sorted order.

"""

def mergeTwoSortedArray(x, y):
    
    lenX = len(x)
    lenY = len(y)
    
    for i in range(lenX):
        
        # compare the current element of x[] with the first element of y[]
        if x[i] > y[0]:
            
            # swap x[i] with y[0]
            temp = x[i]
            x[i] = y[0]
            y[0] = temp
            
            first = y[0]
            
            # move y[0] to its correct position to maintain the sorted order of y[]
            k = 1
            while k < lenY and y[k] < first:
                y[k - 1] = y[k]
                k = k + 1
            
            y[k - 1] = first

if __name__ == "__main__":
    
    x = [1, 4, 7, 8, 10]
    y = [2, 3, 9]
    
    mergeTwoSortedArray(x, y)
    print("x", x)
    print("y", y)

