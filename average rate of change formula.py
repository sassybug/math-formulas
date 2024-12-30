the_multiply_part_of_the_function = int(input("enter what we are multiplying by "))
the_addition_part_of_the_function = int(input("enter what we are adding by "))
interval_1 = float(input("enter the first interval "))
interval_2 = float(input("enter the second interval "))
interval_2_gone_trough_function = (interval_2*the_multiply_part_of_the_function)+the_addition_part_of_the_function
interval_1_gone_trough_function = (interval_1*the_multiply_part_of_the_function)+the_addition_part_of_the_function
answer = (interval_2_gone_trough_function-interval_1_gone_trough_function)/(interval_2-interval_1)
print(f"the answer is {answer}")
