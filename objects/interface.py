import os
from .routine import routine
from colorama import Fore,Back

class Interface:
	def __init__(self,organaizer_class,options_class,notifications_class):
		self.organizer = organaizer_class(options_class,self)
		self.notifications = notifications_class()
	def run(self):
		while True:
			print(self.render())
			key = input()
			self.react(key)
	def react(self,key):
		if key == 'h':
			print(routine._green('Нажимая Enter вы даётё утилите команду',Fore))
			print(f"{routine._cyan('[help]',Fore)}"+"\t\t - Получить данную подсказку")
			print(f"{routine._cyan('[пустая строка]',Fore)}"+"\t - Переместиться ниже")
			print(f"{routine._cyan('[a]',Fore)}"+"\t\t - Получить опции выбранного файла или директории")
			print(f"{routine._cyan('[пробел]',Fore)}"+"\t - Получить опции выбранного файла или директории\n")
			input(f"Нажмите {routine._yellow('ENTER',Back)} что бы выйти")
			routine._clear()
		elif key == ' ':
			self.organizer.select()
		elif key == '':
			self.organizer.after()
		elif key == 'a':
			if self.organizer.pos != 0:
				self.organizer.option = True
	def render(self):
		routine._clear()
		count=0
		output=f"  {os.getcwd()}\n\n{self.organizer._iscurrent(count,'...')}\n\n"
		for i in os.listdir():
			count += 1
			output += '  ' + self.organizer._iscurrent(count,i)+'\n'
		output += self.notifications.get()
		return output