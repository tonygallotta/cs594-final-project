import numpy as np
import sys
import yt
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank() + int(sys.argv[1])

if rank < 2:
  sys.exit()
prefix = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/"
file = prefix + "ds14_scivis_0128_e4_dt04_{:.04f}".format(rank / 100.0)
ds = yt.load(file)
ad = ds.all_data()
ds.domain_left_edge = np.floor(ds.domain_left_edge.astype(np.float64))
ds.domain_right_edge = np.ceil(ds.domain_right_edge.astype(np.float64))
ds.domain_width = ds.domain_width.astype(np.float64)
ds.domain_center = ds.domain_center.astype(np.float64)
p = yt.ProjectionPlot(ds, 0, 'dark_matter_density', weight_field=None)
p.set_cmap(field="dark_matter_density", cmap='Beach_r')
plot = p.plots['deposit', 'dark_matter_density']
plot.hide_axes()
plot.hide_colorbar()

p.save("output/beach{:0>3d}.png".format(rank))
p.set_cmap(field="dark_matter_density", cmap='GREEN')
p.save("output/green{:0>3d}.png".format(rank))
p.set_cmap(field="dark_matter_density", cmap='BLUE')
p.save("output/blue{:0>3d}.png".format(rank * 100))
p.set_cmap(field="dark_matter_density", cmap='STD GAMMA-II')
p.save("output/STD_GAMMA-II{:0>3d}.png".format(rank))
p.set_cmap(field="dark_matter_density", cmap='PRISM_r')
p.save("output/PRISM_r{:0>3d}.png".format(rank * 100))
p.set_cmap(field="dark_matter_density", cmap='afmhot')
p.save("output/afmhot_r{:0>3d}.png".format(rank))
