---
layout: default
title: Homepage
---

Welcome to the class website of ENGR 21 @ Swarthmore Engineering, Fall 2025. This page serves as the syllabus for this course, and will be updated regularly throughout the semester.

**Instructor**: Emad Masroor `emasroo1@swarthmore.edu`  
**Meeting Times**: MW 8:30 to 9:45  
**Office Hours**: T 12:30 to 2:00  
**Pre-requisities**: MATH 25, ENGR 17  
**Lab**: MR 1:15 to 4:00  
**Lab Instructor**: Will Johnson `wjohnso3@swarthmore.edu`  
**URL**: `https://emadmasroor.github.io/E21-F25/`  
**Midterm**: None; 6 tests  
**Final Exam**: None; Project  
**Homework Due Date**: Tue at 11:59 PM  
**Wizard Session**: Mon 7:00 to 9:00 PM  

[Schedule](#schedule) | [Lab Schedule](#labs-schedule) | [Teaching Team](#teaching-team) | [Grades](#assessment-and-grades) | [Policies](#policies)

# Schedule

| No.   | Date    | Day | Lecture Slides | Topic                                              | HW / Test |
|-------|---------|-----|----------------|----------------------------------------------------|-----------|
| 1.1   | T 09/02 | Tue |                | Introduction & Installation; variables & types     |           |
| 1.2   | R 09/04 | Thu |                | Programming basics: variables, types, conditionals |           |
| 2.1   | T 09/09 | Tue |                | Base systems; Analog vs. digital data              | HW 1      |
| 2.2   | R 09/11 | Thu |                | Relative & absolute errors;                        |           |
| 3.1   | T 09/16 | Tue |                | For/while loops; 'dot notation'                    | HW 2      |
| 3.2   | R 09/18 | Thu |                | Functions; Finite State Machines                   | Test 1    |
| 4.1   | T 09/23 | Tue |                | Desktop installation; IDEs                         | HW 3      |
| 4.2   | R 09/25 | Thu |                | Floating point numbers                             |           |
| 5.1   | T 09/30 | Tue |                | Introduction to `numpy`                            | HW 4      |
| 5.2   | R 10/02 | Thu |                | Data Visualization for Engineering in Python       | Test 2    |
| 6.1   | T 10/07 | Tue |                | Root-finding                                       | HW 5      |
| 6.2   | R 10/09 | Thu |                | Root-finding                                       |           |
|       |         |     |                | **Fall break**                                     |           |
| 7.1   | T 10/21 | Tue |                | Linear Systems                                     | HW 6      |
| 7.2   | R 10/23 | Thu |                | Linear Systems                                     | Test 3    |
| 8.1   | T 10/28 | Tue |                | Curve fitting & Interpolation                      | HW 7      |
| 8.2   | R 10/30 | Thu |                | Curve fitting & Interpolation                      |           |
| 9.1   | T 11/04 | Tue |                | Optimization                                       | HW 8      |
| 9.2   | R 11/06 | Thu |                | Optimization                                       | Test 4    |
| 10.1  | T 11/11 | Tue |                | Optimization                                       | HW 9      |
| 10.2  | R 11/13 | Thu |                | Numerical Differentiation                          |           |
| 11.1  | T 11/18 | Tue |                | Numerical Integration                              | HW 10     |
| 11.2  | R 11/20 | Thu |                | Initial Value Problems                             | Test 5    |
| 12.1  | T 11/25 | Tue |                |                                                    |           |
|       | R 11/28 | Thu |                | **Thanksgiving**                                   |           |
| 13.1  | T 12/02 | Tue |                | Final Project                                      | HW 11     |
| 13.2  | R 12/04 | Thu |                | Final Project                                      | Test 6    |
| 14.1  | T 12/09 | Tue |                | Final Project                                      |           |

# Labs Schedule

| Date  | Day | Lab          |
|-------|-----|--------------|
| 09/08 | Mon | Lab 1        |
| 09/11 | Thu | Lab 1        |
| 09/15 | Mon | Lab 1        |
| 09/18 | Thu | Lab 1        |
| 09/22 | Mon | Lab 2        |
| 09/25 | Thu | Lab 2        |
| 09/29 | Mon | Lab 2        |
| 10/02 | Thu | Lab 2        |
| 10/06 | Mon | Lab 3        |
| 10/09 | Thu | Lab 3        |
|       |     | Fall Break   |
| 10/20 | Mon | Lab 3        |
| 10/23 | Thu | Lab 3        |
| 10/27 | Mon | Lab 4        |
| 10/30 | Thu | Lab 4        |
| 11/03 | Mon | Lab 4        |
| 11/06 | Thu | Lab 4        |
| 11/10 | Mon | Lab 5        |
| 11/13 | Thu | Lab 5        |
| 11/17 | Mon | Lab 5        |
| 11/20 | Thu | Lab 5        |
| 11/24 | Mon |              |
| 11/27 | Thu | Thanksgiving |
| 12/01 | Mon |              |
| 12/04 | Thu |              |
| 12/08 | Mon |              |

# Learning Objectives

At the end of this course, you will be able to:

- Write programs on the desktop and on microcontrollers :
	- Control the flow of a program using if statements, for/while loops, functions
	- Perform computations using variables and lists / `numpy` arrays
	- Print strings/results and debug code using print statements
	- Understand how to use external modules/libraries such as `numpy`
- Explain how information is represented by computers and microcontrollers:
	- Explain the base system and how it is used to represent decimal, binary and hexadecimal numbers.
	- Convert numbers between decimal, binary, and hexadecimal representations.
	- Define the range of variable types such as booleans, bytes, (un)signed integers, and floats, and explain their potential use cases.
	- Determine the value of a signed variable from its binary or hexadecimal representation.
- Use and understand fundamental numerical methods topics relevant to engineering 
	- Understand the concept of convergence, sources of error (e.g. truncation and round-off), relative and absolute error
	- Use root finding to solve one-dimensional equations numerically
	- Use Gaussian elimination to solve systems of linear equations
	- Apply linear systems solving to do linear least-squares curve-fitting
	- Understand single- and multi-variable unconstrained optimization
- Program microcontrollers for applications relevant to engineering
	- Interface with peripheral devices using digital inputs/outputs (e.g. LED, tactile switch)
	- Interface with peripheral devices using analog-to-digital converters (e.g. temperature sensor)
	- Interface with peripheral devices using pulse-width modulation (e.g. servo motor)
	- Interface with peripheral devices using serial communications (e.g. accelerometer or LCD)
- Place computing and embedded systems in a broader social context
	- Identify examples of embedded systems in everyday life
	- Discuss impact of systems on different aspects of society

# Teaching Team

| Name     		 | Role         		|
|----------------|----------------------|
| Instructor     | Emad Masroor         |
| Lab Instructor | Will Johnson         |
| Wizards        | Ian Forehand         |
|                | Paolo Bosques-Paulet |
|                | Brad Johnston        |
|                | Emily Chen           |
|                | Nick Fettig          |
| Graders        | Owen Hoffman         |
|                | Howard Wang          |
|                | Hannah Poon          |
|                | Liam Worden          |

# Assessment and Grades

In this class, you will have six regularly-spaced [tests](#tests) instead of one or two midterms. Reflecting the hands-on nature of the content of E21, a large proportion of the grade depends on your performance in labs and the final project (30%). There is no final exam for this course, and your final project plays the role of a 'final'. The full breakdown of how your grade will be calculated is shown in the following table.

| Component     | Grade % |
|---------------|---------|
| Homework      | 20%     |
| Tests         | 45%     |
| Lab           | 15%     |
| Final Project | 15%     |
| Participation | 5%      |

The participation grade will primarily be determined based on attendance.

The grade thresholds are shown below. The Instructor, in consultation with the Lab Instructor, reserves the right to revise these numbers upward, but will not revise these numbers downward.

| To get a grade of | You must score at least |
|-------------------|-------------------------|
| A-                | 90                      |
| B-                | 80                      |
| C-                | 70                      |
| D-                | 60                      |

A score of 60 out of 100 is the minimum passing grade for this course. 

The class will not be 'curved'. The instructor's interpretation of letter grades is the following: an A is an excellent grade; a B is a good grade, and a C is an acceptable grade. A D reflects a barely passing grade, and a score less than 60 is a failing grade. 

# Policies
Hello, world

## Lectures

Lectures for this class will be in person. They will not be recorded, and remote participation is not possible. You are expected to attend all lectures unless you have received an exception from the Instructor.

## Homework

Homework will be assigned approximately every week, and will typically be due by midnight on the Tuesday following the week in which it was assigned. You can generally expect HW $n$ to cover the material from week $n$, and to be due in week $n+1$. Typically, homework will be submitted on Moodle using Gradescope. 

Most homework assignments will have a written component as well as a programming component.

## Tests

The purpose of holding six tests instead of one or two midterms is so that you have low-stakes opportunities to demonstrate your mastery of the course material at regular intervals. In general, you can expect these tests to be independent of each other, as opposed to being cumulative. 

These tests will be held on Thursdays during the first half of class time (typically for 20 to 25 minutes), and will typically be closed-book, closed-notes and closed-computer. The tests will usually be incremental rather than cumulative, and will only cover the material from approximately two weeks prior to each test. Typically, test $n$ will cover the material from week $2n−1$ and week $2n$, and will be held on week $2n+1$; for example, test 1 will cover weeks 1 and 2 and will be held on the Thursday of week 3; test 2 will cover weeks 3 and 4 and will be held on the Thursday of week 5, etc.

## AI Tools
Hello, world

## Accommodations
Hello, world


