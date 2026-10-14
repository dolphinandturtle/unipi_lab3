# Introduction
Il file contiene la soluzione agli esercizi d'esami di *Laboratorio 3* e qualche accenno di teoria sporadico.

# How to make PDF
To *compile* the pdf, *python* is required (version >3.14.8)
from the command line use the following command.
```bash
python -BO make.py
```

# How to contribute (adding/modifying)

## Project structure
- Every used package is referenced inside `include.tex`
- Exercises are to put separately into files *pre*-ceded by "ex"
- The compilation is performed over `main.tex`
- Acknowledgements and guidelines may be added in `first.tex`

## Don't
- Add complicated/heavy packages, I want the project to be easy and accessible for people even in the future
- Don't *pull* for *aesthetic* changes
