N = int(input()) #(3<=N<=100)
warehouse = list(map(int, input().split()))

food_list = [0]*N

food_list[0] = warehouse[0]
food_list[1] = warehouse[1]
food_list[2] = warehouse[2] + warehouse[0]

#1 8 9 1 4 5 6 --> 20
for i in range(3, N):
    food_list[i] = max(warehouse[i] + food_list[i-2], warehouse[i] + food_list[i-3])

print(food_list)
print(food_list[N-1])
