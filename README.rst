Springboard IoGT Uganda
=======================

.. image:: https://travis-ci.org/universalcore/springboard-iogt-ug.svg?branch=develop
    :target: https://travis-ci.org/universalcore/springboard-iogt-ug
    :alt: Continuous Integration

.. image:: https://coveralls.io/repos/universalcore/springboard-iogt-ug/badge.png?branch=develop
    :target: https://coveralls.io/r/universalcore/springboard-iogt-ug?branch=develop
    :alt: Code Coverage

.. image:: https://readthedocs.org/projects/springboard/badge/?version=latest
    :target: https://springboard.readthedocs.org
    :alt: Springboard Documentation

Installing for local dev
~~~~~~~~~~~~~~~~~~~~~~~~

Make sure elasticsearch_ is running, then::

    $ git clone https://github.com/universalcore/springboard-iogt-ug.git
    $ cd springboard-iogt-ug
    $ virtualenv ve
    $ source ve/bin/activate
    (ve)$ pip install -e .
    (ve)$ springboard bootstrap -v
    (ve)$ pserve development.ini --reload


.. _elasticsearch: http://www.elasticsearch.org
