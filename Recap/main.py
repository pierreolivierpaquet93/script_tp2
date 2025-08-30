import utils as ut

# ------------------------------------------------------------------------------

def test_utils():
	ut.repeter_mot( "Bonjour", 0)
	ut.repeter_mot( "Impossible", -1 )
	ut.repeter_mot( "Répéter", 3 )
	
	numbers: list[int] = [-1, 2, 3, 4]
	print( ut.somme_liste( numbers ) )

	test_tuple = ut.separe_text( "LeftHandSide:RightHandSide:test", ":" )
	print( test_tuple[0] )
	print( test_tuple[1] )

# --------------------------------------------------------------------- [ MAIN ]

def main():
	test_utils()

if __name__ == "__main__":
    main()
