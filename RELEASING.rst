Publishing
==========

::

    # Create some distributions
    #
    $ python setup.py sdist bdist_wheel

    # Register your project (if necessary):
    # One needs to be explicit here, globbing dist/* would fail.
    #
    $ twine register dist/project_name-x.y.z.tar.gz
    $ twine register dist/mypkg-0.1-py2.py3-none-any.whl

    # Upload with Twine
    #
    $ twine upload dist/*
