"""
Copyright 2013 Tristan Waddington

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import sys
import argparse

from PIL import Image

"""
iOS@2x = xhdpi

    2x * .375 = ldpi
    2x * .75  = hdpi
    2x * .50  = mdpi
    2x * 1.5  = xxhdpi


aar --source=xxhdpi,xhdpi,ios2x --prefix=ic,ic_launcher,ic_menu,ic_stat_notify,ic_tab,ic_dialog *2x.png out/

global_nav-chart-icon-selected@2x.png => res/drawable-xhdpi/ic_global_nav-chart-icon-selected.png
"""

SOURCE_DENSITY_CHOICES = ('xxhdpi', 'xhdpi',)
DEFAULT_OUT_PATH = '%s/res' % os.getcwd()
DEFAULT_OUT_MODE = 0755

O = ('drawable-xxhdpi', 'drawable-xhdpi', 'drawable-hdpi', 'drawable-mdpi', 'drawable-ldpi')

def main():
    # ...
    parser = argparse.ArgumentParser(description='Process some images.')

    # ...
    # TODO: Add ldpi option
    # TODO: Add filter argument for PIL
    parser.add_argument('-d', '--density', default='xhdpi', choices=SOURCE_DENSITY_CHOICES,
            help='the density of the source images')
    parser.add_argument('-p', '--prefix',
            help='a prefix to add to the filename')
    parser.add_argument('-o', '--out',
            help='the path to the output directory')
    parser.add_argument('pattern', nargs='+',
            help='the path to the source images')

    # ...
    args = parser.parse_args()
    print args.density
    print args.prefix
    print args.out

    # TODO: Validate args.out
    # - Is a directory?
    # - Is empty? if not os.listdir(work_path):
    # - Is writeable?

    print DEFAULT_OUT_PATH

    if args.out:
        out = os.abspath(args.out)
    else:
        out = DEFAULT_OUT_PATH

    print out

    # Create the output directory
    try:
        os.mkdir(out, DEFAULT_OUT_MODE)
    except OSError as e:
        pass

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

if __name__ == "__main__":
    sys.exit(main())
