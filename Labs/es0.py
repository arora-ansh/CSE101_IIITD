number=10
while True:
	try:
		i=int(input())
		if i<number:
			raise ValueTooSmallError
		elif i>number:
			raise ValueTooLargeError
		break
	except ValueTooSmallError:
		print("Too Small")
	except ValueTooLargeError:
		print("Too Large")

	print("Congrats bruh")