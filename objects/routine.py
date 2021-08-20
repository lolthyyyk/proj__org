import os
from colorama import init

init(autoreset=True)

class routine(object):
	def _cyan(arg,Obj):
		return Obj.CYAN + arg + Obj.RESET
	def _red(arg,Obj):
		return Obj.RED + arg + Obj.RESET
	def _green(arg,Obj):
		return Obj.GREEN + arg + Obj.RESET
	def _yellow(arg,Obj):
		return Obj.YELLOW + arg + Obj.RESET
	def _clear():
		os.system(OsCommands()._clear)
	def _file_qualifier(filename):
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

class OsCommands:
	def __init__(self):
		if os.name == 'nt':
			self._clear = 'cls'
		elif os.name == 'posix':
			self._clear = 'clear'
