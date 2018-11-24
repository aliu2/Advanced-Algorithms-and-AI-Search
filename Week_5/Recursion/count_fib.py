#recursive fibonacci is very slow for large numbers

# def fib_count(n, count):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1

# 	else:
# 		if n == 2:
# 			count = count + 1
# 			print(count)
# 		return fib_count(n-1, count) + fib_count(n-2, count)

def fib(n):
	global count
	if n == 0:
		return 0
	elif n == 1:
		return 1

	else:
		if n == 5:
			count += 1
		return fib(n-1) + fib(n-2)


def main():
	n = 20
	global count
	count = 0
	i = fib(n)
	print(count)


if __name__ == '__main__':
	main()