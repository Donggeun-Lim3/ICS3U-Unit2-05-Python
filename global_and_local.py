#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on June 2020
# This program shows how global and local variables work

# global variable
variable_A = 25


def local_variable():
    # this shows what happens with local variables

    variable_A = 10
    variable_B = 30
    variable_C = variable_A + variable_B

    print("Local variable_a, ariable_B, variable_C: {0} + {1} = {2}".
          format(variable_A, variable_B, variable_C))


def global_variable():
    # this shows what happens with global variables

    global variable_A
    variable_A = variable_A + 1
    variable_B = 30
    variable_C = variable_A + variable_B

    print("Global variable_A, variable_B, variable_C: {0} + {1} = {2}".
          format(variable_A, variable_B, variable_C))


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
