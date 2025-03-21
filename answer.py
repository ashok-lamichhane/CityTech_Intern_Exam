def count_inversions(arr):
    inversion_count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversion_count += 1 
    
    return inversion_count


if __name__ == "__main__":
    arr = [8, 4, 2, 1]
    
    total_inversions = count_inversions(arr)
    
    print(f"Total inversions in the array: {total_inversions}")
