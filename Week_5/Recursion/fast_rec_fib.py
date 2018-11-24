#recursive and fast implementation of fib using memoization

def fib(n, memo = {}):
	if n in memo:
		return memo[n]
	elif n == 1:
		return 1
	elif n == 0:
		return 0

	else:
		memo[n] = fib(n-1, memo) + fib(n-2, memo)
		return memo[n]


def main():
	n = 35
	for i in range(n+1):
		print(i, fib(i))


if __name__ == '__main__':
		main()