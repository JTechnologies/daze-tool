#!/usr/bin/env python
import sys
import os
import argparse
def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
if len(sys.argv)>=2:
    if sys.argv[1]=="compile":
        if len(sys.argv)==4:
            inFile = sys.argv[2]
            outFile = sys.argv[3]
            with open(inFile,'r') as i:
                lines = i.read()
                with open(outFile,'w') as o:
                    o.write(toHtml(lines))
        elif len(sys.argv)>4:
            print("daze: Too many arguments")
        elif len(sys.argv)==3:
            print("daze: No output file specified")
        elif len(sys.argv)==2:
            print("daze: No input file specified")
        else:
            print("daze: Internal Error 0x01")
    elif sys.argv[1]=="help":
        print("""
        Usage: daze [options] [command]

        Options:
          -e, --engine ENGINE BRANCH               Select the engine to use. Will automatically pull.
          -p, --pull-engine ENGINE BRANCH          Download an engine branch.
          -v, --version                            Print the version of daze-tool.
        Commands:
          compile: Compiles the input file into an html file (daze compile <input> <output>)
          help: Shows this help message
          version: Shows the version of daze-tool
          update: Pulls the latest version of daze-lang
        """)
    else:
        print(f"daze: invalid command {sys.argv[1]}. Try 'daze help' to see available commands.")
else:
    print("daze: no command. Try 'daze help' to see available commands.")
