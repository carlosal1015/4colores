all:	example clean

example:
	pdflatex example.tex
	bibtex example
	alphabib -bs example.bbl
	pdflatex example.tex
	pdflatex example.tex

clean:
	rm -f example.aux example.bbl example.blg example.log example.out
