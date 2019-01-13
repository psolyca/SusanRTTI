# ClassInformer python
# Nicolas Guigo / NCC Group
# Tyler Colgan / NCC Group
# 03/2017

import idaapi
idaapi.require("utils")
idaapi.require("msvc")
idaapi.require("gcc")
idaapi.require("classdiagram")
from idaapi import autoIsOk
from msvc import run_msvc
from gcc import run_gcc
from classdiagram import ClassDiagram

def show_classes(classes):
    c = ClassDiagram("Class Diagram", classes)
    c.Show()

def isGcc():
    gcc_info = find_binary(0x0, SEARCH_CASE|SEARCH_DOWN, "4e 31 30 5f 5f 63 78 78 61 62 69 76 31 31 37 5f 5f 63 6c 61 73 73 5f 74 79 70 65 5f 69 6e 66 6f 45")
    return gcc_info != BADADDR

def main():
    print "Starting ClassInformerPython"
    if autoIsOk():
        classes = run_gcc() if isGcc() else run_msvc()
        print classes
        show_classes(classes)
    else:
        print "Take it easy, man"
    print "Done"

if __name__ == '__main__':
    main()
