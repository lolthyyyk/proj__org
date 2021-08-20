from .org import Organizer,Notifications,Options,routine

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
		routine._clear()
