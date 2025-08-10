#!/usr/bin/env bash

# This test verifies that the code compiles cleanly with -Wall.
# The default timeout for tests is 2 seconds; we increase it here
# because compilation can take a while.

#@test{"stdout":10, "name":"Test case 1"}
./main < test1.txt

#@test{"stdout":10, "name":"Test case 2"}
./main < test2.txt