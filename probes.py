T = int(input())
for t in range(T):
    N = int(input())
    A = input()
    arr = []
    for a in str(A):
        arr.append(int(a))
    
    cl = N//2 + N%2
    ans = 0
    count, l, c = 0, 0, 0
    for x in arr:
        if c == cl:
            count += x
            count -= arr[l]
            l += 1
        else:
            count += x
            c += 1
        
        ans = max(count, ans)
    
    print('Case #{}: {}'.format(t+1,ans))