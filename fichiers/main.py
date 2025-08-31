import RecipeCalculator as rc
from os import path

# https://stackoverflow.com/questions/595305/how-do-i-get-the-path-of-the-python-script-i-am-running-in

# -------------------------------------------------------------------- [ FILES ]

PRICE_FILENAME = "Prix.txt"
RECIPE_FILENAME = "Recette.txt"

# --------------------------------------------------------------------- [ MAIN ]

def main():

	current_dir = ( path.dirname( __file__ ) )
	prix_abspath = f"{current_dir}\\{PRICE_FILENAME}"
	recipe_abspath = f"{current_dir}\\{RECIPE_FILENAME}"

	test = rc.RecipeCalculator( prix_abspath, recipe_abspath )	

if __name__ == "__main__":
	main()