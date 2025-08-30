from utils import repeter_mot

class Instrument():
	def __init__(
		self,
		nom: str
	):
		self._nom: str = nom

	def jouer( self ) -> None:
		print( "Impossible" )

class Piano( Instrument ):
	sons: list[str] = ["Plink"]
	def __init__(
		self,
		nom: str,
		n_touche: int
	):
		super().__init__( nom )
		self._n_touche: int = n_touche

	def jouer( self ):
		repeter_mot( Piano.sons[0], self._n_touche )

class Batterie( Instrument ):
	sons: list[str] = ["Boom","Tink"]
	def __init__(
		self,
		nom: str,
		cymbale: bool
	):
		super().__init__( nom )
		self._cymbale = cymbale

	def jouer( self ):
		print(f"{Batterie.sons[0]}{Batterie.sons[int(self._cymbale)]}" )
		