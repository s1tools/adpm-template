#!/usr/bin/make -f

PYTHON ?= python3

.PHONY: help html pdf dist clean lint linkcheck doctest coverage spelling latexpdf

help:
	@echo "Main targets:"
	@echo "  html        to make standalone HTML files"
	@echo "  pdf         to make LaTeX and PDF files (default pdflatex)"
	@echo "  dist        to generate a tarball of the adpm template"
	@echo "  clean       to clean the working directory"
	@echo "  lint        to run the sphinx linter"
	@echo "  linkcheck   to check all external links for integrity"
	@echo "  doctest     to run all doctests embedded in the documentation (if enabled)"
	@echo "  coverage    to run coverage check of the documentation (if enabled)"
	@echo "  spelling    to run spell check of the documentation"

html latexpdf linkcheck doctest coverage spelling:
	$(MAKE) -C adpm $@

pdf: latexpdf

dist:
	$(PYTHON) -m build --sdist

clean:
	$(MAKE) -C adpm $@
	$(RM) -r adpm/_build
	$(RM) -r adpm_template.*-info
	$(RM) -r dist
	$(RM) -r .ruff_cache/

lint:
	sphinx-lint --max-line-length=80 --enable=all --ignore=adpm/_build adpm README.rst
	ruff check .

format:
	ruff format .
	docstrfmt -l 80 -s "#|=-*^+" adpm
