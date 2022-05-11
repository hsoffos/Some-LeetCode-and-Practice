

def mergesort(mylist):
    if len(mylist) > 1:  # Make sure the list can be split
        # Define midpoint, split list in half
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]

        # Recursively call the function
        mergesort(left)
        mergesort(right)

        # indexes for left and right
        i = 0  # left index
        j = 0  # right index

        # index for main list
        k = 0


        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1

        print(mylist)
        return mylist


thelist = [123, 897, 134, 58, 76, 193, 37, 2, 6, 9, 145, 154, 89]
mergesort(thelist)