# compiler-example

This project is to create a small compiler for an imaginary simple language.

## The language

### Base types:
- int (equivalent of a int64)
- float (equivalent of a float64)
- bool (boolean: True or False)
- string
- []\<type> :list (an unbound liked list implementation)
- [\<type a>]\<type b> (a map from type a to type b)

### Declare a variable or constant:
- let ident \<type>;
- const ident \<type>= \<value>;
    - A const must be assigned at declaration

### Assign a value to a variable:
- ident = \<value>;

value here can be any expression producing a value

### Operators

- +: perform the sum of two int or float, producing either an int or a float depending on its parameters. Concatenate two strings together.
- -: compute the difference betzeen two int or float, producing either an int or a float depending on its parameters.
- *: multiply two int or float, producing either an int or a float depending on its parameters.
- /: divide two ints or float, if the parameters are int then it computes the whole division, if they are float then it is the usual division.
- ==: compare two values of the same type and returns whether or not they have the exact same value as a boolean
- !=: compare two values of the same type and returns whether or not they have different value as a boolean
- !: inverse the value of a boolean
- <: compare two floats or two ints and return whether the value on the left is lower than the value on the right
- \>: compare two floats or two ints and return whether the value on the left is greater than the value on the right
- <=: compare two floats or two ints and return whether the value on the left is lower or equal than the value on the right
- \>=: compare two floats or two ints and return whether the value on the left is greater or equal than the value on the right
- &: returns the AND operator of two booleans
- ||: returns the OR operator of two booleans

### Function

```
fun <function_name>(param1 <type>, param2 <type>) <return_type>{

}
```

The key-word 'return' is the end of the function, any lines past this key-word that are still in the braces are not takken into account. 'return' sends the value on its right to the function caller.

### Blocks

```
if <boolean expression> {

}
if <boolean expression> {

}else {

}
```
These blocks are the conditionnal blocs for the language.
```
for <pre loop statement>;<continuation statement>;<post loop statement> {

}
for <continuation statement> {

}
```
The \<pre loop statement> is done just before the loop start.
The \<continuation statement> is done at the beginning of each iteration. If the statement has a true value then the iteration continues, if it is false then the iteration ends.
The \<post loop statement> is performed at the end of any iteration.
If no pre loop or post loop statement are to be performed then it is possible to write the for loop without ';'.
