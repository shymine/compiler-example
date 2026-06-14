from lexical import lexical

text = """
let x int = 3 + 5;
const y int = 2 * 4;
let z float = x / y;
"""

seq = lexical(text)
print(seq)