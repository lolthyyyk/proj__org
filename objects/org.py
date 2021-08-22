import os
from .routine import routine

# Ядро файлового менеджера
class Organizer:
	
	def __init__(self,options_class,interface):
	
		self.pos = 1
		self.option = False
		self.options = options_class()
		self.interface = interface
	
	def after(self): # Перейти на следущий элемент
	
		if self.option == False:
			if len(os.listdir()) == self.pos:
				self.pos = 0
			else:
				self.pos+=1
		elif self.option == True:
			self.options.after()
	
	def select(self): # Выбрать текущий элемент
	
		if self.option == False:
			if self.pos == 0:
				os.chdir('..')	
			else:
				if os.path.isdir(os.listdir()[self.pos-1]):
					os.chdir(os.listdir()[self.pos-1])
					self.pos=1
					if os.listdir() == []:
						self.pos = 0
				else:
					if routine._file_qualifier(os.listdir()[self.pos-1]):
						self.interface.see_item(os.listdir()[self.pos-1])
					else:
						self.interface.notifications.addUsual('Органайзер не умеет читать данный формат файлов')
		if self.option == True:
			self.option = self.options.select()

	def brief(self): # Отчёт о состоянии

		return {
			'items': os.listdir(),
			'location': os.getcwd(),
		}