#fast but not recursive implementation of fibonacci

def fib(n):
	fib_list = []
	fib_list.append(0)
	fib_list.append(1)


	for i in range(2, n+1):
		fib_list.append(fib_list[len(fib_list)-2] + fib_list[len(fib_list)-1])

	return fib_list


def main():
	n = 35
	fib_list = fib(n)
	for i in range(n+1):
		print(i, fib_list[i])

if __name__ == '__main__':
	main()