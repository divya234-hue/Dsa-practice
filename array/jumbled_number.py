n = input("enter a number")
ans = True
for i in range(len(n)-1):
    if abs(int(n[i])-int(n[i+1]))>1:
        ans = False
if ans :
    print("jumbled")
else:
    print("no jumbled")
