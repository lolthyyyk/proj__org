from colorama import Fore 
from .routine import routine

class Notifications:
	def __init__(self):
		self.important = []
		self.usual = []
	def addUsual(self,notification):
		self.usual.append(notification)
	def addImportant(self,notification):
		self.imortant.append(notification)
	def removeImportant(self,index):
		self.important.pop(index)
	def get(self):
		output = '\n' 
		for i in self.important:
			output += f'[{routine._red(i,Fore)}]\n'
		output+='\n'
		for i in self.usual:
			output += f'[{routine._green(i,Fore)}]\n'
		self.usual = []
		return output
			