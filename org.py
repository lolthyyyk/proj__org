from colorama 				import init,Fore,Back
from pygments 				import highlight
from pygments.lexers 		import PythonLexer, HtmlLexer, JavascriptLexer
from pygments.formatters 	import TerminalFormatter
import os
import time

from .objects.routine import routine

init(autoreset=True)

def file_qualifier(filename):
	if filename.endswith('.html'):
		with open(filename,encoding='utf8') as f:
			return highlight(f.read(),HtmlLexer(),TerminalFormatter())
	if filename.endswith('.js'):
		with open(filename,encoding='utf8') as f:
			return highlight(f.read(),JavascriptLexer(),TerminalFormatter())
	if filename.endswith('.py'):
		with open(filename,encoding='utf8') as f:
			return highlight(f.read(),PythonLexer(),TerminalFormatter())
	if filename.endswith('.txt'):
		with open(filename,encoding='utf8') as f:
			return f.read()

class Organizer:
	def __init__(self,options_object,notifications_object):
		self.pos = 1
		self.option = False
		self.options = options_object()
		self.notifications = notifications_object()
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
					# if os.listdir()[self.pos-1].endswith('.py')
					if file_qualifier(os.listdir()[self.pos-1]):
						routine.clear()
						print(file_qualifier(os.listdir()[self.pos-1]),flush=True)
						input(f"\nНАЖМИ {routine._green('ENTER',Fore)} ЧТО БЫ ПОКИНУТЬ РЕЖИМ ЧИТАТЕЛЯ")
					else:
						self.notifications.addUsual('Органайзер не умеет читать данный формат файлов')
					self.pos=1
			#
		if self.option == True:
			self.option = self.options.select()
	def render(self):
		count=0
		output=f"  {os.getcwd()}\n\n{self._iscurrent(count,'...')}\n\n"
		for i in os.listdir():
			count += 1
			output += '  ' + self._iscurrent(count,i)+'\n'
		output += self.notifications.get()
		return output