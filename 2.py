"""
Problem two.
Runs with Python 3.6.3 or later
.
.

solved by Mustafa Ahmed
mmustafaadn@gmail.com


"""
import unittest

def score(words):
	"""
	takes in a string of words and returns the highest scoring word in the string.
	note : the score of a word is the sum of the score of its letters.
	Args:
        words (string): string made of lowercase words.

    Returns:
        result (string): highest scoring word.
	"""

	words = words.strip().split()
	scoreWords = {}

	for word in words:
		# calculate the score using the ascii
		score = sum(ord(i) - 96 for i in word )
		
		if score not in scoreWords:
			scoreWords[score] = [word]
		else:
			# words with the same score
			scoreWords[score].append(word)

	return scoreWords[max(scoreWords)][0]

class testScore(unittest.TestCase):
	def testOne(self):
		
		self.assertEqual(score("man i need a taxi up to ubud"), 'taxi')

		self.assertEqual(score("what time are we climbing up to the volcano"), 'volcano')

		self.assertEqual(score("take me to semynak"), 'semynak')

if __name__ == "__main__":
	unittest.main()
	