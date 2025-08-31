import os

RECIPEWPRICE_FILENAME = "RecetteWithPrice.txt"
SEP = ':'

def locate(
	haystack: str,
	needle: str
) -> int:
	length = len( haystack )
	i = 0
	while i < length:
		if haystack[i] == needle[0]:
			length_needle = len( needle )
			j = 0
			while haystack[i+j] == needle[j]:
				j += 1
				if j == length_needle:
					return i
		i += 1
	return -1

def display_number( n: float ):
	cast_before: int = int( int(n) * 100 )
	cast_after: int = int( n * 100 )
	if cast_before == cast_after:
		return int( n )
	return n

class RecipeCalculator():
	def __init__(
		self,
		liste_de_prix: str,
		recette: str
	):
		self._path_liste_de_prix = liste_de_prix
		self._path_recette = recette
		self._liste_de_prix: dict[str:float] = {}
		self._recette: dict[str,dict[str,float]] = {}

		with open( self._path_liste_de_prix, 'r' ) as f:
			for line in f:
				if locate( line, SEP ) >= 0:
					tmp = line.split( ':', 2 )
					self._liste_de_prix[tmp[0]] = float( tmp[1] )

		with open( self._path_recette, 'r' ) as f:
			current_recipe = ""
			for line in f:
				if locate( line , "---" ) >= 0:
					current_recipe = line
					self._recette[current_recipe] = {}
				if locate( line, ':' ) >= 0:
					tmp = line.split( ':', 2 )
					self._recette[current_recipe][tmp[0]] = float( tmp[1] )
		
		self._path_recipe_with_price = (
			f"{os.path.dirname( self._path_recette )}\\" + 
			f"{RECIPEWPRICE_FILENAME}"
		)
		print( self._path_recipe_with_price )
		with open( self._path_recipe_with_price, 'w' ) as f:
			for recipe in self._recette:
				total = 0
				f.write( recipe )
				for item in self._recette[recipe]:
					f.write(
						item +
						":" +
						str( display_number(self._recette[recipe][item]))
						+ "\n"
					)
					
