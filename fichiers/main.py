import RecipeCalculator as rc
from os import path

# ---------------------------------------------------------------------- [ DOC ]

# https://stackoverflow.com/questions/595305/how-do-i-get-the-path-of-the-python-script-i-am-running-in
# https://www.geeksforgeeks.org/python/__file__-a-special-variable-in-python/

# -------------------------------------------------------------------- [ FILES ]

PRICE_FILENAME = "Prix.txt"
RECIPE_FILENAME = "Recette.txt"

# --------------------------------------------------------------------- [ MAIN ]

def main():
	current_dir = ( path.dirname( __file__ ) )
	prix_abspath = f"{current_dir}\\{PRICE_FILENAME}"
	recipe_abspath = f"{current_dir}\\{RECIPE_FILENAME}"

	rc.RecipeCalculator( prix_abspath, recipe_abspath )	

if __name__ == "__main__":
	main()
