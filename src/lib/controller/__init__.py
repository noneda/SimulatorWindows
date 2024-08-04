
from ..model import Status

class Computer(Status):

    Actions : tuple[bool, bool, bool]
    def __init__(self) -> None:
        self.On()
        
    #* Actions that can be Use
    def On(self) -> bool:
        self.On = True
        self.Screen().run()
        return True

    def Off(self) -> bool:
        self.On = True
        del self.Process
        del self.Keyboard
        return True

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
    def KeyBoardDontGetEnymore(self) -> bool:
        if len(self.Keyboard) >= 10:
            self.Error.SlowPerformance = True
            return True
        elif len(self.Keyboard) >= 20:
            self.Error.SlowPerformance = True
            return True
        else:
            return False        

    def ProcessDontGetEnymoressMore(self) -> bool:
        if len(self.Process) >= 2:
            self.Error.ErrorToLoad = True
            return True
        elif len(self.Keyboard) >= 5:
            self.Error.ErrorToLoad = True
            return True
        else:
            return False

    def IsDead(self) -> bool:
        if self.Error.ErrorToLoad == True and self.Error.SlowPerformance: 
            self.Error.BlueScreenOfDead = True
        else:
            return False
