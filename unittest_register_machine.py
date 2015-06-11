import application
import unittest

class TestRegisterMachine(unittest.TestCase):
	#Function 1
	def test_question_add(self):
		self.assertTrue(application.question_add("CASA").islower())
	#Function 2
	def test_select_option(self):
		self.assertTrue(application.select_option('5') == False)
		self.assertTrue(application.select_option("hola") == True)
	#Function 3
	def test_the_product(self):
		self.assertTrue(application.the_product("producto").isalpha())
	#Function 4
	def test_the_price(self):
		self.assertTrue(type(application.the_price("product",1)) == int)
	#Function 5
	def test_silver_card(self):
		self.assertEqual(application.silver_card(5),0.10)
	#Function 6
	def test_gold_card(self):
		self.assertEqual(application.gold_card(5),0.25)
	#Function 7
	def test_mySubtotal(self):
		self.assertEqual(application.mySubtotal(5,3),8.00)
	#Function 8
	def test_myFinalTotal(self):
		self.assertEqual(application.myFinalTotal(10,5),5.00)
	#Function 9
	def test_buy_product(self):
		self.assertTrue(application.buy_product("HOLA").islower())
	#Function 10
	def test_less_or_greater(self):
		self.assertEqual(application.less_or_greater(5),"INSERT A VALID OPTION!!!")
	#Function 11
	def test_myTry(self):
		self.assertEqual(application.myTry("uno"),"INSERT ONLY NUMBERS!!!")
	#Function 12
	def test_main_menu(self):
		self.assertGreaterEqual(application.main_menu(1),1)
		self.assertLessEqual(application.main_menu(3),3)

if __name__ == "__main__":
	unittest.main()