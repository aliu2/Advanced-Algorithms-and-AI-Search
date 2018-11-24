def make_greedy_sum(total, coins):
	num_of_coins = [0] * len(coins)
	i = 0

	while total > 0 and i < len(coins):
		if coins[i] <= total:
			num_of_coins[i] += 1
			total -= coins[i]
		else:
			i += 1
	return num_of_coins

def min_coins(amount, coins, memo = {}):
	assert amount >= 0
	
	if amount in memo:
		return memo[amount]
	elif amount == 0:
		return 0 # base case
	else:
		# try every possibility
		memo[amount] = min([1 + min_coins(amount - coin, coins, memo) for coin in coins if coin <= amount])
		return memo[amount]

# The amount is 49 and the coins are [52, 28, 24, 1]

def main():
	print(f"The greedy algorithm says it takes {sum(make_greedy_sum(49, [52, 28, 24, 1]))} coins")
	print(f"The non-greedy algorithm says it takes only {min_coins(49, [52, 28, 24, 1])} coins")


if __name__ == '__main__':
	main()