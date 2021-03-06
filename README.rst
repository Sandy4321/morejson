morejson
#########

|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

``morejson`` is a drop-in replacement for Python's ``json`` that handles additional built-in Python types.

.. code-block:: python

  import morejson as json
  import datetime

  json.dumps({'now': datetime.datetime.now()})
  json.dumps({'set': set([1,2]), 'complex': complex(32, -4)})

.. contents::

.. section-numbering::


Installation
============

Install ``morejson`` with:

.. code-block:: bash

  pip install morejson


Use
===

``morejson`` implements the exact same API as Python's built-in ``json`` module; the ``dump``, ``dumps``, ``load`` and ``loads`` methods wrap around their ``json`` counterparts without changing their interface, while any other function or attribute is left unchanged.

You can use any argument of these methods, including ``default``, ``cls`` and ``object_hook``; ``morejson`` will wrap around any kind of custom behaviour you provide, giving it priority over ``morejson``'s encoding or decoding, and allowing you to use it with any custom JSON encoding/decoding code you have.


Supported Types
===============

Built-in Types
--------------

* set
* frozenset
* complex

datetime module types
---------------------

* date
* time
* datetime
* timedelta
* timezone


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/morejson.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd morejson
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests, use:

.. code-block:: bash

  nosetests --cover-erase --with-coverage --cover-package=morejson -d


Adding documentation
--------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).

Inspired by a great Github gist by abhinav-upadhyay: https://gist.github.com/abhinav-upadhyay/5300137


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/morejson.svg
  :target: https://pypi.python.org/pypi/morejson

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/morejson.svg
   :target: https://pypi.python.org/pypi/morejson

.. |Build-Status| image:: https://travis-ci.org/shaypal5/morejson.svg?branch=master
  :target: https://travis-ci.org/shaypal5/morejson

.. |LICENCE| image:: https://img.shields.io/pypi/l/morejson.svg
  :target: https://pypi.python.org/pypi/morejson

.. |Codecov| image:: https://codecov.io/github/shaypal5/morejson/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/morejson?branch=master