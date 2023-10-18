'''
  Writing a sorting algorithm that can handle any data type 
  Then test the algorithm with test cases
    - sort numbers ascending by numerical value,
    - sort people alphabetically (lexicographically) by name, 
    and to
    - sort people descending by age, where people of the same 
    age should be sorted alphabetically (lexicographically).
'''


def merge(arr, l_idx, m_idx, r_idx):
    """
    Doing the merging of the two subarrays in the mergesort algorithm
    :param arr: The array that is being sorted
    :param l_idx: The left index of the array
    :param m_idx: The middle index of the array
    :param r_idx: The right index of the array
    """

    # Calculating the sizes of the left and right subarrays
    l_arr_size = m_idx - l_idx + 1
    r_arr_size = r_idx - m_idx

    # Creating two temporary subarrays
    LEFT_ARRAY = [0] * (l_arr_size)
    RIGHT_ARRAY = [0] * (r_arr_size)

    # Copying elements from actual array to the left & right subarrays
    for elmnt in range(0, l_arr_size):
        LEFT_ARRAY[elmnt] = arr[l_idx + elmnt]

    for elmnt in range(0, r_arr_size):
        RIGHT_ARRAY[elmnt] = arr[m_idx + 1 + elmnt]

    # Index pointers to the left and right subarrays
    l_ptr = r_ptr = 0
    # Index pointer to the merged subarray
    m_ptr = l_idx

    # Running a loop until pointers reach the end of the subarrays
    while l_ptr < l_arr_size and r_ptr < r_arr_size:
        # Comparing the first element of the left subarray with
        # the first element of the right subarray
        if LEFT_ARRAY[l_ptr] <= RIGHT_ARRAY[r_ptr]:
            arr[m_ptr] = LEFT_ARRAY[l_ptr]
            l_ptr += 1  # Incrementing the left subarray index pointer
        else:
            arr[m_ptr] = RIGHT_ARRAY[r_ptr]
            r_ptr += 1  # Incrementing the right subarray index pointer
        m_ptr += 1  # Incrementing merged subarray index pointer

    # Copying the remaining elements of the left subarray
    # and incrementing the index pointers
    while l_ptr < l_arr_size:
        arr[m_ptr] = LEFT_ARRAY[l_ptr]
        l_ptr += 1
        m_ptr += 1

    # Copying the remaining elements of the right subarray
    # and incrementing the index pointers
    while r_ptr < r_arr_size:
        arr[m_ptr] = RIGHT_ARRAY[r_ptr]
        r_ptr += 1
        m_ptr += 1


def merge_sort(arr, left, right):
    """
    Function to break the main array into subarrays and call the merge function
    to recursively sort and merge the subarrays
    :param arr: The array that is being sorted
    :param left: The left index of the array
    :param right: The right index of the array

    :return arr: Returning the sorted array
    """
    # Checking if the left index is less than the right index
    if left < right:
        # Calculating the mid value
        mid = (left + (right - 1)) // 2
        # Applying the merge_sort function recursively
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        # Calling the merge function to merge the sorted subarrays
        merge(arr, left, mid, right)

    # Returning the sorted array
    return arr


# Running the main function to call functions and apply test cases on them
if __name__ == "__main__":
    # Checking to sort numbers
    test1 = [645, 37, 76, 5, -34, 1,
             0, 23, 635, -876, 467, 62]
    print("Original sequence: ", test1)
    sorted_seq1 = merge_sort(test1, 0, len(test1) - 1)
    print("Sorted sequence: ", sorted_seq1)

    # Checking to sort decimals
    test2 = [645.41, 37.59, 76.41, 5.31, -34.23, 1.11,
             1.10, 23.46, 635.47, -876.32, 467.83, 62.25]
    print("\nOriginal sequence: ", test2)
    sorted_seq2 = merge_sort(test2, 0, len(test2) - 1)
    print("Sorted sequence: ", sorted_seq2)

    # Checking to sort strings
    test3 = ["Hal", "Susann", "Dwight", "Kassandra", "Lawrence", "Cindy", "Cory", "Mac",
             "Romana", "Doretha", "Danna", "Zara", "Rosalyn", "Risa", "Benny", "Juan", "Natalie"]
    print("\nOriginal sequence: ", test3)
    sorted_seq3 = merge_sort(test3, 0, len(test3) - 1)
    print("Sorted sequence: ", sorted_seq3)
