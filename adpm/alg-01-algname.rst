[Algorithm name] - ALG-001
==========================

.. _alg-001:

Overview
--------

[Objective or purpose of the algorithm, rationale for the selected method and
the specifications it supports. Comparison analysis of different methods and
trade-offs, including rationale of the choice, to be provided in a separate TN
or justification file when relevant.]


Inputs and outputs
------------------

[VDT containing all the inputs, outputs, physical constants, parameters and
variables used in the algorithm. The VDT shall be self-contained, with all the
relevant information to understand the algorithm, including the origin and
destination of each variable, and the reference to the corresponding processing
block or product.]

.. list-table:: ALG-001 Variable Description Table (VDT).
    :header-rows: 1
    :class: longtable
    :widths: 16 7 8 16 16 7 12 10 12 12

    * - Name
      - Sym
      - Role
      - Origin
      - Destination
      - Units
      - Type
      - Dim
      - Range
      - Default
    * - ``x_i``
      - :math:`x_{i}`
      - IN
      - Input product
      - ALG-001
      - s
      - float
      - (n,)
      - [0, 5]
      - N/A
    * - ``exp_decay``
      - :math:`p`
      - IN
      - Configuration
      - ALG-001
      - :math:`s^{-1}`
      - float
      - Scalar
      - (0, 10]
      - 0.8
    * - ``resp``
      - :math:`y`
      - OUT
      - ALG-001
      - Output product
      -
      - float64
      - (n,)
      - [0, 1)
      - N/A


Mathematical formulation
------------------------

[Complete, self-contained mathematical description of the algorithm, in terms of
equation and formulas (with the same identifiers and symbols used in the VDT),
avoiding omitting relevant parts of the mathematical formulation in favor of
external references. Add the intermediate equations and steps, definitions and
conventions required to understand the formulation.]

example:

The output is computed as a normalized cumulative exponential response:

.. math::
    :label: eq-model

    y_i
    = p \int_{0}^{x_i} \exp(-p\xi)\,d\xi
    = 1-\exp(-p x_i),
    \qquad i=0,\ldots,n-1 .


Approximations and assumptions
------------------------------

[Description of the approximations and assumptions made in the algorithm
including a short analysis of the induced errors. More detailed error analyses
can be provided in dedicated appendices if needed. A parametric demonstration of
the approximation impact can be provided in form of plots, providing context and
justification to the assumptions made in the algorithm, when needed.]

example:

.. toctree::
    :maxdepth: 4

    notebooks/alg-001_approximation_example


Uncertainty propagation and evaluation
--------------------------------------

[Uncertainty propagation model description, detailed in dedicated appendices if
needed.]


Numerical implementation
------------------------

[For each project algorithm, extend the numerical description with:

- Details about methods for the numerical implementation.
- Clear identification of default and optional sub-steps, description of trigger
  conditions for sub-step activation, and possible switches to select among
  alternative algorithms or sub-steps. The configuration parameters controlling
  these switches shall be included in the inputs table with their default values
  and a reference to the applicable configuration-file document.
- Description of possible implementation issues.
- Analysis of algorithm complexity and possible criticalities in terms of
  computational load and use of system resources.
- Concurrency: independent blocks, data dependencies, parallelization strategy,
  synchronization requirements, and scalability performance.
- Expected performance.]

Example:

Equation :eq:`eq-model` is evaluated with the composite trapezoidal rule. For
each input :math:`x_i`, a uniform grid :math:`\xi_0,\ldots,\xi_{m-1}` is
generated over :math:`[0,x_i]` and:

.. math::
    :label: eq-model-discrete

    y_i^{(m)}
    = p\sum_{k=1}^{m-1}
    \frac{\xi_k-\xi_{k-1}}{2}
    \left[
    \exp(-p\xi_{k-1})+\exp(-p\xi_k)
    \right].

.. toctree::
    :maxdepth: 4

    notebooks/alg-001_numerical_implementation

See also the
:download:`the ALG-001 demonstrator <notebooks/alg-001_numerical_implementation.ipynb>`
Jupyter Notebook for a demonstration of the numerical implementation.


Validation guidelines
---------------------

[Description of the inputs for the definition of the validation approach, where
relevant.]
