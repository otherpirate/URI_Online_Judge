executions = int(input())

for execution in range(executions):
	products = {}
	total = 0

	store_items = int(input())
	for item in range(store_items):
		name, value = input().split()
		products[name] = float(value)

	list_items = int(input())
	for item in range(list_items):
		name, quantity = input().split()
		total += products[name] * int(quantity)

	print('R$ %0.2f' % total)