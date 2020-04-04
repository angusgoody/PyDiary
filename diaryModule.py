
"""
PyDiary 1.0
Angus Goody
01/04/20

Diary Module
Contains Diary Classes
"""

# =========IMPORTS==========
from datetime import date
from datetime import datetime

# =========FUNCTIONS==========

# =========CLASSES==========

class diary:
	"""
	The diary object is where
	all the user diary entries
	and stored along with user
	settings
	"""
	def __init__(self,name):
		self.name=name
		self.hint=None
		#Store viewing information
		self.font="Helvetica"
		self.fontSize="13"
		self.darkMode=False
		#Store Content
		self.entryList=[]

	def addEntry(self,title):
		"""
		Will add an entry
		to the diary
		"""
		#Create the object
		newEntryObject=diaryEntry(self,title)
		#Add to array
		self.entryList.append(newEntryObject)
		#Return
		return newEntryObject


class diaryEntry:
	"""
	The diaryEntry stores
	all the data for a specific diary entry
	"""
	def __init__(self,master,title):
		self.master=master
		self.title = title
		self.dateCreated=str(date.today())
		self.timeCreated=datetime.now().strftime("%H:%M")
		self.content=""


