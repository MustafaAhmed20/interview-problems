"""
Problem one.
Runs with Python 3.6.3 or later
.
.

solved by Mustafa Ahmed
mmustafaadn@gmail.com


"""
import unittest

def persistence(num):
	"""
	takes in a positive parameter num and returns its multiplicative persistence.
	Args:
        num (int): The number.

    Returns:
        result (int): 0 or positive number represent the multiplicative persistence.
	"""

	#check if num is positive number
	try:
		if not float(num).is_integer() or num <= 0:
			raise ValueError("the input must be positive integer number") 
	except Exception as e:
		raise e

	result = 0
	while True:
		digits = [int(i) for i in str(num)]
		
		# multiple digits
		if len (digits) > 1:
			result +=1
			num = 1
			for i in digits:
				num *= i
		# one digit
		else:
			break
	return result

class testPersistence(unittest.TestCase):
	def testOne(self):
		# 3*9 = 27, 2*7 = 14, 1*4=4  -> 3
		self.assertEqual(persistence(39), 3)

		# 9*9*9 = 729, 7*2*9 = 126,   1*2*6 = 12, 1*2 = 2
		self.assertEqual(persistence(999), 4)
		
		# already one digit
		self.assertEqual(persistence(4), 0)

		# 5*5 = 25, 2*5 = 10, 1*0 = 0   -> 3
		self.assertEqual(persistence(55), 3)

if __name__ == "__main__":
	unittest.main()
	