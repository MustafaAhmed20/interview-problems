"""
Problem three.
Runs with Python 3.6.3 or later
.
.

solved by Mustafa Ahmed
mmustafaadn@gmail.com


"""
import unittest

def formatTime(seconds):
	"""
	takes in a positive number of seconds and returns string represent time in human-friendly way.
	
	Args:
        seconds (integer): positive integer.

    Returns:
        result (string): time in human-friendly way
	"""

	# check the validity of the input
	if seconds <0 :
		raise ValueError("seconds can't be negative number")

	if seconds == 0:
		return "now"

	
	
	minutes = seconds // 60
	hour = minutes // 60 
	days = hour // 24
	years = days // 365 

	seconds %= 60
	minutes %= 60
	hour %= 24
	days %= 365

	# format the time and add the 's' if the value > 1
	availableFormats = [f'{years} year' + ('s' if years > 1 else '') if years else None,\
			f'{days} day' + ('s' if days > 1 else '') if days else None,\
			f'{hour} hour' + ('s' if hour > 1 else '') if hour else None,\
			f'{minutes} minute' + ('s' if minutes > 1 else '')  if minutes else None,\
			f'{seconds} second' + ('s' if seconds > 1 else '')  if seconds else None]

	# remove None values
	for _ in range(availableFormats.count(None)):
		availableFormats.remove(None)

	return ' and '.join([', '.join(availableFormats[:-1]), availableFormats[-1]] \
						if len(availableFormats) > 2 else availableFormats)
	
class testFormatTime(unittest.TestCase):
	def testOne(self):
		
		self.assertEqual(formatTime(0), 'now')

		self.assertEqual(formatTime(62), '1 minute and 2 seconds')

		self.assertEqual(formatTime(3662), '1 hour, 1 minute and 2 seconds')
		

	def test2(self):
		self.assertEqual(formatTime(122), '2 minutes and 2 seconds')
		
		self.assertEqual(formatTime(121), '2 minutes and 1 second')


if __name__ == "__main__":
	unittest.main()
