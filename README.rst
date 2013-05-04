android-asset-resizer
=====================

Requirements
------------

- PIL (tested with version ``1.1.7``, may work with earlier versions)

Installing
----------

::

    $ pip install android-asset-resizer

Examples
--------

You can easily generate Android assets from your ``@2x`` iOS assets:

::

    $ adresize assets/icon@2x.png

Running the previous command will create the following assets:

::

    - res
      - drawable-ldpi
        - icon.png
      - drawable-mdpi
        - icon.png
      - drawable-hdpi
        - icon.png
      - drawable-xhdpi
        - icon.png

These assets were created from the original ``@2x`` asset where the icon in
the ``drawable-xhdpi`` folder is just a copy of the original.

You can also resize an entire directory of images:

::

    $ adresize assets/*@2x.png

An Android ``xhdpi`` asset is roughly equivalent to an ``@2x`` asset, so you
can easily resize those too:

::

    $ adresize res/drawable-xhdpi/*.png

If you have a large ``drawable-xxhdpi`` asset you can use the ``--density``
flag to generate the smaller assets:

::

    $ adresize res/drawable-xxhdpi/*.png --density=xxhdpi

Publishing
----------

::

    # Register with pypi (only done once)
    $ python setup.py register

    # First create a source distribution
    $ python setup.py sdist

    # Upload the distribution to pypi
    $ python setup.py upload

License
-------

See the LICENSE_ file.

.. _LICENSE: https://github.com/twaddington/android-asset-resizer/blob/master/LICENSE 

