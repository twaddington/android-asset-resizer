"""
"""

import os

from PIL import Image

"""
iOS@2x = xhdpi

    2x * .375 = ldpi
    2x * .75  = hdpi
    2x * .50  = mdpi
    2x * 1.5  = xxhdpi
"""

DENSITY_TYPES = ('ldpi', 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi')

def mkres(path):
    """
    Creates a directory tree for the resized Android assets.
    """
    for d in DENSITY_TYPES:
        os.makedirs('%s/res/drawable-%s' % (os.path.abspath(path), d), 0755)

def resize(path, out, density='xhdpi', prefix='', filter=Image.ANTIALIAS):
    print 'resizing!'
    return

    """
    for path in args.pattern:
        # TODO: Verify this is a file
        if os.path.isfile(path):
            print path
            try:
                im = Image.open(path)
                
                w, h = im.size

                # TODO: Function for calculating out width and height
                size = (int(w * .75), int(h * .75))
                print im.size
                print size

                _, filename = os.path.split(path)

                # Try other options, provide setting? Try BILINEAR?
                # TODO: Make this a method!
                # TODO: drawable-xhdpi dir!
                # TODO: Replace '@2x'
                # TODO: Add prefix!
                im.resize(size, Image.ANTIALIAS).save(os.path.join(out, filename))
            except IOError:
                pass
    """
