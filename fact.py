def fact(num):
	if num==0:
		return 1
	else:
		return num*fact(num-1)
k=int(input("Enter the number:"))
m=fact(k)
print(m)