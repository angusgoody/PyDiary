"""
PyDiary 1.0
Angus Goody
01/04/20
"""

# =========Imports==========
from shed.tkinterTools import *
from shed.storageTools import *
# =========Classes==========

# =========Main Program==========
class PyDiary(Tk):
	"""
	The PyDiary window class
	"""
	def __init__(self):
		Tk.__init__(self)
		#Setup
		self.title("PyDiary")
		self.geometry("600x500")
		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)
		self.screenMaster=screenController(self)
		self.screenMaster.grid(row=0,column=0)
		#Project Manager
		self.projectManager=projectManager(getWorkingDirectory(),"PyDiary")
		self.projectManager.fileExtension=".pdy"





#Final Call
if __name__ == '__main__':
	window=PyDiary()
	window.mainloop()

