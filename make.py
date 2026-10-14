import os
import sys
from subprocess import call


if len(sys.argv) < 2:
    call(["pdflatex", "-jobname", "lab3ex", os.path.join("src", "main.tex")])

elif sys.argv[1] == "clean":
    call(["rm", "-f", "lab3ex.aux"])
    call(["rm", "-f", "lab3ex.log"])
    call(["rm", "-f", "lab3ex.out"])
