"""
Author: Charlie Doherty
KUID: 3115329
Date: 1/31/24
Lab: 01
Last modified: 1/31/24
Purpose: Refresh on EECS 168 concepts and familiarize self with tsv files
"""
from executive import Executive

if __name__ == "__main__":
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name)
    my_exec.run()
