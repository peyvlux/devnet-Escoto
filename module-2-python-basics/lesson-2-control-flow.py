"""
Module 2 — Lesson 2: Control Flow
Student: Jazper Escoto
Date: September 28, 2026

Control flow is used to control which code runs in a
program. It allows the program to make decisions based
on conditions. We can use if, elif, and else to choose
what the program should do.

control flow: controls the order in which code runs.
condition: something that can be True or False.
if: runs code when a condition is True.
elif: checks another condition if the first condition is False.
else: runs when all previous conditions are False.
comparison: checks values using operators like ==, >, or <.

Write at least one working example below that you
came up with yourself — not copied from class.
"""

score = 85

if score >= 90:
print("Excellent")
elif score >= 75:
print("Passed")
else:
print("Failed")

"""
A MISTAKE I MADE (or one I want to avoid)

One mistake I want to avoid is forgetting the colon (:)
after an if, elif, or else statement. I also need to
remember to use proper indentation for the code inside
the condition.

Control flow can work with variables and loops. A program
can use a variable as a condition and then use a loop to
repeat an action based on that condition.
"""