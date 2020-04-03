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
        self.titleLeftSide.grid(row=0,column=0,sticky="EW")
        self.titleMiddle=mainFrame(self.titleBar)
        self.titleMiddle.grid(row=0,column=1,sticky="EW")
        self.titleRightSide=mainFrame(self.titleBar)
        self.titleRightSide.grid(row=0,column=2,sticky="EW")

        self.toolBar=mainFrame(self)
        self.toolBar.grid(row=1,column=0,sticky="EW")
        self.toolBar.gridConfig(0)
        self.toolBarMiddle=mainFrame(self.toolBar)
        self.toolBarMiddle.grid(row=0,column=0)

        self.mainContent = mainFrame(self)
        self.mainContent.grid(row=2, column=0, sticky="NSEW")
        self.buttonSection = buttonSection(self)
        self.buttonSection.grid(row=3, column=0, sticky="EW")
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
        self.wordCountLabel.config(font=globalFontTiny)
        self.wordCountLabel.grid(row=0,column=0)
        #Tool Bar
        #todo create custom class with bold font option
        self.fontPickerVar=StringVar()
        self.fontPickerVar.set("Arial")
        self.fontOptions=["Helvetica","Arial","Avenir"]
        self.fontPicker=ttk.OptionMenu(self.toolBarMiddle, self.fontPickerVar, self.fontOptions[0], *self.fontOptions)
        self.fontPicker.configure(width=12)
        self.fontPicker.grid(row=0,column=0)
        self.fontSizeVar=StringVar()
        self.fontSizeVar.set("13")
        self.fontSizeOptions=[5,6,7,8,9,10,11,12,13,14,15,16,18,20,22]
        self.fontSizePicker=ttk.OptionMenu(self.toolBarMiddle, self.fontSizeVar, self.fontSizeOptions[0], *self.fontSizeOptions)
        self.fontSizePicker.configure(width=12)
        self.fontSizePicker.grid(row=0,column=1)
        #Main Content
        self.mainContent.gridConfig(0)
        self.textArea=Text(self.mainContent)
        self.textArea.configure(borderwidth=0, highlightthickness=0)
        self.textArea.grid(row=0,column=0,sticky="NSEW")
        #Button Bar
        self.buttonSection.addButton("Close")
        self.buttonSection.addButton("Save")
        #Colour
        self.buttonSection.colour(globalOffWhiteColour)
        #self.titleBar.colour("#d1e8cc")

class viewDiaryScreen(screen):
    """
    Screen where user
    can view and edit diary contents
    """
    def __init__(self,controller):
        screen.__init__(self,controller,"Diary")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        #Configure
        self.topBar=mainFrame(self)
        self.topBar.grid(row=0,column=0)
        self.mainContent=mainFrame(self)
        self.mainContent.grid(row=1,column=0,sticky="NSEW")
        self.buttonFrame=mainFrame(self)
        self.buttonFrame.grid(row=2, column=0)
        self.buttonFrame.grid_columnconfigure(0,weight=1)
        self.leftButtonSection=buttonSection(self.buttonFrame)
        self.leftButtonSection.grid(row=0,column=0,sticky="EW",padx=20)
        self.rightButtonSection=buttonSection(self.buttonFrame)
        self.rightButtonSection.grid(row=0,column=1,sticky="EW",padx=20)
        #Title
        self.topBar.gridConfig(0)
        self.titleLabel=titleLabel(self.topBar,text="Diary - Entries")
        self.titleLabel.grid(row=0,column=0)
        #Main
        self.mainContent.gridConfig(0)
        self.diaryEntryListbox=advancedListbox(self.mainContent)
        #self.diaryEntryListbox.configure(width=150)
        self.diaryEntryListbox.grid(row=0,column=0,sticky="NSEW")
        #Buttons
        self.rightButtonSection.addButton("Delete")
        self.rightButtonSection.addButton("Open")
        self.leftButtonSection.addButton("Back")
        self.leftButtonSection.addButton("Create")



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
        #todo add while loop to check for previous entries
        numberOfEntries=0
        self.diaryEntryTitle.entry.insert(END,"Entry #"+str(numberOfEntries+1))
        #todo add banned words
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
        self.geometry("700x500")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.screenMaster=screenController(self)
        self.screenMaster.grid(row=0,column=0,sticky="NSEW")
        #Project Manager
        self.projectManager=projectManager(getWorkingDirectory(),"PyDiary")
        self.projectManager.fileExtension=".pdy"
        #Reference the screens
        self.openScreen=openScreen(self.screenMaster)
        self.unlockScreen=unlockScreen(self.screenMaster)
        self.viewDiaryEntryScreen=viewDiaryEntryScreen(self.screenMaster)
        self.viewDiaryScreen=viewDiaryScreen(self.screenMaster)
        #Show Call
        self.viewDiaryScreen.show()

        #======BUTTON COMMANDS======
        #Open Screen
        self.openScreen.buttonSection.getButton("Create").config(command=self.launchCreateDiaryFileWindow)
        #ViewDiaryScreen
        self.viewDiaryScreen.leftButtonSection.getButton("Create").config(command=self.launchCreateDiaryEntryWindow)

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
                self.createNewDiary(checkEntryDict[windowObject.diaryNameSection.entry],
                                    checkEntryDict[windowObject.passwordSection.entry],hint)


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
        print("\nReady to create a new diary")
        print("Name: ",diaryName)
        print("Password: ",diaryPassword)
        print("Hint: ",hint)

#Final Call
if __name__ == '__main__':
    window=PyDiary()
    window.mainloop()

