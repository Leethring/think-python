# Find the index of unsorted number, if the list 
# is sorted, print sorted

unsorted_index = None
my_list = [-1, 0, 3, 6]

# Loop the list to find index, to compare current number and previous number
for index, current_num in enumerate(my_list):
    # If the index is 0, we can't compare
    if index == 0:
        previous_num = current_num
    elif previous_num > current_num:
        unsorted_index = index 
        print(unsorted_index)
        break
    else:
        # The current number change to the next number.
        previous_num = current_num
else:
    print('sorted')