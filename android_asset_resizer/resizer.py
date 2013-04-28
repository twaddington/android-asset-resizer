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

class AssetResizer():
    """
    """
    def __init__(self, out, source_density='xhdpi', prefix='',
            filter=Image.ANTIALIAS):
        self.out = os.path.abspath(out)
        self.source_density = source_density
        self.prefix = prefix
        self.filter = filter

    def mkres(self):
        """
        Creates a directory tree for the resized Android assets.
        """
        for d in DENSITY_TYPES:
            try:
                path = os.path.join(self.out, 'res/drawable-%s' % d)
                os.makedirs(path, 0755)
            except OSError:
                pass

    def resize(self, path):
        """
        """
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
        #im.resize(size, Image.ANTIALIAS).save(os.path.join(out, filename))
