from .routine import routine

class Interface:
	def __init__(self):
		self.organizer = Organizer(Options,Notifications)
	def run(self):
		while True:
			routine._clear()
			print(self.organizer.render(),end='\r')
			key = input()
			self.react(key)
	def react(self,key):
		if key == 'h':
			print(routine._green('Нажимая Enter вы даётё утилите команду'))
			print(f"{routine._cyan('[help]')} - Получить данную подсказку")
			print(f"{routine._cyan('[пустая строка]')} - Переместиться ниже")
			print(f"{routine._cyan('[a]')} - Получить опции выбранного файла или директории")
			print(f"{routine._cyan('[пробел]')} - Получить опции выбранного файла или директории")
		elif key == ' ':
			self.organizer.select()
		elif key == '':
			self.organizer.after()
		elif key == 'a':
			if self.organizer.pos != 0:
				self.organizer.option = True
