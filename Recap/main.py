import utils as ut
import Media as med
import Instrument as ins
import Porte as por

# ------------------------------------------------------------------ [ COLOR.S ]

BLD = "\033[1m"
BLU = "\033[1;34m"
GRN = "\033[1;32m"
RED = "\033[1;31m"
RST = "\033[0m"

# --------------------------------------------------------------------- [ MISC ]

SEP = "-----"

# ------------------------------------------------------------------------------

def test_title( name:str ) -> str:
	title = f"\n{BLU}[ {name} ]{RST}"
	return title

def banner(
	title: str,
	color: str = ""
) -> str:
	len = 5
	if color != "":
		len *= 2
	banner = SEP * len
	banner += f"[ {color}{title}{RST} ]"
	return banner

# ------------------------------------------------------------------------------

def test_utils():
	print( test_title( "TEST_UTILS" ) )
	print( banner('repeter_mot( "bonjour", 0 )', RED) )
	ut.repeter_mot( "Bonjour", 0)
	print( banner('repeter_mot( "Impossible", -1 )', RED) )
	ut.repeter_mot( "Impossible", -1 )
	print( banner('repeter_mot( "Répéter\\n", 3 )', GRN) )
	ut.repeter_mot( "Répéter\n", 3 )
	
	print( banner( 'somme_liste( [-1, 2 ,3, 4] )', GRN) )
	numbers: list[int] = [-1, 2, 3, 4]
	print( ut.somme_liste( numbers ) )

	print( banner( 'somme_liste( [-100, -93465, 93465, 100] )', GRN) )
	numbers: list[int] = [-100, -93465, 93465, 100]
	print( ut.somme_liste( numbers ) )

	print( banner( 'separe_text( "LeftHandSide:RightHandSide", ":" )', GRN ) )
	test_tuple = ut.separe_text( "LeftHandSide:RightHandSide", ":" )
	print( test_tuple )

	print(
		banner(
			'separe_text( "Please Do Not Throw Sausage Pizza Away", " " )',
			GRN
		)
	)
	test_tuple = ut.separe_text( "Please Do Not Throw Sausage Pizza Away", " " )
	print( test_tuple )

# ------------------------------------------------------------------------------
def test_media():
	print( test_title( "TEST_MEDIA" ) )
	print( banner( 'Donnie Darko, 113 min :: donne_information()', GRN ) )
	media = med.Media("Donnie Darko",113)
	media.donne_information()

	print( banner( 'hagazussa, 102 min :: donne_information()', GRN ) )
	media = med.Media("hagazussa",102)
	media.donne_information()

	print( banner( 'Kung Fury, 31 min :: donne_information()', GRN ) )
	media = med.Media("Kung Fury", 31)
	media.donne_information()

# ------------------------------------------------------------------------------
def test_instrument():
	print( test_title( "TEST_INSTRUMENT" ) )

	print( banner( 'Instrument :: "Triangle"', RED ) )
	instrument = ins.Instrument( "Triangle" )
	instrument.jouer()

	print( banner( 'Piano :: "Yamaha", 4', GRN ) )
	piano = ins.Piano( "Yamaha", 4 )
	piano.jouer()

	print( banner( 'Batterie :: "Pearl", False', GRN ) )
	batterie = ins.Batterie( "Pearl", False )
	batterie.jouer()

	print( banner( 'Batterie :: "Roland", True', GRN ) )
	batterie = ins.Batterie( "Roland", True )
	batterie.jouer()

# ------------------------------------------------------------------------------
def test_porte():
	print( test_title( "TEST_PORTE" ) )
	
	print( banner( 'Porte', GRN ) )
	porte = por.Porte()
	porte.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte.ouvrir()
	porte.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte.ouvrir()
	porte.afficher_etat()
	print( banner( 'fermer()' ) )
	porte.fermer()
	porte.afficher_etat()
	print( banner( 'fermer()' ) )
	porte.fermer()
	porte.afficher_etat()

	print( banner( 'PorteCode( "12345" )', GRN ) )
	porte_code = por.PorteCode( "12345" )
	porte_code.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte_code.ouvrir()
	porte_code.afficher_etat()
	print( banner( 'ouvrir_avec_code( "12344" )' ) )
	porte_code.ouvrir_avec_code( "12344" )
	porte_code.afficher_etat()
	print( banner( 'ouvrir_avec_code( "12345" )' ) )
	porte_code.ouvrir_avec_code( "12345" )
	porte_code.afficher_etat()
	print( banner( 'fermer()' ) )
	porte_code.fermer()
	porte_code.afficher_etat()

	print( banner( 'PorteVerrou', GRN ) )
	porte_verrou = por.PorteVerrou()
	porte_verrou.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte_verrou.ouvrir()
	porte_verrou.afficher_etat()
	print( banner( 'deverouiller() + ouvrir()' ) )
	porte_verrou.deverouiller()
	porte_verrou.ouvrir()
	porte_verrou.afficher_etat()
	print( banner( 'fermer()' ) )
	porte_verrou.fermer()
	porte_verrou.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte_verrou.ouvrir()
	porte_verrou.afficher_etat()
	print( banner( 'fermer() + verrouiller()' ) )
	porte_verrou.fermer()
	porte_verrou.verrouiller()
	porte_verrou.afficher_etat()
	print( banner( 'ouvrir()' ) )
	porte_verrou.ouvrir()
	porte_verrou.afficher_etat()

# --------------------------------------------------------------------- [ MAIN ]

def main():
	test_utils()
	test_media()
	test_instrument()
	test_porte()

if __name__ == "__main__":
    main()
