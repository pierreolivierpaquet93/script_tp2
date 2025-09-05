import Regex

def main():
	user_names=[
		'"Tremblay Jean"',
		'Sophie LÃ©vesque',
		'Dupont Marc',
		'@Luc Parent',
		'Lavoie;Catherine',
		'Nadia GagnÃ©',
		'Marc-AndrÃ©_Benoit',
		'GeneviÃ¨ve.Dionne',
		'"Boucher Alain"',
		'Roxanne.Larose',
		'"Dupuis Sophie"',
		'HervÃ© Morin',
		'FÃ©lix Tremblay',
		'Julie Moreau',
		'Alexandre Gagnon',
		'Lalonde Claude',
		'Couture Ã‰lise',
		'Annie Therrien',
		'GÃ©rard NoÃ«l',
		'Marie-Claude.Nantel'
	]

	print("------Validation of User Names------")
	for name in user_names:
		Regex.RegularExpression.validate_user_name( name )

if __name__ == "__main__":
	main()