

count = 0
memo = {}
def fib(n):
	global count
	if n in memo:
		return memo[n]
	print(f'Calculating: {n}')
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else: 
		memo[n] = fib(n-1) + fib(n-2)
		count = count + 1
		return memo[n]

answer = fib(10)
print(f"Answer: {answer}")
print(f"Number of iterations {count}")