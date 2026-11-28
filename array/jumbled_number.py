n = input("enter no:").strip()
for i in range(len(n)-1):
    if abs(int(n[i])-int(n[i+1]))>1:
        print("not jumbled")
        break
else:
    print("jumbled")