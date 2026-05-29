# Detailed Notes on Chapter 1: A Tutorial Introduction

## 1.1 Getting Started
* **Program Structure:** The only way to learn a new programming language is by writing programs in it. Every C program consists of functions and variables, and execution always begins at the `main` function. Statements specify the computing operations to be done and are enclosed in braces `{ }`.
* **Standard Library:** The directive `#include <stdio.h>` tells the compiler to include information about the standard input/output library, providing access to functions like `printf`.
* **Strings and Escape Sequences:** A sequence of characters in double quotes is called a character string or string constant. C uses escape sequences for hard-to-type characters, such as `\n` for a newline, `\t` for a tab, `\b` for backspace, `\"` for a double quote, and `\\` for a backslash. 

## 1.2 Variables and Arithmetic Expressions
* **Declarations and Types:** All variables must be declared before they are used, usually at the beginning of the function. Basic data types include `int` (integer), `float` (floating point), `char` (single byte character), `short` (short integer), `long` (long integer), and `double` (double-precision floating point).
* **Arithmetic and Truncation:** Integer division truncates any fractional parts. However, if an arithmetic operator has one floating-point operand and one integer operand, the integer will be automatically converted to floating point before the operation.
* **Formatting Output:** The `printf` function uses conversion specifications like `%d` for integers, `%f` for floating-point numbers, and `%o` or `%x` for octal and hexadecimal. Width and precision can also be specified, such as `%6.1f` (at least six characters wide, one digit after the decimal).
* **While Loops:** The `while` loop tests a condition in parentheses; if true, the body of the loop executes, and the condition is re-tested again until it becomes false.

## 1.3 The `for` Statement
* The `for` loop is a generalization of the `while` loop. It consolidates the initialization, condition test, and incrementing step into a single line, making loops more compact and keeping the loop control statements together in one place. 

## 1.4 Symbolic Constants
* **Avoiding "Magic Numbers":** It is bad practice to bury hardcoded numbers directly in the program code. The `#define` directive creates a symbolic constant, replacing a symbolic name with a specific replacement text.
* **Syntax:** Symbolic constant names are conventionally written in upper case so they can be readily distinguished from lower case variable names, and there is no semicolon at the end of a `#define` line.

## 1.5 Character Input and Output
* **Text Streams:** Input and output are dealt with as text streams—sequences of characters divided into lines, each ending with a newline.
* **Reading and Writing:** `getchar()` reads the next character from a text input stream, and `putchar(c)` prints a character. 
* **End of File (EOF):** `getchar` returns a distinctive value, `EOF` (end of file), when there is no more input. Variables storing characters from `getchar` must be declared as `int` rather than `char` so they are big enough to hold the `EOF` value in addition to any valid character.
* **Assignment within Expressions:** In C, any assignment is an expression and has a value, allowing concise idioms like `while ((c = getchar()) != EOF)`.
* **Logical Operators:** Expressions connected by `&&` (AND) or `||` (OR) are evaluated strictly from left to right, and evaluation is guaranteed to stop as soon as the truth or falsehood is known.
* **Conditionals:** The `if-else` statement expresses decisions. The double equals sign `==` tests for equality, while a single `=` is used for value assignment. 

## 1.6 Arrays
* Arrays group multiple variables of the same type, and array subscripts always start at zero in C.
* Characters are small integers, so `char` variables and constants are identical to `int`s in arithmetic expressions. For instance, `c - '0'` converts a character digit into its numeric value.
* Multi-way decisions are frequently expressed using `else if` sequences, which evaluate conditions in order from the top until one is satisfied.

## 1.7 Functions
* Functions encapsulate computations so they can be used without worrying about their implementation details.
* **Function Prototypes:** A declaration like `int power(int m, int n);` before `main` specifies the parameter types and the return type. This prototype makes it much easier for a compiler to detect errors caused by mismatched arguments. 
* A function returns a value to the caller using the `return` statement. If a function reaches the closing right brace without returning, it returns no useful value to the caller. 

## 1.8 Arguments - Call by Value
* In C, all function arguments are passed **"by value"**. This means the called function receives the values of its arguments in temporary variables rather than the originals.
* Modifying a parameter inside a function does not alter the original argument originally called with in the calling routine. To modify a caller's variable, pointers must be used. 
* **Array Exception:** When the name of an array is passed as an argument, the value passed to the function is the location or address of the beginning of the array, allowing it to access and alter actual array elements.

## 1.9 Character Arrays
* Character arrays are the most common type of array in C. C stores strings internally as arrays of characters terminated by a null character (`'\0'`) so programs can detect the end of the string.
* Functions that return no value should state so explicitly by using the return type `void`.

## 1.10 External Variables and Scope
* **Local Variables:** Automatic variables declared inside a function are private to it. They come into existence when the function is called and disappear when the function is exited.
* **External Variables:** Variables defined outside of any function are external (global) and remain permanently in existence. They can be accessed by any function that declares them, using the `extern` keyword.
* **Best Practices:** While external variables simplify argument passing, relying on them too heavily is fraught with peril. It leads to programs where data connections are not obvious, variables can be changed inadvertently, and function generality is destroyed.