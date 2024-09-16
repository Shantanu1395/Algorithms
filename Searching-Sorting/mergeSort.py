class MergeSortSwaps:
    def __init__(self):
        self.swaps = 0  # To keep track of the total number of swaps

    def merge(self, arr, index, l, m, r):
        # Create left and right subarrays from the current segment of the main array
        left = arr[l:m+1]
        right = arr[m+1:r+1]

        # Track the original indices of the elements in left and right subarrays
        left_index = index[l:m+1]
        right_index = index[m+1:r+1]

        i, j, k = 0, 0, l  # Initialize pointers for left, right, and the merged array

        # Merge the two halves while counting the necessary swaps
        while i < len(left) and j < len(right):
            # If an element in the right subarray is smaller, it needs to be swapped
            if right[j] < left[i]:
                arr[k] = right[j]
                index[k] = right_index[j]  # Update index tracking for sorted positions
                self.swaps += len(left) - i  # Count swaps: all remaining left elements are "moved" past this point
                j += 1
            else:
                arr[k] = left[i]
                index[k] = left_index[i]  # Update index tracking for sorted positions
                i += 1
            k += 1

        # Copy any remaining elements from the left subarray, if any
        while i < len(left):
            arr[k] = left[i]
            index[k] = left_index[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right subarray, if any
        while j < len(right):
            arr[k] = right[j]
            index[k] = right_index[j]
            j += 1
            k += 1

    def merge_sort_and_count_swaps(self, arr, index, l, r):
        if l < r:
            # Find the middle point to divide the array into two halves
            mid = (l + (r - 1)) // 2

            # Recursively sort the first and second halves, accumulating swaps
            self.merge_sort_and_count_swaps(arr, index, l, mid)
            self.merge_sort_and_count_swaps(arr, index, mid + 1, r)

            # Merge the sorted halves and count the swaps during merging
            self.merge(arr, index, l, mid, r)

    def get_minimum_swaps(self, arr):
        self.swaps = 0  # Reset the swap count before starting
        index = list(range(len(arr)))  # Create an index array to track original positions
        self.merge_sort_and_count_swaps(arr, index, 0, len(arr) - 1)
        return self.swaps


# Example usage with test cases
test_cases = [
    [45, 43, 25, 64, 22, 63, 7, 76, 65, 43, 24, 27, 82, 0],  # Mixed values
    [7, 3, 2, 1, 5, 4, 6],                                  # Random small array
    [1, 5, 3, 2, 4, 6, 7],                                  # Nearly sorted
    [4, 3, 2, 1],                                           # Reversed
    [1, 2, 3, 4, 5],                                        # Already sorted
    [10, 20, 30, 40, 50],                                   # Already sorted larger steps
    [50, 40, 30, 20, 10],                                   # Fully reversed
    [3, 3, 2, 1, 2, 3, 4],                                  # Contains duplicates
    [1],                                                    # Single element
    []                                                      # Empty array
]

results = []

# Create an instance of the MergeSortSwaps class
merge_sort_swaps = MergeSortSwaps()

for arr in test_cases:
    # Copy the array to preserve the original for verification
    original_arr = arr[:]
    swaps = merge_sort_swaps.get_minimum_swaps(arr)  # Get the minimum swaps for sorting
    results.append((original_arr, arr, swaps))

# Display the results in a DataFrame format
import pandas as pd
results_df = pd.DataFrame(results, columns=["Original Array", "Sorted Array", "Minimum Swaps"])
results_df
