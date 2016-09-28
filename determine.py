#!/usr/bin/env python3
import os
import platform
import subprocess

print("OS ",platform.system())
print("Release ",platform.release())

p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
#out = p.stdout.readlines()
print("String: ",p.stdout.readlines())
print("String: ",p.stdout.readlines())

