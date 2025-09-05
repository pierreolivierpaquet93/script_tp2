import Regex

def main():
	"""
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

	phones = [
		'5141234567',
		'(514) 555-1234',
		'514.555.7890',
		'',
		'438 123 4567',
		'514-333-6789',
		'1234567890',
		'514 999 1234',
		'(514)5551234',
		'514/321/7890',
		'514*123*1234',
		'4385559999',
		'514 222 1111',
		'514.222.3333',
		'(438)123-4567',
		'514123456789',
		'438-321-4567',
		'514.444.0000',
		'514123-7890',
		'5141231234'
	]
	print("------Validation of Phones------")
	for num in phones:
		Regex.RegularExpression.validate_phone( num )
	"""


if __name__ == "__main__":
	main()