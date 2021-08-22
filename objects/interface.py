from .routine import routine
from colorama import Fore,Back

# Класс оболочки программы
class Interface:
	
	def __init__(self,organaizer_class,options_class,notifications_class):
		
		self.organizer = organaizer_class(options_class,self)
		self.notifications = notifications_class()
	
	def run(self): # Запуск оболочки
		
		while True:
			print(self.render())
			key = input()
			self.react(key)
	
	def react(self,key): # Интерактив оболочки
		
		if key == 'h':
			self.help()
		elif key == ' ':
			self.organizer.select()
		elif key == '':
			self.organizer.after()
		elif key == 'a':
			if self.organizer.pos != 0:
				self.organizer.option = True
	
	
	def render(self): # Отрисовка оболочки
		
		brief = self.organizer.brief()

		def _iscurrent(count,arg): # 
			if count == self.organizer.pos:
				if brief["items"] == []:
					return routine._yellow('>>>'+arg,Fore)
				return routine._yellow('>>>'+arg,Fore)+self.organizer.options.get_options(brief["items"][self.organizer.pos-1],self.organizer.option)
			else:
				return "   " + arg

		routine._clear()
		count=0
		output=f"\n\t{brief['location']}\n\n\t{_iscurrent(count,'...')}\n\n"
		for i in brief["items"]:
			count += 1
			output += '\t' + _iscurrent(count,i)+'\n'
		output += self.notifications.get()
		return output

	def see_item(self,name): # Режим читателя

		routine._clear()
		print(routine._file_qualifier(name),flush=True)
		input(f"\nНАЖМИ {routine._green('ENTER',Fore)} ЧТО БЫ ПОКИНУТЬ РЕЖИМ ЧИТАТЕЛЯ")

	def help(self): # Вызов мануала

		routine._clear()
		print(routine._green('Нажимая Enter вы даётё утилите команду',Fore))
		print(f"{routine._cyan('[h]',Fore)}"+"\t\t - Получить данную подсказку")
		print(f"{routine._cyan('[пустая строка]',Fore)}"+"\t - Переместиться ниже")
		print(f"{routine._cyan('[a]',Fore)}"+"\t\t - Получить опции выбранного файла или директории")
		print(f"{routine._cyan('[пробел]',Fore)}"+"\t - Получить опции выбранного файла или директории\n")
		input(f"Нажмите {routine._yellow('ENTER',Back)} что бы выйти")
		routine._clear()

