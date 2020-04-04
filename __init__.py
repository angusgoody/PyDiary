"""
PyDiary 1.0
Angus Goody
01/04/20
"""

# =========IMPORTS==========
from shed.tkinterTools import *
from shed.storageTools import *
from diaryModule import *

globalOffWhiteColour="#f2f2f2"
globalRedColour="#f09892"
globalGreenColour="#c1e3ca"

globalFontList=["Arial","Avenir","Times","Courier","Helvetica","Verdana","Comic Sans MS"]

# =========SCREENS==========
class openScreen(screen):
	"""
	Screen where user selects
	which diary file to open
	"""
	def __init__(self,controller):
		screen.__init__(self,controller,"Open")
		self.grid_rowconfigure(1,weight=1)
		self.grid_columnconfigure(0,weight=1)
		#Configure sections
		self.topBar=mainFrame(self)
		self.topBar.grid(row=0,column=0,sticky="EW")
		self.mainContent = mainFrame(self)
		self.mainContent.grid(row=1,column=0,sticky="NSEW")
		self.buttonSection=buttonSection(self)
		self.buttonSection.grid(row=2, column=0, sticky="EW")
		#Top Bar
		self.topBar.grid_columnconfigure(0,weight=1)
		self.topTitle=titleLabel(self.topBar,text="Select Diary")
		self.topTitle.grid(row=0,column=0)
		#Listbox
		self.mainContent.gridConfig(0)
		self.openListbox=advancedListbox(self.mainContent)
		self.openListbox.configure(borderwidth=0, highlightthickness=0)
		self.openListbox.grid(row=0,column=0,sticky="NSEW")
		#Buttons
		self.buttonSection.addButton("Create")
		self.buttonSection.addButton("Open")
		#Colour
		self.buttonSection.colour(globalOffWhiteColour)

class unlockScreen(screen):
	"""
	Screen where user enters
	the password to unlock a diary file
	"""
	def __init__(self,controller):
		screen.__init__(self,controller,"Unlock")

