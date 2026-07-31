# Reflection Answers

## 1. You accessed a _protected attribute from outside the class and Python allowed it. So what is the point of the underscore?

A single underscore is a convention that tells programmers that an attribute is intended for internal or protected use. Python does not actually prevent access to it from outside the class.

## 2. You accessed a __private attribute using its mangled name. Is __ really "private"? What is it actually for?

No, `__` does not provide true private access in Python. It uses name mangling, which changes the attribute name to `_ClassName__attribute` and helps prevent accidental access or naming conflicts.

## 3. Which of the three protections in this assignment is genuinely enforced by Python, and how do you know?

The read-only property is genuinely enforced by Python in this assignment. Since the property has a getter but no setter, trying to assign a new value raises an `AttributeError`.

## 4. Why must total_accounts be a class attribute rather than an instance attribute? What would break if you made it an instance attribute?

`total_accounts` must be a class attribute because it represents the total number of accounts shared by all `BankAccount` objects. If it were an instance attribute, each account would have its own separate counter instead of one shared total.

## 5. In Problem 3, average is calculated every time instead of being stored. Give one advantage and one disadvantage of that design.

One advantage is that the average is always based on the latest marks, so it cannot become stale when marks are changed. One disadvantage is that the calculation is repeated every time the average is accessed, which can be less efficient if it is accessed frequently.
