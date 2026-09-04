##############
 Introduction
##############


Purpose and scope
=================

This document describes the algorithms, and models [Processor Name] to generate
[Product Name]. It provides the theoretical and technical basis of the
processing chain, including the definition of inputs and outputs, mathematical
formulations, processing steps, auxiliary data usage, retrieval and correction
methods, and associated assumptions and uncertainties evaluation.


Document structure
==================

.. todo:: Use the ``:ref:`` or the ``:doc:`` directive to create cross-links

The document is structured as follows:

- :doc:`Chapter 1 </01_introduction/introduction>` provides the purpose and
  scope, the structure of the document, the applicable and reference documents,
  and the list of acronyms, definitions, conventions, and symbols.

- :doc:`Chapter 2 </02_state_of_the_art/state_of_the_art>` provides the
  state-of-the-art of the algorithms and processing blocks.

- :doc:`Chapter 3 </03_processing_model/processing_model>` gives the top-down
  processing model and data flow.

- :doc:`Chapter 4 </04_step_01_stepname/stepname>` and
  :doc:`Chapter 5 </05_step_02_stepname/stepname>`, and
  :doc:`Chapter 6 </06_step_03_stepname/stepname>` describe the processing steps
  and their algorithms, including variable definitions, mathematical
  formulation, uncertainty and validation.

- :ref:`Appendices <appendices>` contains optional appendices.


Applicable and reference documents
==================================

.. only:: latex

    Applicable and reference documents can be found th the ``Bibliography``
    section.

    Applicable documents are identified by IDs stating with the ``AD`` prefix
    (e.g. ``[AD01]``), while reference documents are identified by the ``RD``
    prefix (e.g. ``[RD01]``).

.. only:: not latex

    Applicable documents
    --------------------

.. [AD1] [Document code] [Project SoW / system or product requirements]
.. [AD2] ESA-EOPG-EOPGMQ-RS-2023-4, ADPM requirements, Issue/Revision 1.3


.. only:: not latex

    Reference documents
    -------------------

.. [RD1] `The Python Programming Language <https://www.python.org>`_

.. [RD2] `Sphinx Python Documentation Generator <https://www.sphinx-doc.org>`_
         Documentation generator reference
.. [RD3] `Jupyter Project <https://jupyter.org>`_
         Interactive scientific-computing framework
.. [RD4] `QA4EO — A guide to expression of uncertainty of measurements
         <https://qa4eo.org/docs/QA4EO-QAEO-GEN-DQK-006_v4.0.pdf>`_.
         Last accessed on 09/06/2026.
.. [RD5] `reStructuredText format <https://docutils.sourceforge.io/rst.html>`_
.. [RD6] `CEOS — Jupyter Notebooks Best Practice, Issue 1.1, 2024
         <https://ceos.org/document_management/Working_Groups/WGISS/Documents/WGISS%20Best%20Practices/CEOS_JupterNotebooks_Best%20Practice_v1.1.pdf>`_
.. [RD7] [IODD/ICD and configuration schema]


List of acronyms
================

.. glossary::
    :sorted:

    AD
        Applicable Document

    ADPM
        Algorithms Description and Processing Model

    ATBD
        Algorithm Theoretical Baseline Document

    CEM
        Copernicus Expansion Missions

    DPM
        Detailed Processing Model

    ESA
        European Space Agency

    ICD
        Interface Control Document

    IODD
        Input Output Description Document

    PM
        Processing Model

    QA4ECV
        Quality Assurance for Essential Climate Variables

    RD
        Reference Document

    SAR
        Synthetic Aperture Radar

    SoW
        Statement of Work

    SW
        Software

    SRD
        Software Requirements Document

    TN
        Technical Note

    VDT
        Variables Description Table

    V&V
        Verification and Validation


Definitions and conventions
===========================

.. glossary::
    :sorted:

    Processing step
        Logical group of operations, possibly divided into sub-steps.

    [Project term]
        [Definition consistent with the IODD, ICD, code and validation
        documents.]

        Multi-paragraph definition.


List of symbols
===============

.. list-table:: List of symbols.
    :header-rows: 1
    :widths: 25 75

    * - Symbol
      - Description
    * - :math:`\lambda`
      - RADAR wavelength.
    * - :math:`c`
      - Speed of light in the vacuum.
    * - :math:`...`
      - TBW
