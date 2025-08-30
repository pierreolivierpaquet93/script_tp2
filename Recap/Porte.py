
class Porte():
	DOOR_OPENED = ( True, "Ouvert" )
	DOOR_CLOSED = ( False, "Fermer" )
	def __init__( self ):
		self.__state: tuple[bool,str] = Porte.DOOR_CLOSED

	def ouvrir( self ) -> None:
		self.__state =  Porte.DOOR_OPENED
	
	def fermer( self ) -> None:
		self.__state = Porte.DOOR_CLOSED
	
	def afficher_etat( self ) -> None:
		print( self.__state[1] )

class PorteCode(Porte):
	def __init__(
		self,
		code: str
	):
		super().__init__()
		self.__code = code
	
	def ouvrir( self ):
		pass

	def checkCode(
		self,
		code: str
	) -> bool:
		return ( code == self.__code )

	def ouvrir_avec_code(
		self,
		code: str
	):
		if self.checkCode( code ) == True:
			super().ouvrir()

class PorteVerrou(Porte):
	def __init__( self ):
		super().__init__()
		self.__locked = True

	def deverouiller( self ) -> None:
		self.__locked = False

	def verrouiller( self ) -> None:
		self.__locked = True

	def ouvrir( self ):
		if self.__locked == False:
			super().ouvrir()
	