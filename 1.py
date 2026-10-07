def process_culinary_array():
    raw_input = input("Enter array elements (or press Enter to use default C array): ")
    if raw_input.strip():
        c = [float(x) for x in raw_input.split()]
    else:
        c = [2.1, 3.6, -6.3, 4.1, 2.2, -2.3]
    
    positive_count = 0
    negative_count = 0
    total_count = len(c)
    
    for value in c:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
            
    print("Total elements:", total_count)
    print("Positive elements count:", positive_count)
    print("Negative elements count:", negative_count)

if __name__ == "__main__":
    process_culinary_array()