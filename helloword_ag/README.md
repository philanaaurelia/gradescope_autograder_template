This is the basic form of the Gradescope Autograder: Diff-based solution with no additional files. 
The following problem is here:

```
(3) (20 points) Hello World

Write a program titled a C++ program in a file titled hello_world.cpp
that prompts a user for their full name and displays “Hello, [name here]!”
The output format should look EXACTLY (except for the name of
course!) like the following example:

What is your name? Philana Benton
Hello, Philana Benton!
```

# Modified files/folders 
## BUILD-FILES
Contains the Makefile used to compile student submitted C++ file(s). 
- I emphasized importance of naming the file `hello_world.cpp`, otherwise the build will fail! Also note that the executable is named `main`. This is because its easier to edit different autograders for different problems.

## EXECUTION-FILES
Contains all files needed to run the student code and solution code needed to perform a diff.
- I added the test files I wanted to run as input for the student code and my solution code.

## REFERENCE-FILES
Contains all references files related to the solution
- I added the correct solution I wrote `hello_world.cpp` here.

## diff.sh
Contains the bash file needed to run the executable (with any necessary execution files)
