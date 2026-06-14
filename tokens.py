from enum import Enum

class Token(Enum):
    LET = 0
    CONST = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    BOOL = 5
    AFFECT = 6
    SEMI_COLON = 7
    ADD = 8
    SUB = 9
    MULT = 10
    DIV = 11
    EQU = 12
    DIFF = 13
    NOT = 14
    LT = 15
    GT = 16
    LE = 17
    GE = 18
    AND = 19
    OR = 20
    FUN = 21
    LBRACE = 22
    RBRACE = 23
    LBRACKET = 24
    RBRACKET = 25

class IntValue:
    def __init__(self, value: int) -> None:
        self.value = value
    def __str__(self) -> str:
        return "IntValue(" + str(self.value) + ")"
class FloatValue:
    def __init__(self, value: float) -> None:
        self.value = value
    def __str__(self) -> str:
        return "FloatValue(" + str(self.value) + ")"
class StringValue:
    def __init__(self, value: str) -> None:
        self.value = value
    def __str__(self) -> str:
        return "StringValue(" + str(self.value) + ")"
class BoolValue:
    def __init__(self, value: bool) -> None:
        self.value = value
    def __str__(self) -> str:
        return "BoolValue(" + str(self.value) + ")"
class IdentValue:
    def __init__(self, value: str) -> None:
        self.value = value
    def __str__(self) -> str:
        return "IdentValue(" + str(self.value) + ")"