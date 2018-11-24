import math

class Item(object):

	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

	def __repr__(self):
		return f"({self.value}, {self.weight})"


def ks_greedy(capacity, items):
	assert capacity >= 0
	total_value = 0
	items.sort(key=getValue, reverse=True)

	for item in items:
		while capacity >= item.weight:
			total_value += item.value
			capacity -= item.weight

	return total_value


def dp_knapsack(capacity, items):
	assert capacity >= 0
	memo = [math.inf] * (capacity+1)
	memo[0] = 0

	for i in range(1, len(memo)):
		memo[i] = ks_greedy(i, items)

	return memo


def getValue(item):
	return item.value/item.weight


def main():
	print(dp_knapsack(10, [Item(20, 5), Item(300, 11), Item(4, 2)]))


if __name__ == '__main__':
	main()