class viewDiaryEntryScreen(screen):
	"""
	Screen where user
	can view and edit diary contents
	"""
	def __init__(self,controller):
		screen.__init__(self,controller,"Diary Entry")
		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(2,weight=1)
		# Configure sections
		self.titleBar = mainFrame(self)
		self.titleBar.grid(row=0, column=0, sticky="EW")
		self.titleBar.grid_columnconfigure(0,weight=1)
		self.titleBar.grid_columnconfigure(1,weight=1)
		self.titleBar.grid_columnconfigure(2,weight=1)
		self.titleLeftSide=mainFrame(self.titleBar)
		self.titleLeftSide.grid(row=0,column=0,sticky="EW",pady=10)
		self.titleMiddle=mainFrame(self.titleBar)
		self.titleMiddle.grid(row=0,column=1,sticky="EW",pady=10)
		self.titleRightSide=mainFrame(self.titleBar)
		self.titleRightSide.grid(row=0,column=2,sticky="EW",pady=10)

		self.toolBar=mainFrame(self)
		self.toolBar.grid(row=1,column=0,sticky="EW")
		self.toolBar.gridConfig(0)
		self.toolBarMiddle=mainFrame(self.toolBar)
		self.toolBarMiddle.grid(row=0,column=0,pady=10)

		self.mainContent = mainFrame(self)
		self.mainContent.grid(row=2, column=0, sticky="NSEW")

		self.statusBar = mainFrame(self)

		self.buttonSection = buttonSection(self)
		self.buttonSection.grid(row=4, column=0, sticky="EW")
		#Title Bar
		#Left Side
		self.titleLeftSide.gridConfig(0)
		self.currentDiaryName=StringVar()
		self.currentDiaryName.set("My Diary - Entry #1")
		self.titleLabel=advancedLabel(self.titleLeftSide,textvariable=self.currentDiaryName)
		self.titleLabel.config(font=globalFont)
		self.titleLabel.grid(row=0,column=0)
		#Middle Side
		self.titleMiddle.gridConfig(0)
		self.dateVar=StringVar()
		self.dateVar.set("Date Created: 16/07/12")
		self.dateLabel=advancedLabel(self.titleMiddle,textvariable=self.dateVar)
		self.dateLabel.config(font=globalFontTiny)
		self.dateLabel.grid(row=0,column=0)
		#Right Side
		self.titleRightSide.gridConfig(0)
		self.wordCountVar=StringVar()
		self.wordCountVar.set("Word Count: 120")
		self.wordCountLabel=advancedLabel(self.titleRightSide,textvariable=self.wordCountVar)
		self.wordCountLabel.config(font=globalFontTiny,width=20)
		self.wordCountLabel.grid(row=0,column=0)
		#Tool Bar
		#todo create custom class with bold font option
		self.fontPickerVar=StringVar()
		self.fontPickerVar.set("Arial")
		#todo ammend colour function for optionMenu
		self.fontPicker=ttk.OptionMenu(self.toolBarMiddle, self.fontPickerVar, globalFontList[0],
									   *globalFontList,command=lambda value: self.updateTextWidget() )
		self.fontPicker.configure(width=12)
		self.fontPicker.grid(row=0,column=0)
		self.fontSizeVar=StringVar()
		self.fontSizeVar.set("13")
		self.fontSizeOptions=[5,6,7,8,9,10,11,12,13,14,15,16,18,20,22]
		self.fontSizePicker=ttk.OptionMenu(self.toolBarMiddle, self.fontSizeVar, self.fontSizeOptions[0],
										   *self.fontSizeOptions,command=lambda value: self.updateTextWidget() )
		self.fontSizePicker.configure(width=12)
		self.fontSizePicker.grid(row=0,column=1)
		#Main Content
		self.mainContent.gridConfig(0)
		self.textArea=Text(self.mainContent)
		self.textArea.configure(borderwidth=0, highlightthickness=0,padx=20,pady=30)
		self.textArea.config(wrap=WORD)
		self.textArea.grid(row=0,column=0,sticky="NSEW")
		#Status Bar
		self.statusBar.gridConfig(0)
		self.statusVar=StringVar()
		self.statusLabel=advancedLabel(self.statusBar,textvariable=self.statusVar)
		self.statusLabel.grid(row=0,column=0)
		#Button Bar
		self.buttonSection.addButton("Close")
		self.buttonSection.addButton("Save")
		#Colour
		self.buttonSection.colour(globalOffWhiteColour)
		self.titleBar.colour(globalOffWhiteColour)
		self.toolBar.colour(globalOffWhiteColour)
		#Bindings
		self.textArea.bind("<KeyRelease>",lambda event: self.updateWordCount())

	def showGoodStatus(self,message):
		"""
		Will show the status bar
		with a green background
		"""
		self.statusBar.grid(row=3, column=0, sticky="EW")
		self.statusVar.set(message)
		self.statusBar.colour(globalGreenColour)

	def showStatus(self,message):
		"""
		Will show the status
		bar with a red background
		"""
		#todo create a status class
		self.statusBar.grid(row=3, column=0, sticky="EW")
		self.statusVar.set(message)
		self.statusBar.colour(globalRedColour)

	def hideStatus(self):
		"""
		Hide the status bar
		"""
		self.statusBar.grid_forget()

	def updateWordCount(self):
		"""
		Will calculate word count
		"""
		content=self.textArea.get("1.0",END)
		wordCount=len(content.split())
		self.wordCountVar.set("Word Count: "+str(wordCount))

	def updateTextWidget(self):
		"""
		Will update the text widget
		ie, change fonts etc
		"""
		#Get Data
		font=self.fontPickerVar.get()
		fontSize=self.fontSizeVar.get()
		#Update
		self.textArea.configure(font=(font,fontSize))
		#Save
		self.master.masterWindow.quickSaveEntryMetaData()

