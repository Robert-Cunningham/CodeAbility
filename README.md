<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/CodeAbility_Logo.png" height="300"><br><i>Sanskriti Sharma, Lilia Heinold, Ian Richardson, Chris Zhu and Robert Cunningham<br>Winner of Best Overall Hack and Best Documentation<br>HackUMass VI 2018</i></align>

# Summary
Code-ability is an interface of hardware and software that allows people who have limited use of their hands to program. 

Many programmers have limited use of ther hands— be it from stress related injuries to carpal tunnel, early onset arthritis, or even paralysis and nerve damage. Whatever the cause, these programmers have a very hard time typing their programs and have to choose between trying to use an existing dictation software not meant for programmers, or avoiding writing new code altogether.

Most text to speech today is meant specifically to parse English, which makes it very hard to dictate code without saying something like

> If open parenthesis x equals equals 5 close parenthesis open bracket...

With Code-ability, the above if statement can be dictated as

> If x equals 5 then

Which will be parsed as

    if(x == 5):
	    # body

Here is a [full demo video](https://youtu.be/aKf8mtaoPjI).

See the *Hardware* section for description of the navigational foot pedals which accompany the project.

**TL;DR** : This is a [link to a transcript](https://docs.google.com/document/d/19Auq4oLQTWo006qVTXHtjpSA8jYfUK3qx8wWoGSSg0s/edit?usp=sharing) of our brief overview presented in the closing ceremonies of HackUMass VI.

# User Guide
Here is a comprehensive guide for the use of CodeAbility. This roadmap is mainly organized into: **Keywords**, **Line by line / Program Examples**, and **Hardware**.

## Keywords
If the program parses what you say straight into code (see *Line by line examples*), it will insert it into your file. Otherwise, there are specific voice commands that you can use for various operations. 

*NOTE: The program uses the NATO phonetic alphabet to say single letters, so as not to confuse the speech to text algorithm.*

The specific commands are split into the following categories, as they appear in the sections of this document:

 - **Create command**: `Create [item]`: Creates an item such as a for loop, if statement etc
	 - When creating an item, use the word "next" to jump to the next field
 - **Manuverability Commands**: Shortcuts based on Vim to navigate around the page and manipulate the text efficiently.
 - **Editing Commands**: Shortcuts that allow you to go back and edit things you've already written.
 - **Function Definition**: `Define [name] with parameters [param1] and [param2] body`: Create a function [name](param1, param2):
 - **Function Calling**: `Call [function] ...`: Calls a function with parameters 
 - **Delimiting Lists**: Methodology for specifying a list (including nested lists).



### Create keyword

You can create the following items with the **create** keyword. The [] means that you can use **next** to fill in that field
- For loop
	- `for [] in []:`\
			`[]`
- For range loop
	- `for [] in range([]):`\
			`[]`
- While loop
	- `while([]):`\
			`[]`
- If statement
	- `if([]):`\
			`[]`
- Function
	- `def []([]):`\
			`[]`

### Manuverability
Use these words to navigate around the page:
- `Next word`: equivalent to vim’s “e”
- `Previous word`: equivalent to vim’s “b”

- `Teleport to [symbol]`: Teleport to symbol
- `Teleport to line`: Teleport to line
- `Jump to [item] / goto [item]`: Goes to an item in the file, such as a line number, word or specific function

You can do the following with the **teleport to**,  **goto**, and **Jump to** keywords:
- line #
- next word
- last word / previous word

### Editing
Commands to edit previously written code:
- `Backspace / Back`: you guessed it
- `Replace [word1] with [word2]`: Replace the next occurance of word1 with word2

### Calling functions
- No parameters
	- `call [function name]`
- One parameter
	- `call [function name] with parameter [param]`
- Parameter as return value
	- `call [function name] with result of [function name 2]`
- Multiple parameters
	- `call [function name] with parameters [param1] and [param2] and [param3]`

### Delimiting lists
- If you have a nested list (like a nested function call), each list should be delimited with the same word, with different words for different lists. For example:
	-  > print the result of func with parameters second func 40 comma third func 9 pound 4 and 7
		- `print(func(secondFunc(40,thirdFunc(9,4)),7)`
	- You can use the following words to distinguish between separate lists:
		- comma
		- and
		- pound
		- carat

## Line by Line Examples
Here are a few examples of other english-like language which CodeAbility is able to parse:

- return the result of the factorial of the quantity 5 plus the element at x plus y in myarray → `return factorial(5 + myArray[x + y])`
- The result of x of 1 and two and the result of y of three comma four and five) → `x(1, 2, y(3, 4), 5)`
- Length of an iterable
	- The length of array → `len(array)`
- Compare Expressions
	- X is greater than or equal to Y → `X >= Y`
	- X equals Y → `X == Y`
- Call Functions
	- Call fib with parameters x and y → `fib(x,y)`
	- Return the result of fib of x and y → `fib(x,y)`
- Create Lists
	- List of x and y and z → `[x,y,z]`
	- Empty list → `[]`
- Index and slice into arrays
	- Element 2 of myArray → `myArray[2]`
	- Elements 3+1 through end of myArray → `myArray[4:]`
- Prioritize expressions
	- Fib of x plus y plus z → `fib(x)  + y + z`
	- Fib of quantity x plus y plus z → `fib(x + y) + z`
- Arithmetic
	- x plus y → `x + y`
- Control Statements
	- if x equals y then return x minus y
	- Otherwise if x is less than y then return y minus x
	- Else return y
- Assing variables
	- Set x to y
- Strings
	- Quote hello unquote


## Full Program Examples

> import math\
> define function sum with parameters X-Ray and Yankee\
> return X-Ray plus Yankee\
> back call print with result of sum with parameters math dot pow of 2 comma 3 and 70

    import math
    def sum(x, y):
	    return x + y
	print(sum(math.pow(2,3),70))

> define sort with parameters array and body\
> if the length of array is less than or equal to 1 then\
> return array\
> else\
> set pivot to element 0 of array then\
> set larger to x for x in elements 1 through end of array if x is greater than pivot then\
> set smaller to x for x in elements 1 through end of array if x is less than or equal to pivot then\
> return result of sort of smaller plus list of pivot plus result of sort of larger

    def q_sort(array):
    	if len(array) <= 1:
    		return array
    	else:
    		pivot = array[0]
    		larger = [ element for element in array[1:] if element > pivot ]
    		smaller = [ element for element in array[1:] if element <= pivot ]
    		return q_sort(smaller) + [pivot] + q_sort(larger)

> if num is greater than one then\
> create for range\
> india next\
> two comma num next\
> if num modulus india equals 0 then\
> return false\
> break\
> back else\
> return true\
> back back else\
> return false

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
            return false
            break
        else:
            return true
    else:
        return false

# Hardware
While the implementation of manuverability commands is very helpful, using voice commands for scrolling or simple navigation is tedious. This is why we implemented a custom designed system of foot pedals which allow the user to preform navigational actions quickly and smoothly.

There are 5 foot pedals, whose actions are completely configurable to any keyboard shortcut in `pedalConfig.json` (see the file for reference as well.
By default, the settings map the pedals to PTT, Shift, Down, Up, and Tab.

PTT (Push To Talk):
When pushing PTT, the program begins listening for commands and processes any speech into formatted syntactic text. Letting go of PTT ends speech to text conversion. Holding Shift and then depressing PTT latches PTT, so that the program continues listening without continual depression of the PTT pedal. To disable PTT latch, press the PTT pedal (pressing Shift is not necessary).

Down:
Pushing Down moves the cursor down one line, and pressing Shift with Down inserts a new line below the cursor.

Up:
Pushing Up moves the cursor up one line, and pressing Shift with Up inserts a new line above the cursor.

Tab:
Pushing Tab switches between the 2 most recent tabs, and pressing Shift with Tab allow you to cycle through all open tabs.

Shift:
(Modifier key to trigger secondary action).

# Images

<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/Cover_image.jpg" height="300"></align>

<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/Project_in_use.jpg" height="300"></align>


<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/top_pedal_design.png" height="300"></align>

<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/Bottom_pedal_design.png" height="300"></align>

<p align="center"><img src="https://github.com/Robert-Cunningham/CodeAbility/blob/master/Images/Schematic_Scrn.png" height="300"></align>

### Notes
Although this is a Hackathon project, this isn't the final version. We plan to continue development and testing; which includes code refactoring, adding new features and releasing the project fully with install instructions. 
