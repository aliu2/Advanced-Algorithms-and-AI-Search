import math

def dp_make_change(amount, coins):
	memo = [math.inf] * (amount + 1)
	memo[0] = 0
	coins.reverse()

	for n in range(1, len(memo)):
		curr_amount = n
		counter_array = []

		for j in range(len(coins)):
			counter = 0
			i = j

			while curr_amount > 0 and i < len(coins) and i > 0:
				if coins[i] <= curr_amount:
					counter += 1
					curr_amount -= coins[i]
				else:
					i -= 1

			counter_array.append(counter)

		if curr_amount == 0:
			memo[n] = min(counter_array)


	return memo


def main():
	print(dp_make_change(12, [5,2,1]))


if __name__ == '__main__':
	main()