from sys import argv  # argv Is A List Which Contains All The Argument Values Passed While Running The .py File Through Command Line.

## sys Is Called Module Or Libraries.
print(type(argv))  # Type Of argv

#a, b, c, d, e, f, g = argv # Unpacking Into Variables. Count Of Variables Must Be Equal To Passed Arguments. Filename Is Also Counted As One Of The Argument.

a = argv[0]  # argv Is A List. Indexing Is Allowed.
print(a)

print(f'Printing The Arguments :: {argv}')

for value in argv:  # Iterating The Arguments.
    print(value)
