import sys
import os
from portal import portal
from estudios import estudios
from CS import CS
from directorio import directorio
import sys, getopt
import os

def main(args):
    result = [""]
    if len(args) == 0:
        if os.environ['Modulo']:

            if os.environ['Modulo'] == "1":
                result = portal(result)
            elif os.environ['Modulo'] == "2":
                result = estudios(result)
            elif os.environ['Modulo'] == "3":
                result = CS(result)
            elif os.environ['Modulo'] == "4":
                result = directorio(result)
            else:
                result = runAll(result)
        else:
            result = runAll(result)
    elif args.__contains__("1"):
        result = portal(result)
    elif args.__contains__("2"):
        result = estudios(result)
    elif args.__contains__("3"):
        result = CS(result)
    elif args.__contains__("4"):
        result = directorio(result)
    printResult(result)

def runAll(result):
    result += portal(result)
    result += estudios(result)
    result += CS(result)
    result += directorio(result)
    return result

def printResult(result):
    result.insert(0, "Abner Xocop Chacach")
    for i in result:
        print(i)


if __name__ == "__main__":
   main(sys.argv)