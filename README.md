# Code Dictate

## Summary
Code Dictate is a dictation tool especially for programmers. Most text to speech today is meant specifically to parse English, which makes it very hard to dictate code without saying something like

> If open parenthesis x equals equals 5 close parenthesis open bracket...

Many programmers can't use their hands; from stress related injuries to carpal tunnel to early onset arthritis and even paralysis and nerve damage. Whatever the cause, these programmers have a very hard time typing their programs and have to choose between trying to use an existing dictation software not meant for programmers, or avoiding writing new code altogether. 

With Code Dictate, the above if statement can be dictated as

> If x equals 5 then

Which will be parsed as 

    if(x == 5):
	    # body
	 

## User Guide
If the program parse what you say straight into code, it will insert it into your file. Otherwise, there are specific voice commands that you can use for various operations. The program uses the NATO phonetic alphabet to say single letters, as not to confuse the speech to text algorithm.

The specific commands are split into the following catagories: 

 - `Create [item]`: Creates an item such as a for loop, if statement etc
	 - When creating an item, use the word "next" to jump to the next field
- Jump to [item] / goto [item]: Goes to an item in the file, such as a line number, word or specific function
- Back: A simple backspace
- Replace [word1] with [word2]: Replace the next occurance of word1 with word2
- Define function [name] with parameters [param1] and [param2]

### Create keyword

You can create the following items with the **create** keyword. The [] means that you can use **next** to fill in that field
- For loop
	- `for [] in []:`
- While loop
	- `while([]):`
- If statement
	- `if([]):`

### Jump to and goto

You can do the following with the **jump to** and **goto** keywords:
- end of file
- end of line
- end of block (eg. current statement or function)
- line #
- next [word]
- beginning of file
- beginning of line
- beginning of block
- next word
- last word / previous word

### Callling functions 
- No parameters
	- call [function name]
- One parameter
	- call [function name] with parameter [param]
- Parameter as return value
- Multiple parameters
### Delimiting lists
- If you have a nested list (like a nested function call), each list should be delimited with the same word, with different words for different lists. For example: 
	-  > print the result of func with parameters second func 40 comma third func 9 pound 4 and 7
		- `print(func(secondFunc(40,thirdFunc(9,4)),7)`
	- You can use the following words to distinguish between separate lists:
		- comma
		- and 
		- pound
		- carat
## Examples

> import math
> define function sum with parameters X-Ray and Yankee
> return X-Ray plus Yankee
> call print with result of sum with parameters math dot pow of 2 comma 3 and 70

    import math
    def sum(x, y):
	    return x + y
	print(sum(math.pow(2,3),70))
