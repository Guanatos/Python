#!/usr/bin/env python
import os

dirname = input("Please provide the path :\n")

if os.path.isdir(dirname):
   print("is a directory",dirname)
else:
   print("is not a directory",dirname)
