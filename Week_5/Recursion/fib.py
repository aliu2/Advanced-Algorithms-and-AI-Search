#recursive fibonacci is very slow for large numbers

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	else:
		return fib(n-1) + fib(n-2)


def main():
	n = 35
	for i in range(n+1):
		print(i, fib(i))


if __name__ == '__main__':
	main()