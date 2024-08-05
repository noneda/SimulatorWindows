
from ..model import Status
from ..view import ComputerApp

class Computer(Status):

    Actions : tuple[bool, bool, bool]

    def __init__(self) -> None:
        print("On Pc?")
        if "y" == input("\n\t y || n\n"):
            self.On()
        else:
            self.Off()
        
    #* Actions that can be Use
    def On(self):
        self.on = True
        self.Screen = ComputerApp()
        self.Screen.run()

    def Off(self):
        self.on = False
        del self.Process
        del self.Keyboard

    def newProcess(self) -> int:
        new = len(self.status.Process)+1
        self.Process.append(new)
        return new
    
    def delProcess(self, pross:int):
        self.Process.pop(pross)
        pass

    def getKeyBoard(self):
        pass

    #* These are Errors that it can Be Present
    def KeyBoardDontGetEnymore(self):
        if len(self.Keyboard) >= 10:
            if self.Error.SlowPerformance:
                self.Error.ErrorToLoad = True
            else:
                self.Error.SlowPerformance = True

        elif len(self.Keyboard) >= 20:
            self.Error.ErrorToLoad = True
    

    def ProcessDontGetEnymoressMore(self):
        if len(self.Process) >= 2:
            if self.Error.SlowPerformance:
                self.Error.ErrorToLoad = True
            else:
                self.Error.SlowPerformance = True
        elif len(self.Keyboard) >= 5:
            self.Error.ErrorToLoad = True

    def IsDead(self):
        if self.Error.ErrorToLoad == True and self.Error.SlowPerformance: 
            self.Error.BlueScreenOfDead = True