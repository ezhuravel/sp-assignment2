# Name: Eugene Zhuravel, Ian Wodder, Israel Nolazco
# Date: 7/24/2019
# Course Name:CPSC-51100-003
# Semester: Summer 2018
# Assignment: Programming Assignment 2

import sys
import os

# Opens file in local directory, read each line and cast to a float
def openFile(filename):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    location = location + "\\" + filename
    lines = [float(x.rstrip()) for x in open(location)]
    return lines

# Entry point of application
def main(argv):
    #Print header 
    print "CPSC-51100, Summer 2019"
    print "NAME: Eugene Zhuravel. Iam Wodder, Israel Nolazco"
    print "PROGRAMMING ASSIGNMENT #2"
    print ""
        
    points = openFile("prog2-input-data.txt")

    number = float(raw_input("Enter the number of clusters: "))    
        
    pass

if __name__ == "__main__":
    main(sys.argv)

