"""
filehandling:

  read mode(r): for reading
  write mode(w): for writing
  append(a): updating
  create(x): file create
r+
w+ write + read
a+ append+read
"""

f=open("newfile.txt","r")

print(f.read())