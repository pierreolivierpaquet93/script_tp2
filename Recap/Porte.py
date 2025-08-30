DOOR_OPENED = ( True, "Ouvert" )
DOOR_CLOSED = ( False, "Fermer" )

class Porte():
	def __init__( self ):
		self.__state: tuple[bool,str] = DOOR_CLOSED

	def ouvrir( self ) -> None:
		self.__state =  DOOR_OPENED
	
	def fermer( self ) -> None:
		self.__state = DOOR_CLOSED
	
	def afficher_etat( self ) -> None:
		print( self.__state[1] )
