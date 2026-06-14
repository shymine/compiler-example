import re
from typing import Any
from tokens import Token, IntValue, FloatValue, StringValue, BoolValue, IdentValue

categories = {
        "int" : Token.INT,
        "float": Token.FLOAT,
        "bool" : Token.BOOL,
        "string": Token.STRING,
        "let" : Token.LET,
        "const": Token.CONST,
        "=" : Token.AFFECT,
        ";" : Token.SEMI_COLON,
        "+" : Token.ADD,
        "-" : Token.SUB,
        "*" : Token.MULT,
        "/" : Token.DIV,
        "==" : Token.EQU,
        "!=" : Token.DIFF,
        "!" : Token.NOT,
        "<" : Token.LT,
        ">" : Token.GT,
        "<=" : Token.LE,
        ">=" : Token.GE,
        "&" : Token.AND,
        "||" : Token.OR,
        "fun" : Token.FUN,
        "{" : Token.LBRACKET,
        "}" : Token.RBRACKET,
        "[" : Token.LBRACE,
        "]" : Token.RBRACE
    }
def lexical(data: str) -> list[Any]:
    acc = ""
    token_sequence = []
    for i, c in enumerate(data):
        # I stop the accumulation when i encounter these characters
        if re.match("[;\s{}()\[\]]", c) :
            token_sequence.append(tokenize(acc))
            token_sequence.append(tokenize(c))
            acc = ""
        else :
            acc += c
    
    return [el for el in token_sequence if not (el is None)]
            

def tokenize(data: str) -> Token | IntValue | FloatValue | StringValue | BoolValue | IdentValue | None :
    if data in categories:
        return categories[data]
    if re.match("^\"[a-zA-Z]*\"$", data) :
        return StringValue(data[1:-1])
    if re.match("^[a-zA-Z_]+$", data):
        return IdentValue(data)
    if re.match("^\d+\.\d*$", data):
        return FloatValue(float(data))
    if re.match("^\d+$", data):
        return IntValue(int(data))
    if data == "True" or data == "False":
        return BoolValue(bool(data))
    return