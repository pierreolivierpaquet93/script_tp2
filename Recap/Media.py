class Media():
	def __init__(
		self,
		titre: str,
		duree: int
	):
		self._titre: str = titre
		self._duree_m: int = duree

	def getDureeHeure( self ) -> float:
		duree_heure: float = int((self._duree_m / 60)*10) 
		return ( duree_heure / 10 )

	def donne_information( self ) -> None:
		info = f"Titre: {self._titre}\n"
		info += f"Durée: {self.getDureeHeure()}H"
		print( info )
