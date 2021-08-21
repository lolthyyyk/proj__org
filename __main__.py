from colorama import Fore,Back

from .objects.interface  	import Interface
from .objects.org  			import Organizer
from .objects.notifications import Notifications
from .objects.options 		import Options
from .objects.routine 		import routine

if __name__ == '__main__':
	routine._clear()
	interface = Interface(Organizer,Options,Notifications)
	interface.run() 	