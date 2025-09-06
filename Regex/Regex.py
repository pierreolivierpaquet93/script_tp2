import re

# ---------------------------------------------------------------------- [ DOC ]

# https://stackoverflow.com/questions/1034573/most-idiomatic-way-to-convert-none-to-empty-string
# https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/postal-codes.page

# ------------------------------------------------------------------------------

def nonestr( validate: str ) -> str:
	if validate is None:
		return ""
	else:
		return validate

class RegularExpression:
	@staticmethod
	def validate_user_name( user_name: str ) -> None:
		err_invalid_name = '[Invalid Name]'

		open_quote =	r"^[\"]?"
		grp_first =		r"(?P<first>[a-zA-Z]+-?[a-zA-Z]*)"
		sep =			r"[ .-;]"
		grp_second =	r"(?P<second>[a-zA-Z]+)"
		closing_quote =	r"[\"]?$"
		pattern =		(fr"{open_quote}{grp_first}{sep}" +
			f"{grp_second}{closing_quote}")

		matches = re.match( pattern, user_name )
		
		if matches:
			print( f"Name First={matches.group("first")} - " +
		 		f"Second={matches.group("second")}" )
		else:
			print( err_invalid_name )

	@staticmethod
	def validate_phone( phone: str ) -> None:
		err_invalid_phone = '[Invalid Phone Number]'
		
		open_paren =	r"\(?"
		area_code =		r"\d{3}"
		close_paren =	r"\)?"
		grp_area =		fr"{open_paren}(?P<area>{area_code}){close_paren}"
		prefix =		r"\d{3}"
		grp_prefix =	fr"(?P<prefix>{prefix})"
		line =			r"\d{4}"
		grp_line =		fr"(?P<line>{line})"
		sep =			r"[ .\-/]?"
		pattern =		fr"^{grp_area}{sep}{grp_prefix}{sep}{grp_line}$"

		matches = re.match( pattern, phone )
		if matches:
			print(
				f"Phone Number Region={matches.group("area")} " +
				f"Number={matches.group("prefix")}-{matches.group("line")}" )
		else:
			print( err_invalid_phone )

	@staticmethod
	def validate_birth_date( birth_date: str ) -> None:
		err_invalid_birth_date = '[Invalid Birth Date]'
		
		# Format 1 -> "jj/mm/yyyy"
		f1_sep =	r"/"
		f1_day =	r"(?P<f1_day>\d{2})"
		f1_month =	r"(?P<f1_month>\d{2})"
		f1_year =	r"(?P<f1_year>\d{4})"
		f1 =		fr"(^{f1_day}{f1_sep}{f1_month}{f1_sep}{f1_year}$)"

		# Format 2 -> "yyyy-mm-jj"
		f2_sep =	r"\-"
		f2_year =	r"(?P<f2_year>\d{4})"
		f2_month =	r"(?P<f2_month>\d{2})"
		f2_day =	r"(?P<f2_day>\d{2})"
		f2 =		fr"(^{f2_year}{f2_sep}{f2_month}{f2_sep}{f2_day}$)"

		# Format 3 -> "yyyy.jj.mm"
		f3_sep =	r"\."
		f3_year =	r"(?P<f3_year>\d{4})"
		f3_day =	r"(?P<f3_day>\d{2})"
		f3_month =	r"(?P<f3_month>\d{2})"
		f3 =		fr"(^{f3_year}{f3_sep}{f3_day}{f3_sep}{f3_month}$)"

		pattern = fr"{f1}|{f2}|{f3}"

		matches = re.match(pattern, birth_date)

		if matches:
			year = str(
				matches.group( "f1_year" ) or
				matches.group( "f2_year" ) or 
				matches.group( "f3_year" )
			)
			month = str(
				matches.group( "f1_month" ) or
				matches.group( "f2_month" ) or
				matches.group( "f3_month" )
			)
			day = str(
				matches.group( "f1_day" ) or
				matches.group( "f2_day" ) or
				matches.group( "f3_day" )
			)
			print( f"Birth Date Year={year} Month={month} Day={day}" )
		else:
			print( err_invalid_birth_date )

	@staticmethod
	def validate_postal_code( postal_code: str ) -> None:
		err_invalid_postal_code = '[Invalid Postal Code]'

		fsa = r"(?P<fsa>[a-zA-Z][\d][a-zA-Z])"
		sep = r"[ \-]?"
		ldu = r"(?P<ldu>[\d][a-zA-Z][\d])"

		pattern = fr"^{fsa}{sep}{ldu}$"

		matches = re.match( pattern, postal_code )

		if matches:
			lhs = matches.group( "fsa" ).upper()
			rhs = matches.group( "ldu" ).upper()
			print( f"Postal Code = {lhs} {rhs}" )
		else:
			print( err_invalid_postal_code )


	@staticmethod
	def validate_user_id( user_id: str ) -> None:
		err_invalid_user_id = '[Invalid User Id]'

		prefix =	r"(?P<prefix>CLT\-)"
		uid =		r"(?P<id>\d{3})"

		pattern = fr"^{prefix}{uid}"

		matches = re.match( pattern, user_id )

		if matches:
			user = matches.group( "id" )
			print( f"User Id = {user}" )
		else:
			print( err_invalid_user_id )