# -*- coding: utf-8 -*-
print('=' * 40)
print(__file__)
from helper.textool import get_tmp_file

################################################################################
import fiona
c = fiona.open('/gdata/GSHHS_c.shp', 'r')
c.closed

################################################################################
next(c)
len(c)

################################################################################

################################################################################
from pprint import pprint
with fiona.open('/gdata/GSHHS_c.shp') as src:
    pprint(src[1])


################################################################################

try:
    with fiona.open('/gdata/GSHHS_c.shp') as c:
        print(len(list(c)))

except:
    print(c.closed)
    raise


################################################################################

c = fiona.open('/gdata/GSHHS_c.shp')
c.driver

################################################################################
c.crs

################################################################################
from fiona.crs import to_string
to_string(c.crs)

################################################################################
from fiona.crs import from_string
from_string("+datum=WGS84 +ellps=WGS84 +no_defs +proj=longlat")

################################################################################
from fiona.crs import from_epsg
from_epsg(3857)

################################################################################
len(c)

################################################################################
c.bounds
