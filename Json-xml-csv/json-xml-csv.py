import os
import json
import csv
import xml.etree.ElementTree as ET 

# ----------------------------------------------------------------[ CONSTANT.S ]

EXT_JSON = ".json"
EXT_XML = ".xml"
EXT_CSV = ".csv"

INPUT_FILENAME = "InputComputers"
INPUT_JSON = f"{INPUT_FILENAME}{EXT_JSON}"
INPUT_XML = f"{INPUT_FILENAME}{EXT_XML}"

OUTPUT_FILENAME = "OutputComputers"
OUTPUT_JSON = f"{OUTPUT_FILENAME}{EXT_JSON}"
OUTPUT_XML = f"{OUTPUT_FILENAME}{EXT_XML}"
OUTPUT_CSV = f"{OUTPUT_FILENAME}{EXT_CSV}"

BLU = "\033[1;34m"
RST = "\033[0m"

FIELD_NAME = "Name"
FIELD_MODEL = "Model"
FIELD_CPU = "CPU"
FIELD_RAM = "RAM_GB"

# ------------------------------------------------------------------[ CLASSE.S ]

# -------------------------------------------------------------[ Computer ]-----

class Computer():
	def __init__(
        self,
        name: str,
        model: str,
        cpu: str,
        ram: int
    ):
		self._name: str = name
		self._model: str = model
		self._cpu: str = cpu
		self._ram: int = ram

	def GetName( self ) -> str:
		return self._name
	
	def GetModel( self ) -> str:
		return self._model
	
	def GetCpu( self ) -> str:
		return self._cpu
	
	def GetRam( self ) -> int:
		return self._ram
 
# ---------------------------------------------------------------[ MyJson ]-----

class MyJson():
	def __init__(
		self,
		filepath: str
	):
		self._filepath: str = filepath
		self._raw_content: str = ""
		self._parsed = None
		if os.path.exists( filepath ):
			with open( filepath, 'r' ) as f:
				self._raw_content: str = f.read()
				self._parsed = json.loads( self._raw_content )

	def GetParsed( self ):
		return self._parsed

# ----------------------------------------------------------------[ MyXml ]-----

class MyXml():
	def __init__(
		self,
		filepath: str
	):
		self._filepath: str = filepath
		self._raw_content: str = ""
		self._root = None
		if os.path.exists( filepath ):
			with open( filepath, 'r' ) as f:
				self._raw_content = f.read()
				self._root = ET.fromstring( self._raw_content )

	def GetRoot( self ):
		return self._root

# ---------------------------------------------------------------[ Enonce ]-----

class Enonce():
	def __init__(
		self,
		my_json: MyJson = None,
		my_xml: MyXml = None
	):
		self._path = os.path.dirname( __file__ ) + '\\'
		self._computers: list[Computer] = []
		self.AddFromJson( my_json )
		self.AddFromXml( my_xml )
	
	def AddFromXml(
		self,
		my_xml: MyXml = None
	):
		if my_xml is None:
			return
		for new_computer in my_xml.GetRoot().findall( "Computer" ):
			name = new_computer.find( FIELD_NAME ).text
			model = new_computer.find( FIELD_MODEL ).text
			cpu = new_computer.find( FIELD_CPU ).text
			ram = new_computer.find( FIELD_RAM ).text
			tmp = Computer(
				name,
				model,
				cpu,
				ram
			)
			self._computers.append( tmp )

	def AddFromJson(
		self,
		my_json: MyJson = None
	):
		if my_json is None:
			return
		for new_computer in my_json.GetParsed():
			name = new_computer[FIELD_NAME]
			model = new_computer[FIELD_MODEL]
			cpu = new_computer[FIELD_CPU]
			ram = new_computer[FIELD_RAM]
			tmp = Computer(
				name,
				model,
				cpu,
				ram
			)
			self._computers.append( tmp )

	def OutputJson( self ):
		computer_lst: list[dict] = []
		for computer in self._computers:
			computer_dict = {
				f"{FIELD_NAME}" : f"{computer.GetName()}",
				f"{FIELD_MODEL}" : f"{computer.GetModel()}",
				f"{FIELD_CPU}" : f"{computer.GetCpu()}",
				f"{FIELD_RAM}" : int(computer.GetRam())
			}
			computer_lst.append( computer_dict )
		with open( self._path + OUTPUT_JSON, 'w' ) as f:
			computer_json_str = json.dump( computer_lst, f, indent=4 )

	def OutputXml( self ):
		root_computers = ET.Element( "Computers" )
		for computer in self._computers:
			sub_computer = ET.SubElement( root_computers, "Computer" )
			sub_computer_name = ET.SubElement( sub_computer, FIELD_NAME )
			sub_computer_name.text = computer.GetName()
			sub_computer_model = ET.SubElement( sub_computer, FIELD_MODEL )
			sub_computer_model.text = computer.GetModel()
			sub_computer_cpu = ET.SubElement( sub_computer, FIELD_CPU )
			sub_computer_cpu.text = computer.GetCpu()
			sub_computer_ram = ET.SubElement( sub_computer, FIELD_RAM )
			sub_computer_ram.text = str(computer.GetRam())
			ET.indent( root_computers )
			tree_computers = ET.ElementTree( root_computers )
			tree_computers.write(
				self._path + OUTPUT_XML,
				encoding="utf-8",
				xml_declaration=True
			)

	def OutputCsv( self ):
		pass

# ----------------------------------------------------------------------[ MAIN ]

def main():
	path = os.path.dirname(__file__) + '\\'
	input_json = MyJson( path + INPUT_JSON )
	input_xml = MyXml( path + INPUT_XML )
	travail_pratique = Enonce(
		input_json,
		input_xml
	)
	travail_pratique.OutputJson()
	travail_pratique.OutputXml()

if __name__ == "__main__":
	main()
