import re

class RegularExpression:
	@staticmethod
	def validate_user_name( user_name: str ) -> None:
		err_invalid_name = "[Invalid Name]"

		open_quote = "^[\"]?"
		grp_first = "(?P<first>[a-zA-Z]+-?[a-zA-Z]*)"
		sep = "[ .-;]"
		grp_second = "(?P<second>[a-zA-Z]+)"
		closing_quote = "[\"]?$"
		pattern = fr"{open_quote}{grp_first}{sep}{grp_second}{closing_quote}"
		matches = re.match( pattern, user_name )
		
		if matches:
			print( f"Name First={matches.group("first")} - " +
		 		f"Second={matches.group("second")}" )
		else:
			print( err_invalid_name )

	@staticmethod
	def validate_phone( phone: str ) -> None:
		err_invalid_phone = "[Invalid Phone Number]"
		
		open_paren = "\(?"
		area_code = "\d{3}"
		close_paren = "\)?"
		grp_area = f"{open_paren}(?P<area>{area_code}){close_paren}"
		prefix = "\d{3}"
		grp_prefix = f"(?P<prefix>{prefix})"
		line = "\d{4}"
		grp_line = f"(?P<line>{line})"
		sep = "[ .\-/]?"
		pattern = (fr"^{grp_area}{sep}{grp_prefix}{sep}{grp_line}$")

		matches = re.match( pattern, phone )
		if matches:
			print(
				f"Phone Number Region={matches.group("area")} " +
				f"Number={matches.group("prefix")}-{matches.group("line")}" )
		else:
			print( err_invalid_phone )

	@staticmethod
	def validate_birth_date( birth_date: str ) -> None:
		pass
