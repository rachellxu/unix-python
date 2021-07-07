def main():

	print("How big is your brain?")
	input("[type enter to start]")

	mylist = [0, 0, 0]

	print(
		"""Can you tell when a boy likes you? 
	a. Yes - always
	b. No - never I am blind
	c. Sometimes - depends if they're obvious or not"""
	)

	value1 = input("[type a, b, or c]")

	if value1 == "a":
		mylist[0] += 1
	elif value1 == "b":
		mylist[1] += 1
	elif value1 == "c": 
		mylist[2] += 1
	else: 
		print("Choose one of the options chicken brain")
		return

	print(
		"""Can you rememember the score when you play volleyball?
	a. Yes - easy peasy, I always no the score
	b. No - I can never remember even when people tell me
	c. Sometimes - depends on my mood"""
	)

	value2 = input("[type a, b, or c]")

	if value2 == "a":
		mylist[0] += 1
	elif value2 == "b":
		mylist[1] += 1
	elif value2 == "c": 
		mylist[2] += 1
	else: 
		print("Choose one of the options chicken brain")
		return

	print(
		"""Can you remember song lyrics well?
	a. Yes - only takes me a couple listens
	b. No - my brain small
	c. Sometimes - if I listen enough"""
	)

	value3 = input("[type a, b, or c]")

	if value3 == "a":
		mylist[0] += 1
	elif value3 == "b":
		mylist[1] += 1
	elif value3 == "c": 
		mylist[2] += 1
	else: 
		print("Choose one of the options chicken brain")
		return

	print("Here is your result!")
	input("[hit enter to view]")

	if mylist[0] >= 2:
		print("You got a galaxy brain, good 4 u!")

	elif mylist[1] >= 2:
		print("You got a big brain, lame.")

	elif mylist[2] >= 2:
		print("You got a chicken brain, haha.")

	else: 
		print("You got a chicken brain, haha.")

	# print(mylist)




	# tiny buzzfeed quiz
	#


	# =================================

	# value1 = input("num1 :")
	# value2 = input("num2 :")

	# print(int(value1) + int(value2))

	# =================================

	# print("Who are you? :")
	# value = input("Who are you? :")

	# print("Hello " + value)

	# ask a question

	# =================================

    # print(__name__)

    # a = 100
    # print(str(a))

    # b = "taylor swift"
    # print(b)

if __name__ == "__main__":
    main()