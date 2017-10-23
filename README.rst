pretty-json
===========

make pretty json.

Documentation: https://github.com/devstuff-io/pretty-json


Installation
------------

.. code-block:: shell

   pip install pretty-json


Environment Variables
---------------------

``PJSON_OUTPUT_STYLE``
......................

**Default**: monokai

The pygments_ formatter used to make the json pretty.


Usage
-----

.. code-block:: python

   from pretty_json import format_json

   # format_json(content, style=OUTPUT_STYLE)
   print format_json({'key': 'value'})


**See and sample the available styles**

.. code-block:: shell

   python -c "from pretty_json import sample;sample('manni')"


Authors
-------

See contributors section on GitHub.


.. _pygments: http://pygments.org/docs/styles/
