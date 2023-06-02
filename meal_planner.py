import os 
from pandas import *
import random


class Food:
	def __init__(self, file_path, user = input('Please enter your name: ')):
		"""Passing products csv file path and user name"""
		self.file_path = file_path
		self.user = user

	def csv_column_to_list(self, column_name):
		"""Convert columns with dif food groups to lists"""
		with open(self.file_path) as food_csv:
			reader = read_csv(food_csv)
			lst = reader[str(column_name)].tolist()
			return lst
		
	def clean_from_nan(self, lst):
		"""Clean food groups lists from 'nan' values"""
		lst_cleaned = [x for x in lst if str(x) != 'nan']
		return lst_cleaned

	def lst_random(self, lst_cleaned):
		"""Randomize values inside each list """
		lst_randomized = random.sample(lst_cleaned, len(lst_cleaned))
		return lst_randomized 
	
	def get_food_list_from_csv(self, column_name):
		"""Get all the funcs together to get normalized food lists to work with"""
		food_list = self.lst_random(self.clean_from_nan(self.csv_column_to_list(column_name)))
		return food_list
				
	def get_carbs(self, carbs = []):
		"""Get list of available carbs"""
		self.carbs = carbs
		carbs = self.get_food_list_from_csv('Carbohydrate')
		return carbs 
	
	def get_protein(self, protein = []):
		"""Get list of available protein products"""
		self.protein = protein
		protein = self.get_food_list_from_csv('Protein')
		return protein 

	def get_bean(self, bean = []):
		"""Get list of available beans"""
		self.bean = bean 
		bean = self.get_food_list_from_csv('Bean')
		return bean 
	
	def get_vegs(self, vegs = []):
		"""Get list of available vegs"""
		self.vegs = vegs
		vegs = self.get_food_list_from_csv('Vegetable')
		return vegs
	
	def get_fruit(self, fruit = []):
		""""Get list of available fruits and berries"""
		self.fruit = fruit
		fruit = self.get_food_list_from_csv('Fruit_berry')
		return fruit 

	def create_menu(self):
		"""Assigns 1 product from each food group for each meal, for 1 week"""
		#Get all the macronutrients lists
		carbs = self.get_carbs()
		protein = self.get_protein()
		bean = self.get_bean()
		vegs = self.get_vegs()
		fruit = self.get_fruit()
		
		#Days of week list 
		week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		
		#Creating .txt file
		current_dir = os.getcwd()
		output_dir_path = os.path.join(current_dir, 'output')
		os.makedirs(output_dir_path, exist_ok=True)
		txt_file_path = os.path.join(output_dir_path, f'{str(self.user)}s_menu.txt')
		
		#Add menu to txt file
		with open(txt_file_path, 'w', newline='') as txt_menu:
			#List indexes paremeter (c for carbs, etc)
			c = p = v = f = b = w = 0
			while c < 13: 
				print(f'{week_days[w]}: ', file=txt_menu)
				print(f'Breakfast: {carbs[c]}, {protein[p]}, {vegs[v]} and {fruit[f]}', file=txt_menu)
				print(f'Lunch: {bean[b]}, {vegs[v+1]} and {fruit[f+1]}.', file=txt_menu)
				print(f'Dinner: {carbs[c+1]}, {protein[p+1]}, {vegs[v+2]} and {fruit[f+2]}. \n', file=txt_menu)
				w += 1
				c += 2
				p += 2
				v += 3
				f += 3
				b += 1

		print(f'Your menu is ready in the file {str(self.user)}s_menu.txt in the output directory.')
		#Ask user whether to print file in terminal
		display = input('Do you want to display the menu here? yes/no ')
		while display != 'yes' and display != 'no':
			print('try again')
			display = input('Do you want to display the menu here? yes/no ')
		else:
			if display == 'yes':
				with open(txt_file_path, 'r') as f:
					print(f.read())
			elif display == 'no':
				print('Ok! See you!')

#Test
user_menu = Food('food.csv')
user_menu.create_menu()

