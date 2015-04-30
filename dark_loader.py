import yt
import numpy as np
from yt.utilities.sdf import load_sdf
from super_data import SuperData
from darksky_catalog import darksky

prefix = "http://darksky.slac.stanford.edu/simulations/"

def load_ds14_a(midx=None, bbox=None, a=1.0):
    if midx == True:
        midx = 10
    ds = darksky['ds14_a'].load(bounding_box = bbox, midx = midx)
    # the c code chokes on data types without these conversions
    ds.domain_left_edge = ds.domain_left_edge.astype(np.float64)
    ds.domain_right_edge = ds.domain_right_edge.astype(np.float64)
    ds.domain_width = ds.domain_width.astype(np.float64)
    ds.domain_center = ds.domain_center.astype(np.float64)
    return ds

def load_ds14_a_halos(midx=7, bbox=None, a=1.0):
    if a != 1.0:
        raise RuntimeError("Only a=1.0 allowed at this time.")
    ds = darksky['ds14_a']['halos_a_%0.4f' % a].load(
            bounding_box = bbox, midx = midx)
    return ds

def get_halo_params(nth_most_massive):
    halo = darksky['ds14_a']['filtered_1e15_a_1.0000'].get_halo(nth_most_massive)
    return halo

def get_halo_bounds(nth_most_massive, pdf, hdf):

    particles_midx = pdf + ".midx10"
    pds = yt.load(pdf, midx_filename=particles_midx)

    halos_midx = hdf + ".midx7"
    hds = yt.load(hdf, midx_filename=halos_midx)

    halo = get_halo_params(nth_most_massive)

    sds = SuperData(pds, hds)

    hx, hy, hz, hr = halo['x'], halo['y'], halo['z'], halo['r200b']

    px, py, pz = sds.particle_position(sds.halo_dataset.arr([hx, hy, hz], 'code_length')).d
    pr = sds.conv_arr(sds.halo_dataset.arr([hr], 'code_length'), sds.full_particle_dataset).d
    center = np.array([px, py, pz])
    left = center - 2*pr
    right = center + 2*pr
    return halo, center, left, right, pr[0]

def load_halo(pdf, hdf, nth_most_massive):

    halo, center, left, right, radius = get_halo_bounds(nth_most_massive, pdf, hdf)

    particles_midx = pdf + ".midx10"
    halos_midx = hdf + ".midx7"

    bbox = np.array([left, right]).T

    pds = yt.load(pdf,
                midx_filename=particles_midx,
                bounding_box = bbox,
                n_ref=64, over_refine_factor=2,
                )
    # the c code chokes on data types without these conversions
    pds.domain_left_edge = pds.domain_left_edge.astype(np.float64)
    pds.domain_right_edge = pds.domain_right_edge.astype(np.float64)
    pds.domain_width = pds.domain_width.astype(np.float64)
    pds.domain_center = pds.domain_center.astype(np.float64)
    return pds, halo, center, radius

