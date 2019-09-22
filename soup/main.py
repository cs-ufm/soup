import sys
from portal import Portal
from request import Request
#print ('Argument List:', str(sys.argv))

#Instance of request class, in order to DRY
request = Request()

#main class to verify args from running process
def main(args):
    #print(args)
    #print(args.__contains__("1"))

    #array to set the print result
    result = [""]

    #call the correct methods according to the args
    if len(args) == 0:
        result = runAll(result)
    elif args.__contains__("1"):
        result = portal(result)
    
    printResult(result)

#portal method that instances the Portal class and run it
def portal(result):
    result.insert(0, "=============================")
    result.insert(0, "1. Portal")
    portalSoup = request.makeGet("http://ufm.edu/Portal")
    portal = Portal(portalSoup)
    portalArray = portal.init()
    print(portalArray)
    return result

#method defined if no args set
def runAll(result):
    result = result + portal(result)
    return result

#method to print results 
def printResult(result):

    result = ["Enrique Andres Bolanos Reyes", *result]

    if len(result) > 30:
        #method to print result in file
        pass
    else:
        for i in result:
            print(i)

#main method in which I get the args from the running process
if __name__ == "__main__":
   main(sys.argv[1:])
