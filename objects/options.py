import os
from colorama import Fore
from .routine import routine

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
				return routine._yellow(arg,Fore)
			else:
				return routine._green(arg,Fore)
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