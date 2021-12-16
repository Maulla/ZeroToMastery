import unittest 
import script

class TestScript(unittest.TestCase):
	def setup(self):
		print('about to test some stuff')

	def test_input(self):
		result = script.run_guess(5, 5)
		self.assertTrue(result)

	def test_input_wrong_guess(self):
		result = script.run_guess(5, 0)
		self.assertFalse(result)

	def test_input_too_high(self):
		result = script.run_guess(5, 11)
		self.assertFalse(result)

	def test_input_wrong_type(self):
		result = script.run_guess(5, '11')
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()