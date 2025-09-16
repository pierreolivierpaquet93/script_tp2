import os
import json
import csv
import xml.etree.ElementTree as ET 

JSON_FILENAME = "InputComputers.json"
XML_FILENAME = "InputComputers.xml"

BLU = "\033[1;34m"
RST = "\033[0m"

FIELD_NAME = "Name"
FIELD_MODEL = "Model"
FIELD_CPU = "CPU"
FIELD_RAM = "RAM_GB"

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

class Enonce():
	def __init__(
		self,
		my_json: MyJson = None,
		my_xml: MyXml = None
	):
		self._computers: list[Computer] = []
		self.AddFromJson( my_json )
		self.AddFromXml( my_xml )
	
	def AddFromXml(
		self,
		my_xml: MyXml
	):
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
		my_json: MyJson
	):
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

def main():
	path = os.path.dirname(__file__)+'\\'
	a = MyJson( path+JSON_FILENAME )
	b = MyXml( path+XML_FILENAME )
	Enonce(a, b)

if __name__ == "__main__":
	main()
