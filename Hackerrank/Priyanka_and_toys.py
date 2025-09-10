def toys(w):
    w.sort()  
    if not w:  
        return 0
    containers = 1
    current_max_weight = w[0] + 4  
    for i in range(1, len(w)):
        if w[i] > current_max_weight:
            containers += 1
            current_max_weight = w[i] + 4
    return containers
if __name__ == '__main__':
    # Example usage (as per HackerRank input format)
    n = int(input())  # Number of toys
    weights = list(map(int, input().split())) 
    result = toys(weights)
    print(result)
