import re

class RegularExpression:
	@staticmethod
	def validate_user_name( user_name ):
		ERR_INVALID_NAME = "[Invalid Name]"

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
			print( ERR_INVALID_NAME )
