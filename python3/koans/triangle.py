#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    # pass
    if not a > 0 or not b > 0 or not c > 0:
        raise TriangleError(Exception)

    if a==b and b==c:
        return 'equilateral'
    elif not a==b and not b==c and not a==c:
        return 'scalene'
    else:
        if not a+b>c or not a+c>b or not b+c>a:
            raise TriangleError
        return 'isosceles'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
