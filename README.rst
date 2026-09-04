############################################################################
ESA-GMQ Algorithms Description and Processing Model (ADPM) document template
############################################################################

The template exploits `Sphinx <https://www.sphinx-doc.org>`_ documentation
system.
The narrative content is expected to be written in ``reStructuredText``
(with Sphinx extensions) while executable
`Jupyter Notebooks <https://jupyter.org>`_ are integrated through
`nbsphinx <https://nbsphinx.readthedocs.io>`_ Sphinx extension.


.. important::

    This template is still under heavy development and subject to changes.

    It is only provided as guideline for the document organization and the
    expected sections/contents.

    The aspects related to the style and themes shall not be considered as
    a reference.


Prerequisites
=============

The build requires:

* Python 3.11 or newer
* the Python packages listed in the ``requirements.txt`` file
* a LaTeX distribution providing ``latexmk`` for PDF output
* a working installation of the pandoc tool


Environment setup
=================

The installation of the Python (or conda/mamba) and LaTeX pre-requisites
have to be done by the user exploiting the OS specific installers and
package managers.

The Python environment and Pandoc can be installed as described in the
following sub sections.


Python venv
-----------

::

   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt


Conda/mamba environment
-----------------------

::

   mamba create --name adpm --file environment.yml
   mamba activate adpm


Build
=====

Build the interactive HTML version with::

   make html

The entry point is ``adpm/_build/html/index.html``.

Build the PDF version with::

   make pdf

The final PDF is ``adpm/_build/latex/adpm.pdf``.


Source structure
----------------

::

   adpm/
   ├── 01_introduction/
   │   └── introduction.rst
   ├── 02_state_of_the_art/
   │   └── state_of_the_art.rst
   ├── 03_processing_model/
   │   ├── processing_model.rst
   │   └── images/
   │       ├── atbd_diagram_example.drawio
   │       └── atbd_diagram_example.png
   ├── 04_step_01_stepname/
   │   ├── stepname.rst
   │   ├── alg_01_algname/
   │   │   ├── algname.rst
   │   │   ├── approximation_example.ipynb
   │   │   └── numerical_implementation.ipynb
   │   └── alg_02_algname/
   │       └── algname.rst
   ├── 05_step_02_stepname/
   │   ├── stepname.rst
   │   ├── alg_03_algname/
   │   │   └── algname.rst
   │   └── alg_04_algname/
   │       └── algname.rst
   ├── 06_step_03_stepname/
   │   ├── stepname.rst
   │   └── alg_05_algname/
   │       └── algname.rst
   ├── 07_appendices/
   │   ├── appendices.rst
   │   └── a01_appendix_name.rst
   ├── _static/
   ├── conf.py
   ├── index.rst
   ├── Makefile
   └── make.bat


License
=======

Copyright 2026 GMQ Team

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

To Do
=====

* [ ] Explore more/alternative examples to integrate the Jupyter notebooks
  within the narrative sections of the document
* [ ] Provide a more exhaustive example for the algorithms description section
  and its numerical implementation in form of Jupyter notebooks
