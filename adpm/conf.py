# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from string import Template

try:
    from pathlib import Path

    import pypandoc

    # Expose the Pandoc executable bundled with pypandoc-binary to nbsphinx and
    # nbconvert, avoiding a separate system installation.
    _pandoc_dir = str(Path(pypandoc.get_pandoc_path()).parent)
    os.environ["PATH"] = _pandoc_dir + os.pathsep + os.environ.get("PATH", "")
except ImportError:
    pass


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

doc_id = "[Document ID]"
doc_status = "[Draft / Approved]"
processor = "[Processor]"
project = f"{processor} - Algorithms Description and Processing Model"
author = "[Organization / authors]"
copyright = "[Year, copyrights holder]"
distribution = "ESA UNCLASSIFIED - Releasable to the Public"
release = "[Issue / Revision]"
today = "[YYYY-MM-DD]"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinx.ext.graphviz",
    # "sphinx.ext.ifconfig",
    # "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_rtd_theme",
    "nbsphinx",
]

try:
    import sphinxcontrib.spelling  # noqa: F401

    extensions.append("sphinxcontrib.spelling")
except ImportError:
    pass


root_doc = "index"
language = "en"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
templates_path = ["_templates"]


# --- Options for figure numbering -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-figure-numbering

numfig = True
numfig_secnum_depth = 1

# --- Options for Maths ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-maths

math_numfig = True


# --- Options for markup -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-markup

rst_prolog = f"""
.. |document-id| replace:: {doc_id}
.. |issue| replace:: {release}
.. |date| replace:: {today}
.. |status| replace:: {doc_status}
.. |processor| replace:: {processor}
.. |copyright| replace:: {copyright}
.. |distribution| replace:: {distribution}
"""

# --- Options for warning control --------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-warning-control

suppress_warnings = [
    "ref.citation",
    "nbsphinx",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {"collapse_navigation": False}
html_title = project
html_static_path = ["_static"]
html_show_sourcelink = True


# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# Sphinx provides the built-in LaTeX themes "manual" and "howto".
# Change this single value to select the PDF theme.
latex_theme = "manual"
latex_theme_options = {
    "papersize": "a4paper",
    "pointsize": "10pt",
}
# latex_engine = "xelatex"
latex_documents = [
    (
        root_doc,
        "adpm.tex",
        project,
        author,
        latex_theme,
    )
]
latex_appendices = [
    "A01_appendix_name",
]

# Keep only the required distribution marking; all other layout choices are
# delegated to the selected Sphinx theme.
latex_elements = {
    "preamble": Template(r"""
\usepackage{xcolor}
\usepackage[
    type={CC},
    modifier={by},
    version={4.0},
]{doclicense}

\newcommand{\docID}{${doc_id}}
\newcommand{\docversion}{${release}}
\newcommand{\doctitle}{${project}}
\newcommand{\docdist}{${distribution}}

\fancypagestyle{normal}{
  \fancyhf{}
  \fancyhead[L]{\color{gray}\docID}
  \fancyhead[C]{\color{gray}\doctitle}
  \fancyhead[R]{\color{gray}\docversion}
  \fancyfoot[L]{\doclicenseImage[imagewidth=1cm]}
  \fancyfoot[C]{\docdist} 
  \fancyfoot[R]{\small\thepage}
  \renewcommand{\headrulewidth}{0.0pt}
  \renewcommand{\footrulewidth}{0.0pt}
}
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[L]{\color{gray}\docID}
  \fancyhead[C]{\color{gray}\doctitle}
  \fancyhead[R]{\color{gray}\docversion}
  \fancyfoot[L]{\doclicenseImage[imagewidth=1cm]}
  \fancyfoot[C]{\docdist} 
  \fancyfoot[R]{\small\thepage}
  \renewcommand{\headrulewidth}{0.0pt}
  \renewcommand{\footrulewidth}{0.0pt}
}
\fancypagestyle{empty}{
  \fancyhf{}
  \fancyfoot[C]{\doclicenseImage[imagewidth=2cm]}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}
""").substitute(project=project, doc_id=doc_id, release=release, distribution=distribution),
}
latex_show_urls = "footnote"
latex_domain_indices = False


# -- Options for the linkcheck builder ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_allowed_redirects = {
    r"https://www\.sphinx-doc\.org(/.*)?": r"https://www\.sphinx-doc\.org/en/master(/.*)?",
}
linkcheck_ignore = [
    "https://docutils.sourceforge.io/*",
    # The following are not accessible via GHA
    "https://ceos.org/document_management/Working_Groups/WGISS/Documents/WGISS%20Best%20Practices/CEOS_JupterNotebooks_Best%20Practice_v1.1.pdf",
]


# --- sphinx.ext.napoleon ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

napoleon_google_docstring = False
napoleon_numpy_docstring = True


# --- sphinx.ext.todo --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#module-sphinx.ext.todo

todo_include_todos = True


# --- nbsphinx ---------------------------------------------------------------
# https://nbsphinx.readthedocs.io/en/0.9.8/configuration.html

# Execute notebooks from a clean state and fail the build on any notebook
# error. The Python kernel is installed by requirements.txt.
nbsphinx_execute = "always"
nbsphinx_allow_errors = False
nbsphinx_timeout = 120
nbsphinx_kernel_name = "python3"


# --- sphinxcontrb-spelling --------------------------------------------------
# https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html

spelling_lang = "en_US"
