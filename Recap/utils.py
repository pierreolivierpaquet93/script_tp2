def repeter_mot(
	mot: str,
	n: int
) -> None:
	while n > 0:
		print( mot )
		n -= 1
	return

def somme_liste( numbers: list[int] ) -> int:
	sum = 0
	for number in numbers:
		sum += number
	return sum

def separe_text(
	texte: str,
	sep: str
) -> tuple[str,str]:
	return texte.split( sep, 1 )
