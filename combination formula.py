import math
num_of_items_in_group = int(input("enter the number of items in the group "))
num_of_items_that_are_selected = int(input("enter the number of items that are being selected "))
if num_of_items_in_group < num_of_items_that_are_selected:
    print("there is an error in the given data there is no factorial function for values below zero")
    exit(1)
fac_num_of_items=math.factorial(num_of_items_in_group)
fac_num_of_item_selected=math.factorial(num_of_items_that_are_selected)
difference_fac=math.factorial(num_of_items_in_group-num_of_items_that_are_selected)
answer=fac_num_of_items/(fac_num_of_item_selected*(difference_fac))
print(f"in a group of {num_of_items_in_group} there are/is  {int(answer)} number "
      f"of ways/way to select { num_of_items_that_are_selected } items")
