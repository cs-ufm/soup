import sys, getopt
import os

MYNAME = "Abner"

def main(argv):
   inputfile = ''
   outputfile = ''
   programa = len(sys.argv)

   try:
      print(F"My name is {MYNAME}")
      if (programa == 1):
          os.system("python portal.py")
          os.system("python estudios.py")
          os.system("python CS.py")
          os.system("python directorio.py")
      else:
          ejecutar = int(sys.argv[1])
          if(ejecutar == 1):
              os.system("python portal.py")
          elif(ejecutar == 2):
              os.system("python estudios.py")
          elif(ejecutar == 3):
              os.system("python CS.py")
          elif(ejecutar == 4):
              os.system("python directorio.py")
          else:
              print("No se indico el programa a ejecutar")

   except getopt.GetoptError:
      sys.exit(2)


if __name__ == "__main__":
   main(sys.argv)