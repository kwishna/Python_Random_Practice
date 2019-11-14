# def keyword to declare a function
def do_somethig(job):
    print(job+"ing")

do_somethig("runn")
do_somethig("dance")
print("*****************")

def do_somethig(job = "writ"): #default parameter.
    print(job+"ing")
do_somethig()
do_somethig("play")
print("*****************")

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)