class viewDiaryScreen(screen):
	"""
	Screen where user
	can view and edit diary contents
	"""
	def __init__(self,controller):
		screen.__init__(self,controller,"Diary")
		#Variables
		self.buttonHidden=True
		#Config
		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(3,weight=1)
		#Configure
		self.topBar=mainFrame(self)
		self.topBar.grid(row=0,column=0)
		self.searchFrame=mainFrame(self)
		self.searchFrame.grid(row=1,column=0,sticky="EW")
		# Seperator
		self.sep = ttk.Separator(self,orient=HORIZONTAL)
		self.sep.grid(row=2,column=0,sticky="EW")

		self.mainContent=mainFrame(self)
		self.mainContent.grid(row=3,column=0,sticky="NSEW")
		self.buttonFrame=mainFrame(self)
		self.buttonFrame.grid(row=4, column=0,sticky="EW")
		self.buttonFrame.grid_columnconfigure(0,weight=1)
		self.buttonFrame.grid_columnconfigure(1, weight=1)
		self.leftButtonSection=buttonSection(self.buttonFrame)
		self.leftButtonSection.grid(row=0,column=0,sticky="EW",padx=20)
		self.rightButtonSection=buttonSection(self.buttonFrame)
		self.rightButtonSection.grid(row=0,column=1,sticky="EW",padx=20)
		#Title
		self.topBar.gridConfig(0)
		self.topLabelVar=StringVar()
		self.topLabelVar.set("Diary - Entries")
		self.titleLabel=titleLabel(self.topBar,textvariable=self.topLabelVar)
		self.titleLabel.grid(row=0,column=0)
		#Search Frame
		self.searchFrame.grid_columnconfigure(0,weight=1)
		self.searchBar=advancedEntry(self.searchFrame) #todo add placeholder to advancedEntry class
		self.searchBar.grid(row=0,column=0,sticky="EW",pady=10,padx=10)
		self.resetButton=Button(self.searchFrame,text="Reset")
		self.resetButton.config(width=7)
		#self.resetButton.grid(row=0,column=1,padx=(0,10))

		#Main
		self.mainContent.gridConfig(0)
		self.diaryEntryListbox=advancedListbox(self.mainContent)
		self.diaryEntryListbox.configure(borderwidth=0, highlightthickness=0)
		self.diaryEntryListbox.grid(row=0,column=0,sticky="NSEW")
		#Buttons
		self.rightButtonSection.addButton("Delete")
		self.rightButtonSection.addButton("Open")
		self.leftButtonSection.addButton("Close")
		self.leftButtonSection.addButton("Create")
		#Colour
		self.buttonFrame.colour("#d6d5eb")
		#Bindings
		self.searchBar.bind("<KeyRelease>",lambda event: self.master.masterWindow.runEntrySearch())

	def showResetButton(self):
		"""
		Show the reset button
		next to the search bar
		"""
		if self.buttonHidden:
			self.resetButton.grid(row=0, column=1, padx=(0, 10))
			self.buttonHidden=False

	def hideResetButton(self):
		self.resetButton.grid_forget()
		self.buttonHidden=True


# =========TOP LEVELS==========

