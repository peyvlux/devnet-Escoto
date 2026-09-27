"""
Module 2 — Activity 1: File Sorting
Student: Jazper Escoto
Date: September 28, 2026

============================================
WHAT IS THIS ACTIVITY?
======================

This activity is about sorting files into different
categories based on their file extensions. It helps
organize files and makes them easier to find.

============================================
WHAT I LEARNED
==============

I learned that Python can check a file's extension and
use conditions to decide where the file should go.
I also learned how strings and if statements can be
used to handle different file types.

============================================
MY OWN EXAMPLE
==============

"""

filename = "assignment.py"

if filename.endswith(".py"):
print("This is a Python file.")
elif filename.endswith(".txt"):
print("This is a text file.")
elif filename.endswith(".jpg") or filename.endswith(".png"):
print("This is an image file.")
else:
print("Unknown file type.")

# """

# A MISTAKE I MADE (or one I want to avoid)

One mistake I want to avoid is checking the wrong file
extension. I also need to remember that the extension
must be written correctly, such as ".py" for Python files.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
===================================

File sorting connects to control flow because the program
uses if, elif, and else to decide how to handle different
types of files.
"""
