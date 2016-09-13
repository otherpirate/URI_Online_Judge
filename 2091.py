while True:
	executions = int(input())
	if executions == 0:
		break
	numbers = [int(number) for number in input().split()]

	lonely = {}
	for number in numbers:
		if number in lonely:
			del lonely[number]
		else:
			lonely[number] = True

	for key in lonely.keys():
		print(key)