class createDiaryFileWindow(mainTopLevel):
	"""
	A popup window
	that will allow the user
	to create a new diary file
	"""
	def __init__(self,windowInstance):
		mainTopLevel.__init__(self,windowInstance,"Create Diary")
		# Config
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		# Center
		self.centerFrame = mainFrame(self)
		self.centerFrame.grid(row=0, column=0)
		# Add data sections
		self.diaryNameSection = dataSection(self.centerFrame, "Diary Name: ")
		self.diaryNameSection.grid(row=0, column=0,pady=20)
		self.passwordSection = hiddenDataSection(self.centerFrame,"Password: ")
		self.passwordSection.grid(row=1, column=0,pady=7)
		self.confirmPasswordSection = hiddenDataSection(self.centerFrame, "Confirm: ")
		self.confirmPasswordSection.grid(row=2, column=0)
		self.hintSection=dataSection(self.centerFrame,"Hint: ")
		self.hintSection.grid(row=3,column=0,pady=20)
		# Add Status Bar
		self.statusBar=mainFrame(self)
		self.statusBar.gridConfig(0)
		self.statusVar=StringVar()
		self.statusVar.set("Hello world")
		self.statusLabel=advancedLabel(self.statusBar,textvariable=self.statusVar)
		self.statusLabel.grid(row=0,column=0)
		# Add Button Bar
		self.buttonBar = buttonSection(self)
		self.buttonBar.grid(row=2, column=0,sticky="EW")
		self.buttonBar.addButton("Cancel")
		self.buttonBar.addButton("Save")
		#Colour
		self.statusBar.colour(globalRedColour)
		self.buttonBar.colour("#dde4eb")
		# Add exit button command
		self.buttonBar.getButton("Cancel").config(command=self.quit)

	def hideStatus(self):
		"""
		Will hide the status bar
		"""
		self.statusBar.grid_forget()

	def showStatus(self,message):
		"""
		Will show the status bar
		and display a message
		"""
		self.statusBar.grid(row=1,column=0,sticky=EW)
		self.statusVar.set(message)

	def setup(self):
		"""
		Run an initial setup
		on the window and find any
		banned words etc
		"""
		#Find taken file names
		bannedWords=[]
		allFilenames = self.master.projectManager.findAllUserFiles()
		for item in allFilenames:
			bannedWords.append(getBasename(getFileWithoutExtension(item)))
		#Update the entry
		self.diaryNameSection.entry.bannedWords=bannedWords
		#Add the command
		self.buttonBar.getButton("Save").config(command=lambda: self.master.checkNewDiaryDetails(self))

	def checkPassword(self):
		"""
		Will firstly check a valid password
		has been entered, then check the two passwords
		match
		"""
		userPassword=self.passwordSection.entry.getContent()
		userConfirm=self.confirmPasswordSection.entry.getContent()
		if len(userPassword.split()) > 0:
			if userPassword == userConfirm:
				return userPassword
			else:
				return False
		else:
			return False

class createDiaryEntryWindow(mainTopLevel):
	"""
	A popup window
	that will allow the user
	to create a new diary entry
	"""
	def __init__(self,windowInstance):
		mainTopLevel.__init__(self,windowInstance,"Create Diary Entry")
		# Config
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		# Top Bar
		self.topBar=mainFrame(self)
		self.topBar.grid(row=0,column=0,sticky="EW")
		self.topBar.gridConfig(0)
		# Date
		self.dateVar=StringVar()
		self.dateLabel=advancedLabel(self.topBar,textvariable=self.dateVar)
		self.dateLabel.grid(row=0,column=0,pady=20)
		# Center
		self.centerFrame = mainFrame(self)
		self.centerFrame.grid(row=1, column=0)
		# Data Section
		self.diaryEntryTitle=dataSection(self.centerFrame,"Entry Title: ")
		self.diaryEntryTitle.grid(row=1,column=0)
		# Add Status Bar
		self.statusBar=mainFrame(self)
		self.statusBar.gridConfig(0)
		self.statusVar=StringVar()
		self.statusVar.set("Hello world")
		self.statusLabel=advancedLabel(self.statusBar,textvariable=self.statusVar)
		self.statusLabel.grid(row=0,column=0)
		# Button Section
		self.buttonSection=buttonSection(self)
		self.buttonSection.grid(row=3,column=0,sticky="EW")
		self.buttonSection.addButton("Cancel")
		self.buttonSection.addButton("Save")
		#Colour
		self.statusBar.colour(globalRedColour)
		self.buttonSection.colour("#e4ebdd")
		# Add exit button command
		self.buttonSection.getButton("Cancel").config(command=self.quit)

	def setup(self):
		#Setup Current Date
		self.dateVar.set("Date: "+str(date.today()))
		#Insert Template Name
		masterDiary=self.master.currentDiary
		#Generate name that isn't taken
		entryNumber=1
		if masterDiary:
			allEntries = masterDiary.entryList
			allEntryNames = []
			#Update banned words
			self.diaryEntryTitle.entry.bannedWords=allEntryNames
			# Create a list of titles
			for e in allEntries:
				allEntryNames.append(e.title)
			newEntryName = "Entry #1"
			counter = 2
			while newEntryName in allEntryNames:
				newEntryName = "Entry #" + str(counter)
				counter += 1
			entryNumber = counter - 1
		self.diaryEntryTitle.entry.insert(END,"Entry #"+str(entryNumber))
		#Run a content check after inserting data
		self.diaryEntryTitle.entry.checkContent()
		#Add the command
		self.buttonSection.getButton("Save").config(command=lambda: self.master.checkNewDiaryEntryDetails(self))


	def hideStatus(self):
		"""
		Will hide the status bar
		"""
		self.statusBar.grid_forget()

	def showStatus(self,message):
		"""
		Will show the status bar
		and display a message
		"""
		self.statusBar.grid(row=2,column=0,sticky=EW)
		self.statusVar.set(message)


