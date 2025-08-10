#!/usr/bin/env bash

# This test verifies that the code compiles cleanly with -Wall.
# The default timeout for tests is 2 seconds; we increase it here
# because compilation can take a while.

#@test{"stdout":2, "name":"Test case 1", "output":"Hint: Does your program pass the example in the assignment?"}
./main1

#@test{"stdout":2, "name":"Test case 2", "output":"Hint: This is a general test case."}
./main2

#@test{"stdout":2, "name":"Test case 3", "output":"Hint: This is a general test case."}
./main3

#@test{"stdout":2, "name":"Test case 4", "output":"Hint: This is a general test case."}
./main4

#@test{"stdout":2, "name":"Test case 5", "output":"Hint: This is a general test case."}
./main5