H, W = map(int, input().split())
arr = list(map(int, input().split()))

        
def check_pillar(arr, W):
    pillar = [False] * W
    
    max_height = 1
    for i in range(W):
        h = arr[i]
        if max_height <= h:
            max_height = h
            pillar[i] = True
    
    max_height = 1
    for i in reversed(range(W)):
        h = arr[i]
        if max_height <= h:
            max_height = h
            pillar[i] = True
    
    return [(i, arr[i]) for i in range(W) if pillar[i] is True]


pillar_arr = check_pillar(arr, W)
result = 0

for i in range(1, len(pillar_arr)):
    start_idx, start_height = pillar_arr[i - 1]
    end_idx, end_height = pillar_arr[i]
    
    min_height = min(start_height, end_height)
    for j in range(start_idx + 1, end_idx):
        result += min_height - arr[j]

print(result)
