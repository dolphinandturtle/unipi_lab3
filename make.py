import os
import sys
from subprocess import call


if len(sys.argv) < 2:
    call(["pdflatex", os.path.join("src", "main.tex")])

elif sys.argv[1] == "clean":
    call(["rm", "-f", "main.aux"])
    call(["rm", "-f", "main.log"])
    call(["rm", "-f", "main.pdf"])


