from mpi4py import MPI
import matplotlib; matplotlib.use('Agg')
import matplotlib.pylab as pl
import sys
import yt
import numpy as np
from enhance import enhance
from yt.utilities.sdf import load_sdf
from yt.utilities.lib.image_utilities import add_rgba_points_to_image

filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"
midx = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000.midx10"
bbox = np.array([[0.0, 0.0, 0.0],
                 [100*1e3, 100*1e3, 100*1e3]])

print bbox
ds = yt.load(filename,
                midx_filename=midx,
                bounding_box = bbox,
                )

ds.domain_left_edge = ds.domain_left_edge.astype(np.float64)
ds.domain_right_edge = ds.domain_right_edge.astype(np.float64)
ds.domain_width = ds.domain_width.astype(np.float64)
ds.domain_center = ds.domain_center.astype(np.float64)

ad = ds.all_data()
Npix = 1024
image = np.zeros([Npix, Npix, 4], dtype='float64')

cbx = yt.visualization.color_maps.mcm.RdBu
col_field = ad['particle_velocity_z']

# Calculate image coordinates ix and iy based on what your view width is
#
ix = (ad['particle_position_x'] - ds.domain_left_edge[0])/ds.domain_width[0]
iy = (ad['particle_position_y'] - ds.domain_left_edge[1])/ds.domain_width[1]
#
col_field = (col_field - col_field.min()) / (col_field.mean() + 4*col_field.std() - col_field.min())
add_rgba_points_to_image(image, ix.astype('float64'), iy.astype('float64'), cbx(col_field))
#

yt.write_bitmap(enhance(image), 'enhanced.png')
print 'Splatted %i particles' % ad['particle_position_x'].size
