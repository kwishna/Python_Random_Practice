from os import path as p

print(f"If The File {'./files/readmepython.txt'}' Exists : {p.exists('./files/readmepython.txt')}")
print(p.getsize('./files/readmepython.txt'))

with open("./files/readmepython.txt", 'a+') as o:
    o.truncate()
    o.write("This File Is Created By Python\n")
    o.flush()
    o.close()

#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
