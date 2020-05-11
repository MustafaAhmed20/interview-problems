# interview-problems
These are technical questions sent to me for position as Python developer.

i really liked it and had fun solving it , so i shared it with you.

## Run
 **Use Python 3.6.6 or Later**

```bash
python 1.py
```

## Problem one
> Instructions
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
Include unit tests with your solution

### Examples
> - persistence(39) == 3 # because 3*9 = 27, 2*7 = 14, 1*4=4  and 4 has only one digit
- persistence(999) == 4 # because 9*9*9 = 729, 7*2*9 = 126,   1*2*6 = 12, and finally 1*2 = 2
- persistence(4) == 0 # because 4 is already a one-digit number

## Problem two
>Instructions
Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc. You need to return the highest scoring word as a string. If two words score the same, return the word that appears earliest in the original string. All letters will be lowercase and all inputs will be valid.
Include unit tests with your solution

### Examples
> - "man i need a taxi up to ubud" -> "taxi" 
- "what time are we climbing up to the volcano" -> "volcano"
- "take me to semynak" -> "semynak

## Problem three
>Instructions
Write a function which formats a duration, given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds. A year is 365 days and a day is 24 hours. For example:
formatDuration(62)    // returns "1 minute and 2 seconds"
formatDuration(3662)  // returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important. 
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
A more significant unit of time will occur before a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
Different components have different unit of times. So, there should be no repeated units like “5 seconds and 1 second”.
A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
Include unit tests with your solution

### Examples
> - 0 -> “now”
- 62 -> “1 minute and 2 seconds”
- 3662 -> “1 hour, 1 minute and 2 seconds”

