========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/test_gui/badge/?style=flat
    :target: https://readthedocs.org/projects/test_gui
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/test_gui.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/test_gui

.. |commits-since| image:: https://img.shields.io/github/commits-since/vadella/test_gui/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/vadella/test_gui/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/test_gui.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/test_gui

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/test_gui.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/test_gui

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/test_gui.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/test_gui


.. end-badges

testing Pyside

* Free software: Apache Software License 2.0

Installation
============

::

    pip install test_gui

Documentation
=============

https://test_gui.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
