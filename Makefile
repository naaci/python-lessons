nbconvert:
	uv pip install jupyter[nbconvert]
	tlmgr install xetex latex mfware tcolorbox pdfcol parskip float upquote eurosym fontspec unicode-math grffile adjustbox titling booktabs ulem soul jknapltx rsfs bibtex

pdf/%.pdf: nb/%.ipynb
	uv run jupyter-nbconvert --to qtpdf $< --output-dir pdf
