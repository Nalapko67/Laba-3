def process_matrix_minimax():
    raw_m = input("Enter rows count m (<= 4) or press Enter for default (3): ").strip()
    raw_n = input("Enter cols count n (<= 6) or press Enter for default (4): ").strip()
    
    if not raw_m or not raw_n:
        b = [
            [12.5, 8.3, 15.1, 9.4],
            [14.2, 11.0, 7.8, 10.5],
            [5.6, 13.1, 16.0, 6.2]
        ]
        m = len(b)
        n = len(b[0])
    else:
        try:
            m = int(raw_m)
            n = int(raw_n)
            if m > 4 or n > 6 or m <= 0 or n <= 0:
                print("Error: Dimensions out of bounds (m<=4, n<=6).")
                return
            b = []
            print(f"Enter {m} rows with {n} numbers each:")
            for i in range(m):
                row = [float(x.replace(",", ".")) for x in input().split()]
                if len(row) != n:
                    print(f"Error: Row must contain exactly {n} elements.")
                    return
                b.append(row)
        except ValueError:
            print("Error: Invalid numerical data entered.")
            return

    row_minima = []
    for i in range(m):
        min_val = b[i][0]
        for j in range(1, n):
            if b[i][j] < min_val:
                min_val = b[i][j]
        row_minima.append(min_val)

    minimax_val = row_minima[0]
    for val in row_minima:
        if val > minimax_val:
            minimax_val = val

    print("Minima of each row:", row_minima)
    print("Minimax value:", minimax_val)

if __name__ == "__main__":
    process_matrix_minimax()