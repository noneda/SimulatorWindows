from dataclasses import dataclass
from ..view import ComputerApp

@dataclass
class Errors:
    BlueScreenOfDead : bool
    ErrorToLoad : bool
    SlowPerformance : bool

@dataclass
class Status:
    on : bool
    Screen : ComputerApp
    Process : list[int]
    Keyboard : str
    Error : Errors