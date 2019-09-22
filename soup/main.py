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
    res = []
    res.append("=============================")
    res.append("1. Portal")
    portalSoup = request.makeGet("http://ufm.edu/Portal")
    por = Portal(portalSoup)
    portalArray = por.init()
    #print(portalArray)
    res = res + portalArray
    return res

#method defined if no args set
def runAll(result):
    result += portal(result)
    return result
#method to print results 
def printResult(result):

    result.insert(0, "Enrique Andres Bolanos Reyes")

    if len(result) > 30:
        #method to print result in file
        pass
    else:
        for i in result:
            print(i)

#main method in which I get the args from the running process
if __name__ == "__main__":
   main(sys.argv[1:])
