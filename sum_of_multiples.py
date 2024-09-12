def sum_of_multiples(limit, multiples):
    mult = set()  # Use a set to avoid duplicates

    for num in multiples:
        if num == 0:  # Skip zero to avoid infinite loop
            continue
        result = num
        while result < limit:
            mult.add(result)  # Add multiples of num less than limit
            result += num

    return sum(mult)  # Sum of unique multiples
