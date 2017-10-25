# test_yield.py

def run_order():
	for x in range(3):
		# print("Previous",x)
		yield print("yield",x)
		# print("next",x)

r = run_order()


