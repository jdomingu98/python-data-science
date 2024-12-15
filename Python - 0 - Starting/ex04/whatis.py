import sys

try:
	if len(sys.argv) < 2:
		exit()
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	try:
		number = int(sys.argv[1])
		print(f"I'm Odd." if number % 2 else f"I'm Even.")
	except ValueError:
		raise AssertionError("argument is not an integer")
except AssertionError as e:
	print(f"{AssertionError.__name__}: {e}")