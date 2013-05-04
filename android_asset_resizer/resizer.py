"""
"""

import os

from PIL import Image

"""
3:4:6:8:12

xhdpi * .375 = ldpi
xhdpi * .50  = mdpi
xhdpi * .75  = hdpi
xhdpi * 1.0  = xhdpi
xhdpi * 1.5  = xxhdpi

    3 / 8   = ldpi
    4 / 8   = mdpi
    6 / 8   = hdpi
    8 / 8   = xhdpi
    12 / 8  = xxhdpi

xxhdpi / .375 = ldpi
xxhdpi / .50  = mdpi
xxhdpi / .75  = hdpi
xxhdpi / 1.5  = xhdpi
xxhdpi / 1    = xxhdpi

    3 / 12   = ldpi
    4 / 12   = mdpi
    6 / 12   = hdpi
    8 / 12   = xhdpi
    12 / 12  = xxhdpi

current_size * (target_density / current_density) = target_size

24w * (3 / 6)   = 12w # hdpi to ldpi
24w * (4 / 6)   = 16w # hdpi to mdpi
24w * (6 / 6)   = 24w # hdpi to hdpi
24w * (8 / 6)   = 32w # hdpi to xhdpi
24w * (12 / 6)  = 48w # hdpi to xxhdpi

24w * (3 / 8)   = 9w  # xhdpi to ldpi
24w * (4 / 8)   = 12w # xhdpi to mdpi
24w * (6 / 8)   = 18w # xhdpi to hdpi
24w * (8 / 8)   = 24w # xhdpi to xhdpi
24w * (12 / 8)  = 36w # xhdpi to xxhdpi

24w * (3 / 12)  = 6w  # xxhdpi to ldpi
24w * (4 / 12)  = 8w  # xxhdpi to mdpi
24w * (6 / 12)  = 12w # xxhdpi to hdpi
24w * (8 / 12)  = 16w # xxhdpi to xhdpi
24w * (12 / 12) = 24w # xxhdpi to xxhdpi

"""

DENSITY_TYPES = ('ldpi', 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi')
DENSITY_MAP = {
    'ldpi': float(3),
    'mdpi': float(4),
    'hdpi': float(6),
    'xhdpi': float(8),
    'xxhdpi': float(12),
}

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

    def get_out_for_density(self, target_density):
        """
        Return the out directory for the given target density.
        """
        return os.path.join(self.out, 'res/drawable-%s' % target_density)

    def get_size_for_density(self, size, target_density):
        """
        current_size * (target_density / current_density) = target_size
        """
        current_size = size
        current_density = DENSITY_MAP[self.source_density]
        target_density = DENSITY_MAP[target_density]

        #print "%s * (%s / %s)" % (current_size, target_density, current_density)
        return int(current_size * (target_density / current_density))

    def resize(self, path):
        """
        """
        im = Image.open(path) 

        # ...
        _, filename = os.path.split(path)

        # ...
        filename = '%s%s' % (self.prefix if self.prefix else '', filename.replace('@2x', ''))

        # ...
        w, h = im.size

        # ...
        for d in DENSITY_TYPES:
            # TODO: Don't resize if source_density == d, just move and rename
            size = (self.get_size_for_density(w, d), self.get_size_for_density(h, d))

            #print '%s => %s: %s => %s' % (self.source_density, d, im.size, size)

            # ...
            out_file = os.path.join(self.out, self.get_out_for_density(d), filename)
            #print 'Saving to %s' % out_file

            # ...
            im.resize(size, Image.ANTIALIAS).save(out_file)
