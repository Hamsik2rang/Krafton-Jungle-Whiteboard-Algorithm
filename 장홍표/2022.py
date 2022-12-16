x, y, c = map(float, input().split())
high = min(x,y)
low = 1
ans = 0
while low+0.001 <= high:
    w = (low+high)/2
    #w를 이용해서 c계산해봄
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5
    guess_c = (h1*h2)/(h1+h2)
    if guess_c >= c:
        ans = w
        low = w
    else:
        high = w
print(ans)
