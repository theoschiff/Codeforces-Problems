import sys
import math
#input = sys.stdin.readline
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
n, m, f = map(int, input().split())
 
l = []
 
for i in range(m):
    a, b, c, d = list(map(int, input().split()))
    l.append((a, b, c, d))
if (len(l) == 0):
    a, b, c, d = [0,0,0,0]
else:
    a, b, c, d = zip(*l)
 
# n is the number of posts, m is number of hh, f is the fuel in liters
# a is the start position of a hitchhiker, b is end position of a hh, c is number of cans hh has
# d is fuel hh has 
def max_dog_food(n, m, f, a, b, c, d):
    #pour set la limite de recursion
    if (m == 0 and f < n-1):
        return -1
    
    dp = [[-1] * (n+1) for i in range(n+1)]
    #Base case : 
    #if enough fuel to reach gas town without taking any hh no matter how high the fuel is 
    if (f>=n):
        dp[n][n] = 0
    
    return memoized_dog_food(m, f, a, b, c, d, 1, dp)
    

#only need number of hh, remaining fuel, start and end positions and curr_post
def memoized_dog_food(m, r_fuel, a, b, c, d, curr_post, dp):
    sys.setrecursionlimit(4000)
    #upperbound fuel to n - post

    if r_fuel > n - curr_post:
        r_fuel = n - curr_post
    
    if (curr_post == n):
        return 0
    #if value already calculated
    if (dp[curr_post][r_fuel] != -1):
        return dp[curr_post][r_fuel]
    tmp_food = -1
    tmp_food2 = -1
    for k in range(m):
        food_best_hh =-1
        if a[k] == curr_post and ((r_fuel + d[k]) >= (b[k] - a[k])):
            if (d[k] > n - curr_post):
                food_best_hh  = c[k] + memoized_dog_food(m, r_fuel + n - curr_post - (b[k] - a[k]), a, b, c, d, curr_post + (b[k] - a[k]), dp)
            else :
                food_best_hh  = c[k] + memoized_dog_food(m, r_fuel + d[k] - (b[k] - a[k]), a, b, c, d, curr_post + (b[k] - a[k]), dp)
            if (food_best_hh  > tmp_food):
                tmp_food = food_best_hh 
        
    if (r_fuel >= 1): 
        tmp_food2 = memoized_dog_food(m, r_fuel - 1, a, b, c, d, curr_post + 1, dp)

    
        
    #cannot do anything, couldn't pick up a hh nor go further 
    if(tmp_food == -1 and r_fuel == 0):
        dp[curr_post][r_fuel] = -math.inf

    if (tmp_food2 == -math.inf and tmp_food == -1):
        return -math.inf

    if r_fuel >= 1:
        dp[curr_post][r_fuel] = max(tmp_food, tmp_food2)
        return max(tmp_food, tmp_food2)
    else:
        if (dp[curr_post][r_fuel] != -math.inf):
            dp[curr_post][r_fuel] = tmp_food
            return tmp_food
        else:
            return -math.inf

    

max_food = max_dog_food(n, m, f, a, b, c, d)

if (max_food < 0):
    print("Impossible")
else:
    #print(max_food)
    sys.stdout.write(str(max_food) + "\n")
