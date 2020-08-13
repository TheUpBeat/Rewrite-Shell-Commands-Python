# cat command built in Python
# Note: Does not work with multiple arguments (wip)

#!/usr/bin/env python
import getopt
import sys
import os
import re

argumentList = sys.argv[1:]

options = "bEnsThv:"

long_options = ['--number-nonblank', '--show-ends', '--number', '--squeeze-blank', '--show-tabs', '--help', '--version']

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ('-h', '--help'):
            
            sys.stdout.write("Usage: cat [OPTION].. [FILE]... \n" +
                    "Concatenate FILE(s) to standard output.\n" +
                    "When FILE is -, read standard input.\n" +
                    "\n" +
                        "  -b, --number-nonblank    number nonempty output lines, overrides -n \n" +
                        "  -E, --show-ends          display $ at end of each line \n" +
                        "  -n, --number             number all output lines \n" +
                        "  -s, --squeeze-blank      suppress repeated empty output lines \n" +
                        "  -T, --show-tabs          display TAB characters as ^I \n" +
                        "  -h, --help               display this help and exit \n" +
                        "  -v, --version            output version information and exit \n" +
                    "\n" +
                    "Examples: \n" +
                        "  cat f - g  Output f's contents, then standard input, then g's contents. \n" +
                        "  cat        Copy standard input to standard output. \n" +
                    "\n" +
                    "GNU coreutils online help: <https://www.gnu.org/software/coreutils/> \n"
                    "Full documentation <https://www.gnu.org/software/coreutils/cat> \n" +
                    "or available locally via: info \'(coreutils) cat invocation\' \n")
            raise SystemExit
        
        elif currentArgument in ('-v', '--version'):

            sys.stdout.write("cat (GNU coreutils) 8.32\n" +
                    "Copyright (C) 2020 Free Software Foundation, Inc.\n" +
                    "License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.\n" +
                    "This is free software: you are free to change and redistribute it.\n" +
                    "There is NO WARRANTY, to the extent permitted by law.\n" +
                    "\n" +
                    "Written by Torbjorn Granlund and Richard M. Stallman.")
            raise SystemExit

        elif currentArgument in ('-n', '--number'):

            with open(sys.argv[-1], 'r') as f:
                count = 0
                for line in f:
                    count += 1
                    sys.stdout.write(f'     {count} {line}')
                raise SystemExit

        elif currentArgument in ('-b', '--number-noblank'):

            with open(sys.argv[-1], 'r') as f:
                count = 0
                for line in f:
                    if line == "\n":
                        sys.stdout.write("\n")
                    else:
                        count += 1
                        sys.stdout.write(f'     {count} {line}')
            raise SystemExit

        elif currentArgument in ('-E', '--show-ends'):

            with open(sys.argv[-1], 'r') as f:
                for line in f:
                    line = line.rstrip('\n') + '$'
                    sys.stdout.write(line+'\n')
            raise SystemExit

        elif currentArgument in ('-s', '--squeeze-blank'):

            with open(sys.argv[-1], 'r') as f:
                sys.stdout.write(re.sub(r'\n+','\n',f.read()))
            raise SystemExit

        elif currentArgument in ('-T', '--show-tabs'):

            with open(sys.argv[-1], 'r') as f:
                sys.stdout.write(re.sub(r'\t','^I',f.read()))
            raise SystemExit

except getopt.error as err:
    print(str(err))

for i in argumentList:
    
    if i == '-':
        for line in sys.stdin:
            sys.stdout.write(line)
    
    if not os.path.exists(i):
        sys.exit(f'File does not exsist: {i}')

    with open(i, 'r') as f:
        sys.stdout.write(f.read())

    f.close()
