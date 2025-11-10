def compliant_function(first_arg, second_arg, third_arg):
    # This line respects the 80 character limit
    result = 0

    # Only two levels of nesting
    for i in range(10):
        if i > 5:
            result += i

    # Less than 10 statements
    print("Processing data...")
    result += first_arg
    result += second_arg
    result += third_arg

    return result