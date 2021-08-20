from .routine import routine

class Interface:
	def __init__(self,organaizer_object,notifications_object):
		self.organizer = organaizer_object
		self.notifications = notifications_object
	def run(self):
		while True:
			routine._clear()
			print(self.organizer.render(),end='\r')
			key = input()
			self.react(key)
			self.render()
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
	def render(self):
		count=0
		output=f"  {os.getcwd()}\n\n{self._iscurrent(count,'...')}\n\n"
		for i in os.listdir():
			count += 1
			output += '  ' + self._iscurrent(count,i)+'\n'
		output += self.notifications.get()
		return output
