s=[1,4,5,2,3,2,6,8,0,0]
start=0
end=len(s)-1
count0=0
for i in range(len(s)):
    if s[i]%2==0:
        if s[start]==0:
            count0+=1
        s[start]=s[i]
        start+=1
    elif s[i]%2==1:
        if s[end]==0:
            count0+=1
        s[end]=s[i]
        end-=1
    print(s)
for i in range(len(s)):
	if i>=start and i<=end:
		s[i]=0
print(s)