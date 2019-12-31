import os

print(os.path.expanduser("~"))

print(os.path.join(os.getenv("USERPROFILE"), "file.txt"))


def krishna(*, name=0):
    print(name)


krishna(name=2)

print("######################################################")


