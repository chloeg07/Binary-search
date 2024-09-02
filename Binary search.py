#Make a python code for a Binary search using the simpliest form possible.
#NOTE: The list must be sorted before you can do a binary search.
#1. Set low = 0. 2. Set high = length of list - 1. 3. Set mid = low + high/2, rounded down to an integer. 4. If the value at the mid position is the same as the target value, return mid. Else if the value at the mid position is less than tHe target value, Set low = mid + 1. Else if the value at the mid position is greater than the target value, Set high = mid - 1. 5. As long as low doesnt 'cross over' high, go back to step 3 above.  

def binary_search(arr, target):
    #Step 1: Set low = 0
    low = 0
    
    #Step 2: Set high = length of list - 1
    high = len(arr) - 1
    
    
    #Step 5: Loop until low crosses over high
    while low <= high:
       
       #Step 3: Set mid = low + (high - low) // 2
        mid = (low + high) // 2
        
       
       #Step 4: Check if the value at mid is the target value
        if arr[mid] == target:
            return mid
        #Target value found, return the index
        elif arr[mid] < target:
            low = mid + 1
            #Ignore left half
        else:
            high = mid - 1
            #Ignore right half
            
    #If we exit loop, it means the target is not in the list.
    return -1

if __name__ == "__main__":
     #Get user input for the sorted list of numbers and the target value
    
    arr = list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split()))
    target = int(input("Enter the target value: "))
    #Perform binary search
    result = binary_search(arr, target)
    
    #Output result
    if result != -1:
        print(f"Target value {target} found at index {result}.")
    else:
        print(f"Target value {target} not found in the list.")
    
    
    
    
    
    
    
    
    
  


        
        
        
        
        