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
	print( "------Validation of User Names------" )
	for name in user_names:
		Regex.RegularExpression.validate_user_name( name )
	print( "------------------------------------\n" )
		
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
	print( "------Validation of Phones------" )
	for num in phones:
		Regex.RegularExpression.validate_phone( num )
	print( "------------------------------------\n" )

	birth_dates = [
		'01/07/1990',
		'1992-12-05',
		'05-13-1985',
		'July 8th',
		'1988/07/15',
		'15 aoÃ»t 1991',
		'07.07.1987',
		'1986-06-06',
		'06/06/1986',
		'1984-01-01',
		'1985/05/05',
		'1983-11-30',
		'1990-30-12',
		'1993.12.12',
		'1992/01/01',
		'01-01-1991',
		'02/14/1988',
		'1980-02-29',
		'07/07/77',
		'31/02/1984'
	]
	print( "------Validation of Birth Dates------" )
	for date in birth_dates:
		Regex.RegularExpression.validate_birth_date( date )
	print( "------------------------------------\n" )

	postal_codes = [
		'H2X 1Z1',
		'H2Y1Z2',
		'H3Z-9Y9',
		' 1980',
		'H3Z 2X2',
		'H2Y1A1',
		'H1Z-2K2',
		'H2X1A1',
		'H4X 1A3',
		'h1x 2y2',
		'H2X-2X2',
		'H0H0H0',
		'H3Z 1Z9',
		'h2z1x1',
		'H2W 1B2',
		'H4A1A1',
		'H2Y 2Z3',
		'h1z 3x3',
		'H3H 3H3',
		'H2Z 2Z2'
	]
	print( "------Validation of Postal Codes------" )
	for code in postal_codes:
		Regex.RegularExpression.validate_postal_code( code )
	print( "------------------------------------\n" )

	user_ids = [
		'CLT-001,',
		'CLT-002,',
		'CLT_003,',
		'h3x1w4',
		'CLT-005',
		'CLT-006',
		'CLT-007',
		'CLT-008',
		'CLT-009',
		'CLT-010',
		'CLT-011',
		'CLT-012',
		'CLT-013',
		'CLT-014',
		'CLT-015',
		'CLT-016',
		'CLT-017',
		'CLT-018',
		'CLT-019',
		'CLT-020'
	]
	print( "------Validation of User Ids------" )
	for id in user_ids:
		Regex.RegularExpression.validate_user_id( id )
	print( "------------------------------------\n" )
		
if __name__ == "__main__":
	main()
