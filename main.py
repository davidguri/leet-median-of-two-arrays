
nums1 = [1, 2, 3]
nums2 = [4, 6, 5, 7]

merged_array = nums1 + nums2
merged_array.sort()

length_of_merge = len(merged_array)

if (length_of_merge % 2) == 0:
    mid_array1 = int(length_of_merge / 2)
    mid_array2 = int(mid_array1 + 1)
    median = ((mid_array1 + mid_array2) / 2)
    print("Median of two arrays: " + str(median))
else:
    mid_array = int(length_of_merge / 2)
    median = merged_array[mid_array]
    print("Median of two arrays: " + str(merged_array[mid_array]))



