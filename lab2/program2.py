def dig(n):
if n == 0:
return 0
elif n == 1:
return 1
else:

S=n%10
return (s+dig(n//10))
n=int(input("number:"))
result = dig(n)
print(result)
