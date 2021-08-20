import os

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

class OsCommands:
	def __init__(self):
		if os.name == 'nt':
			self._clear = 'cls'
		elif os.name == 'posix':
			self._clear = 'clear'
