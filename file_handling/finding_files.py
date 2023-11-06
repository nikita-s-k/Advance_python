# Finding the files
# List all the files in specific directory

import os, fnmatch
from pathlib import Path


# List all the files in given directory
def list_all_files(dir):
    for files in os.listdir(dir):
        print(files)


def search_files_which_ends_with_extension(directory, search_end):
    for files in os.listdir(directory):
        if files.endswith(search_end):
            print(f"Files with extension {search_end} - {files} ")


def search_files_which_starts_with_string(directory, search_with_start):
    for files in os.listdir(directory):
        if files.startswith(search_with_start):
            print(f"Files with staring {search_with_start} - {files} ")


def search_files_with_matching_pattern_of_name(directory, match_pattern):
    for files in os.listdir(directory):
        if fnmatch.fnmatch(files, match_pattern):
            print(f"matching pattern {match_pattern} - {files} ")


def search_glob(directory, advance_match):
    p = Path(directory)
    for files in p.glob(advance_match):
        print(f"globe search {files}")


# string methods

if __name__ == "__main__":

    # Problem1 : List all the files in given directory
    list_all_files(directory)

    # Problem2 :Search files in given directory which are similar and ends with same extension
    search_end = '.py'
    search_files_which_ends_with_extension(directory, search_end)

    # Problem3 :Search files in given directory which are similar and starts with same string
    search_with_start = "SCP"
    search_files_which_starts_with_string(directory, search_with_start)

    # Problem4 : Search files with module fnmatch
    #  fnmatch : Test whether the filename string matches the pattern string, returning True or False .
    match_pattern = "*.csv"
    search_files_with_matching_pattern_of_name(directory, match_pattern)

    # Advance pattern matching for files
    advance_match = "*Report*.*"
    search_files_with_matching_pattern_of_name(directory, advance_match)

    # Problem 5 : Find file with globe
    # get entire file paths ex  C:\Users\autoadmin\Downloads\abc.xls
    search_glob(directory, advance_match)
