import os
from subprocess import call


call(["pdflatex", os.path.join("src", "main.tex")])
