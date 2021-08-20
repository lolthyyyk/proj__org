from colorama import init,Fore,Back
from pygments import highlight
from pygments.lexers import PythonLexer, HtmlLexer, JavascriptLexer
from pygments.formatters import TerminalFormatter
import os
import time

init(autoreset=True)

def file_dispatcher(filename):
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

class OsComands:
	def __init__(self):
		if os.name == 'nt':
			self._clear = 'cls'
		elif os.name == 'posix':
			self._clear = 'clear'

class routine(object):
	def cyan(arg,Obj):
		return Obj.CYAN + arg + Obj.RESET
	def red(arg,Obj):
		return Obj.RED + arg + Obj.RESET
	def green(arg,Obj):
		return Obj.GREEN + arg + Obj.RESET
	def yellow(arg,Obj):
		return Obj.YELLOW + arg + Obj.RESET
	def clear():
		os.system(OsComands()._clear)

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
			output += f'[{routine.red(i,Fore)}]\n'
		output+='\n'
		for i in self.usual:
			output += f'[{routine.green(i,Fore)}]\n'
		self.usual = []
		return output

class Options:
	def __init__(self):
		self.filename = None
		self.dir_opt = [
			['Удалить папку',os.remove]
		]
		self.file_opt = [
			['Удалить файл',os.remove]
		]
		self.cur_opt = None
		self.pos = 1
	def _iscurrent(self,count,arg):
		if count == self.pos:
			if self.cur_opt == None:
				return routine.yellow(arg,Fore)
			else:
				return routine.green(arg,Fore)
		else:
			return arg
	def after(self):
		if len(self.cur_opt) == self.pos:
			self.pos = 0
		else:
			self.pos += 1
	def select(self):
		if self.pos == 0:
			return False
		else:
			self.cur_opt[self.pos-1][1](self.filename)
			self.cur_opt = None
			self.filename = None
			return False
	def get_options(self,item,org_opt):
		self.filename = item
		if org_opt == False:
			return ""
		count = 0
		output = self._iscurrent(count,"\n\t<---\n")
		if os.path.isdir(item):
			self.cur_opt=self.dir_opt
		else:
			self.cur_opt=self.file_opt
		for i in self.cur_opt:
			count+=1
			output+=f'\t{self._iscurrent(count,i[0])}'
		return output
			
class Organizer:
	def __init__(self,options_object,notifications_object):
		self.pos = 1
		self.option = False
		self.options = options_object()
		self.notifications = notifications_object()
	def _iscurrent(self,count,arg):
		if count == self.pos:
			if os.listdir() == []:
				return routine.yellow('>>>'+arg,Fore)
			return routine.yellow('>>>'+arg,Fore)+self.options.get_options(os.listdir()[self.pos-1],self.option)
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
					if file_dispatcher(os.listdir()[self.pos-1]):
						routine.clear()
						print(file_dispatcher(os.listdir()[self.pos-1]),flush=True)
						input(f"\nНАЖМИ {routine.green('ENTER',Fore)} ЧТО БЫ ПОКИНУТЬ РЕЖИМ ЧИТАТЕЛЯ")
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

class Interface:
	def __init__(self):
		self.organizer = Organizer(Options,Notifications)
	def run(self):
		while True:
			routine.clear()
			print(self.organizer.render(),end='\r')
			key = input()
			self.react(key)
	def react(self,key):
		if key == 'help':
			print(routine.green('Нажимая Enter вы даётё утилите команду'))
			print(f"{routine.cyan('[help]')} - Получить данную подсказку")
			print(f"{routine.cyan('[пустая строка]')} - Переместиться ниже")
			print(f"{routine.cyan('[a]')} - Получить опции выбранного файла или директории")
			print(f"{routine.cyan('[пробел]')} - Получить опции выбранного файла или директории")
		elif key == ' ':
			self.organizer.select()
		elif key == '':
			self.organizer.after()
		elif key == 'a':
			if self.organizer.pos != 0:
				self.organizer.option = True


if __name__ == '__main__':
	routine.clear()
	org = Organizer(Options,Notifications)
	while True:
		print(org.render())
		# print(org.pos,end='\r')
		key = input()
		if key == '':
			org.after()
		elif key == ' ':
			org.select()
		elif key == 'a':
			if org.pos != 0:
				org.option =True
		routine.clear()



