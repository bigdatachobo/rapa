S = input()
diff = 0
for i in range(1,len(S)):
    if S[i-1] != S[i]:
        diff += 1
print((diff + 1)//2)        