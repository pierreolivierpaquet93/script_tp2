import utils as ut
import Media as med
import Instrument as ins
import Porte as por

# ------------------------------------------------------------------------------

def test_utils():
	ut.repeter_mot( "Bonjour", 0)
	ut.repeter_mot( "Impossible", -1 )
	ut.repeter_mot( "Répéter", 3 )
	
	numbers: list[int] = [-1, 2, 3, 4]
	print( ut.somme_liste( numbers ) )

	test_tuple = ut.separe_text( "LeftHandSide:RightHandSide", ":" )
	print( test_tuple[0] )
	print( test_tuple[1] )

# ------------------------------------------------------------------------------
def test_media():
	media = med.Media("Donnie Darko",102)
	media.donne_information()

# ------------------------------------------------------------------------------
def test_instrument():
	#instrument = ins.Instrument( "Triangle" )
	#instrument.jouer()

	#piano = ins.Piano( "Yamaha", 4 )
	#piano.jouer()

	batterie = ins.Batterie( "Pearl", False )
	batterie.jouer()

# ------------------------------------------------------------------------------
def test_porte():
	porte = por.Porte()
	porte.afficher_etat()
	porte.ouvrir()
	porte.afficher_etat()
	porte.fermer()
	porte.afficher_etat()

# --------------------------------------------------------------------- [ MAIN ]

def main():
	#test_utils()
	#test_media()
	test_instrument()
	#test_porte()

if __name__ == "__main__":
    main()
