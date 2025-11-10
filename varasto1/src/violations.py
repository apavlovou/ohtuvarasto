def violating_rules_example(first_arg, second_arg, third_arg, fourth_arg):
    # Violates max-args rule by having more than 3 arguments
    # This line is intentionally very long to violate the max-line-length rule of 80 characters..............................
    result = 0
    
    # Violates max-nested-blocks rule by having more than 2 nested blocks
    for i in range(10):
        if i > 5:
            for j in range(5):
                if j > 2:
                    result += 1
    
    # Violates max-statements rule by having more than 10 statements
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")
    print("Statement 4")
    print("Statement 5")
    print("Statement 6")
    print("Statement 7")
    print("Statement 8")
    print("Statement 9")
    print("Statement 10")
    print("Statement 11")  # This makes it exceed the limit
    
    return result