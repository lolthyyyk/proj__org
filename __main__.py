from colorama import Fore,Back

# from .objects.interface  	import Interface
from .objects.org  			import Organizer
from .objects.notifications import Notifications
from .objects.options 		import Options
from .objects.routine 		import routine

if __name__ == '__main__':
	routine._clear()
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
		routine._clear()
		if key == 'h':
			print(routine._green('Нажимая Enter вы даётё утилите команду',Fore))
			print(f"{routine._cyan('[help]',Fore)}"+"\t\t - Получить данную подсказку")
			print(f"{routine._cyan('[пустая строка]',Fore)}"+"\t - Переместиться ниже")
			print(f"{routine._cyan('[a]',Fore)}"+"\t\t - Получить опции выбранного файла или директории")
			print(f"{routine._cyan('[пробел]',Fore)}"+"\t - Получить опции выбранного файла или директории\n")
			input(f"Нажмите {routine._yellow('ENTER',Back)} что бы выйти")
			routine._clear()