# =========MAIN PROGRAM==========
class PyDiary(Tk):
	"""
	The PyDiary window class
	"""
	def __init__(self):
		Tk.__init__(self)
		#Setup
		self.title("PyDiary")
		self.geometry("750x500")
		self.grid_rowconfigure(0,weight=1)
		self.grid_columnconfigure(0,weight=1)
		self.screenMaster=screenController(self)
		self.screenMaster.grid(row=0,column=0,sticky="NSEW")
		#Globals
		self.currentDiary=None
		self.currentDiaryEntry=None
		#Project Manager
		self.projectManager=projectManager(getWorkingDirectory(),"PyDiary")
		self.projectManager.fileExtension=".pdy"
		#Reference the screens
		self.openScreen=openScreen(self.screenMaster)
		self.unlockScreen=unlockScreen(self.screenMaster)
		self.viewDiaryEntryScreen=viewDiaryEntryScreen(self.screenMaster)
		self.viewDiaryScreen=viewDiaryScreen(self.screenMaster)
		#Show Call
		self.openScreen.show()

		#======BUTTON COMMANDS======
		#Open Screen
		self.openScreen.buttonSection.getButton("Create").config(command=self.launchCreateDiaryFileWindow)
		self.openScreen.buttonSection.getButton("Open").config(command=self.attemptOpenDiary)
		#ViewDiaryScreen
		self.viewDiaryScreen.leftButtonSection.getButton("Create").config(command=self.launchCreateDiaryEntryWindow)
		self.viewDiaryScreen.leftButtonSection.getButton("Close").config(command=self.loadOpenScreen)
		self.viewDiaryScreen.rightButtonSection.getButton("Open").config(command=self.attemptOpenDiaryEntry)
		self.viewDiaryScreen.rightButtonSection.getButton("Delete").config(command=self.attemptDeleteDiaryEntry)
		self.viewDiaryScreen.resetButton.config(command=self.resetSearch)
		#ViewDiaryEntryScreen
		self.viewDiaryEntryScreen.buttonSection.getButton("Close").config(command=self.exitDiaryEntry)
		self.viewDiaryEntryScreen.buttonSection.getButton("Save").config(command=self.quickSaveEntryData)

		#======Last Calls=====
		self.loadAllUserDatabases()

	def runEntrySearch(self):
		"""
		Called on every keystroke
		of the searchBar
		"""
		#Show reset button
		self.viewDiaryScreen.showResetButton()
		#Get the search term
		searchTerm=self.viewDiaryScreen.searchBar.getContent()
		#Check its valid
		if len(searchTerm.split()) > 0:
			#todo add search for contents and change view
			objectMatches=[]
			if self.currentDiary:
				for e in self.currentDiary.entryList:
					if searchTerm.upper() in str(e.title).upper():
						objectMatches.append(e)
			#Sort List
			objectMatches=sorted(objectMatches,key=lambda x: x.title)
			#Display Results
			self.viewDiaryScreen.diaryEntryListbox.clear()
			for r in objectMatches:
				self.viewDiaryScreen.diaryEntryListbox.addObject(r.title,r)
		else:
			self.resetSearch()

	def resetSearch(self):
		"""
		Called when the user clicks
		"Reset"
		"""
		#Clear search bar
		self.viewDiaryScreen.searchBar.clear()
		#Reset listbox
		self.viewDiaryScreen.diaryEntryListbox.clear()
		if self.currentDiary:
			for e in sorted(self.currentDiary.entryList, key=lambda x: x.title):
				self.viewDiaryScreen.diaryEntryListbox.addObject(e.title, e)
		#Hide the reset button
		self.viewDiaryScreen.hideResetButton()


	def deleteDiaryEntry(self,entryObject):
		"""
		Will remove a diaryEntry from a diary
		"""
		masterDiary=entryObject.master
		#Remove from list
		masterDiary.entryList.remove(entryObject)
		#Save
		self.saveDiary()

	def quickSaveEntryMetaData(self,**kwargs):
		"""
		Will only save font information
		etc
		"""
		displayMessage=kwargs.get("message","Details saved")
		#Save
		self.updateDiaryEntryMetaData()
		# Update status
		self.viewDiaryEntryScreen.showGoodStatus(displayMessage)
		# Wait a few seconds and hide the status bar
		self.waithere(1)
		self.viewDiaryEntryScreen.hideStatus()

	def quickSaveEntryData(self):
		"""
		When the user clicks "Save"
		on the view diaryEntry screen
		"""
		# Save details
		self.updateDiaryEntryData()
		# Update status
		self.viewDiaryEntryScreen.showGoodStatus("Data Saved")
		#Wait a few seconds and hide the status bar
		self.waithere(3)
		self.viewDiaryEntryScreen.hideStatus()

	def waithere(self,seconds):
		"""
		Will wait without the
		ui hanging
		"""
		var = IntVar()
		self.after((seconds*1000), var.set, 1)
		self.wait_variable(var)

	def exitDiaryEntry(self):
		"""
		Called when user clicks
		the "Close" button, will prompt
		user to save and then quit
		"""
		#Check data change
		if self.hasEntryDataChanged():
			#Get user response
			userResponse=askYesNoCancel("Save","Would you like to save before exit?")
			#If response not None then continue
			if userResponse is not None:
				#Change the screen
				self.viewDiaryScreen.show()
				#Save if required
				if userResponse:
					#Save details
					self.updateDiaryEntryData()
		else:
			#Change the screen
			self.viewDiaryScreen.show()

	def hasEntryDataChanged(self):
		"""
		Will check that the user has
		changed any data in the entry
		since the last save
		Return False is no change
		Return True is change
		"""
		if self.currentDiaryEntry:
			entryContent=str(self.currentDiaryEntry.content).rstrip("\n")
			textData=str(self.viewDiaryEntryScreen.textArea.get("1.0",END)).rstrip("\n")
			if entryContent == textData:
				return False
			else:
				return True
		return True

	def updateDiaryEntryData(self):
		"""
		Will save the user data
		to file for the given entry
		"""
		#Get currently opened diary entry
		if self.currentDiaryEntry:
			#Get data from textwidget
			textData=self.viewDiaryEntryScreen.textArea.get("1.0",END).rstrip("\n")
			# Update the class
			self.currentDiaryEntry.content = textData
			# Save the metdata (fonts etc)
			self.updateDiaryEntryMetaData(save=False)
			#Save
			self.saveDiary()

	def updateDiaryEntryMetaData(self,**kwargs):
		"""
		Save to file the metdata for
		the entry, font etc
		"""
		saveToFile=kwargs.get("save",True) #Should it be saved to file yet
		if self.currentDiary:
			# Save font settings
			chosenFont = self.viewDiaryEntryScreen.fontPickerVar.get()
			chosenFontSize = self.viewDiaryEntryScreen.fontSizeVar.get()
			# Update the class
			self.currentDiary.font = chosenFont
			self.currentDiary.fontSize = chosenFontSize
			if saveToFile:
				self.saveDiary()


	def saveDiary(self):
		"""
		Will save to file the current
		contents of the current diary
		object
		"""
		if self.currentDiary:
			self.projectManager.saveUserData(self.currentDiary.name, self.currentDiary)

	def loadOpenScreen(self):
		"""
		Will show the open screen
		and update the listbox
		with correct data
		"""
		#Show
		self.openScreen.show()
		#Load
		self.loadAllUserDatabases()

	def loadAllUserDatabases(self):
		"""
		Will locate user data from file
		and display on screen
		"""
		data = self.projectManager.loadAllUserFiles()
		# Clear the listbox
		self.openScreen.openListbox.clear()
		for name in data:
			obj = data[name]
			# If the file name has been changed externally
			if obj.name != name:
				name = str(name) + " (" + str(obj.name) + ")"
			self.openScreen.openListbox.addObject(name, obj)

	def launchCreateDiaryFileWindow(self):
		"""
		Launches a window
		for the user to create a new diary
		"""
		# Create our new popup
		newWindow = createDiaryFileWindow(self)
		newWindow.setup()
		newWindow.runWindow()

	def launchCreateDiaryEntryWindow(self):
		"""
		Launches a window
		for the user to create a new diary entry
		"""
		# Create our new popup
		newWindow = createDiaryEntryWindow(self)
		newWindow.setup()
		newWindow.runWindow()

	def checkNewDiaryEntryDetails(self,windowObject):
		"""
		Will check to see if the details
		the user entered are valid
		"""
		validOrNot=windowObject.diaryEntryTitle.entry.contentValid
		if not validOrNot:
			reasonInvalid=windowObject.diaryEntryTitle.entry.reasonInvalid
			windowObject.showStatus(reasonInvalid)
			#Make the Entry red
			windowObject.diaryEntryTitle.entry.markInvalid()
		else:
			windowObject.hideStatus()
			#Add the new entry
			if self.currentDiary:
				diaryEntryName=windowObject.diaryEntryTitle.entry.getContent()
				#Add the new entry
				entryObj=self.currentDiary.addEntry(diaryEntryName)
				#Display in listbox
				self.viewDiaryScreen.diaryEntryListbox.addObject(diaryEntryName,entryObj)
				#Save to file
				self.saveDiary()
				#Quit window
				windowObject.quit()

	def checkNewDiaryDetails(self,windowObject):
		"""
		Run when user clicks "Save" on the
		popup window, this function will
		check all the details are valid
		"""
		checkEntryDict={windowObject.diaryNameSection.entry:None,
						windowObject.passwordSection.entry:None,
						windowObject.confirmPasswordSection.entry:None}
		validCount=0
		invalidReason=None
		windowQuit=False #If the toplevel has been quit
		for e in checkEntryDict:
			validOrNot = e.contentValid
			#Save data to dictionary
			checkEntryDict[e]=e.getContent()
			#Check if valid
			if validOrNot:
				validCount+=1
			else:
				#Get the reason for invalid data
				invalidReason=e.reasonInvalid
				#Make the box red
				e.markInvalid()
				break
		#If all the sections have valid content
		if validCount >= len(checkEntryDict):
			#Check the passwords
			userPassword=windowObject.checkPassword()
			if not userPassword:
				invalidReason="Passwords do not match"
			else:
				hint=windowObject.hintSection.entry.getContent()
				if len(hint.split()) < 1:
					hint=None
				#Create a new Diary
				diaryObj=self.createNewDiary(checkEntryDict[windowObject.diaryNameSection.entry],
									checkEntryDict[windowObject.passwordSection.entry],hint)
				#Quit the window
				windowObject.quit()
				windowQuit=True
				#Add to listbox
				self.openScreen.openListbox.addObject(diaryObj.name,diaryObj)
				#Open that diary
				self.displayDiary(diaryObj)

		if not windowQuit:
			#Check for Error messages
			if invalidReason is not None:
				windowObject.showStatus(invalidReason)
			else:
				windowObject.hideStatus()

	def createNewDiary(self,diaryName,diaryPassword,hint):
		"""
		Will create and store a
		new diary object
		"""
		#Create Object
		newDiary=diary(diaryName)
		#todo add password bit here
		newDiary.hint=hint
		#Store
		self.projectManager.saveUserData(diaryName, newDiary)
		return newDiary

	def displayDiary(self,diaryObject):
		"""
		Will load the correct screen to display diary
		"""
		self.viewDiaryScreen.show()
		self.currentDiary=diaryObject
		#Clear the listbox
		self.viewDiaryScreen.diaryEntryListbox.clear()
		#Sort data
		#Add the entries to the listbox
		for e in sorted(diaryObject.entryList,key=lambda x: x.title):
			self.viewDiaryScreen.diaryEntryListbox.addObject(e.title,e)
		#Update the label at the top
		self.viewDiaryScreen.topLabelVar.set(str(diaryObject.name)+" - Entries")

	def displayDiaryEntry(self,diaryEntryObject):
		"""
		Will display a diary entry on the screen
		"""
		#Show the screen
		self.viewDiaryEntryScreen.show()
		#Update Variable
		self.currentDiaryEntry=diaryEntryObject
		#Clear the text box
		self.viewDiaryEntryScreen.textArea.delete('1.0', END)
		#Insert the data into the textbox
		self.viewDiaryEntryScreen.textArea.insert('1.0', diaryEntryObject.content.rstrip("\n"))
		#Calculate word count
		self.viewDiaryEntryScreen.updateWordCount()
		#Update the title
		diaryName=diaryEntryObject.master.name
		entryName=diaryEntryObject.title
		self.viewDiaryEntryScreen.currentDiaryName.set(str(diaryName)+" - "+str(entryName))
		#Update creation date
		if diaryEntryObject.dateCreated:
			self.viewDiaryEntryScreen.dateVar.set("Date Created: "+str(diaryEntryObject.dateCreated))
		if self.currentDiary:
			#Update font
			userFont=self.currentDiary.font
			userFontSize=self.currentDiary.fontSize
			self.viewDiaryEntryScreen.fontPickerVar.set(userFont)
			self.viewDiaryEntryScreen.fontSizeVar.set(userFontSize)
			#Update the text widget font
			self.viewDiaryEntryScreen.textArea.configure(font=(userFont,userFontSize))
		#Set Focus
		self.focus_force() #So widgets respond
		self.viewDiaryEntryScreen.textArea.focus_set() #Allow user to start typing


	def attemptOpenDiary(self):
		"""
		Will attempt to open
		diary from start screen
		"""
		# Get object from listbox
		current = self.openScreen.openListbox.getCurrentObject()
		if current:
			self.displayDiary(current)
		else:
			showMessage("Error", "Please select a diary or create one")

	def attemptOpenDiaryEntry(self):
		"""
		When the user clicks
		to open a diary entry
		"""
		current = self.viewDiaryScreen.diaryEntryListbox.getCurrentObject()
		if current:
			self.displayDiaryEntry(current)
		else:
			showMessage("Error", "Please select an entry or create one")

	def attemptDeleteDiaryEntry(self):
		"""
		Called when user clicks "Delete"
		"""
		current = self.viewDiaryScreen.diaryEntryListbox.getCurrentObject()
		if current:
			#Delete
			self.deleteDiaryEntry(current)
			#Remove from listbox
			#todo add method to delete in tkinterTools
			currentIndex=self.viewDiaryScreen.diaryEntryListbox.curselection()
			self.viewDiaryScreen.diaryEntryListbox.delete(currentIndex)
		else:
			showMessage("Error", "Please select an entry to delete")



#Final Call
if __name__ == '__main__':
	window=PyDiary()
	window.mainloop()

