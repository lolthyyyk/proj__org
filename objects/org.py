from colorama 				import Fore,Back
import os

from .routine import routine

class Organizer:
	def __init__(self,options_class,interface):
		self.pos = 1
		self.option = False
		self.options = options_class()
		self.interface = interface
	def _iscurrent(self,count,arg):
		if count == self.pos:
			if os.listdir() == []:
				return routine._yellow('>>>'+arg,Fore)
			return routine._yellow('>>>'+arg,Fore)+self.options.get_options(os.listdir()[self.pos-1],self.option)
		else:
			return arg
	def after(self):
		if self.option == False:
			if len(os.listdir()) == self.pos:
				self.pos = 0
			else:
				self.pos+=1
		elif self.option == True:
			self.options.after()
	def select(self):
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
						routine._clear()
						print(routine._file_qualifier(os.listdir()[self.pos-1]),flush=True)
						input(f"\nНАЖМИ {routine._green('ENTER',Fore)} ЧТО БЫ ПОКИНУТЬ РЕЖИМ ЧИТАТЕЛЯ")
					else:
						self.interface.notifications.addUsual('Органайзер не умеет читать данный формат файлов')
		if self.option == True:
			self.option = self.options.select()