import matplotlib; matplotlib.use('Agg')
import yt
import numpy as np
from enhance import enhance
from yt.utilities.lib.image_utilities import add_rgba_points_to_image
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if len(sys.argv) >= 2:
  missing = np.fromfile("missing", dtype=np.int, sep="\n")
  offset = missing[rank] * 1e3
else:
  offset = rank * 1e3

filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"
midx = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000.midx10"
# 1e3 = 1 Mpc
center = np.array([-2505805.31114929, -3517306.7572399, -1639170.70554688]) + np.array([0, 0, offset])
width = 50.0e3 # 5 Mpc
bbox = np.array([center-width/2, center+width/2])

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
ix = (ad['particle_position_x'] - ds.domain_left_edge[0])/ds.domain_width[0]
iy = (ad['particle_position_y'] - ds.domain_left_edge[1])/ds.domain_width[1]

col_field = (col_field - col_field.min()) / (col_field.mean() + 4*col_field.std() - col_field.min())
add_rgba_points_to_image(image, ix.astype('float64'), iy.astype('float64'), cbx(col_field))

yt.write_bitmap(enhance(image), 'splat{:0>4d}.png'.format(rank))
print 'Splatted %i particles' % ad['particle_position_x'].size
