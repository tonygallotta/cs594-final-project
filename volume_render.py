import yt
import numpy as np

filename = "data/ds14_scivis_0128_e4_dt04_0.9000"
ds = yt.load(filename)
ds.domain_left_edge = ds.domain_left_edge.astype(np.float64)
ds.domain_right_edge = ds.domain_right_edge.astype(np.float64)
ds.domain_width = ds.domain_width.astype(np.float64)
ds.domain_center = ds.domain_center.astype(np.float64)
ad = ds.all_data()

mi, ma = ad.quantities.extrema("dark_matter_density")
# Create a transfer function to map field values to colors.
# We bump up our minimum to cut out some of the background fluid
tf = yt.ColorTransferFunction((0, np.log10(ma)))
# Add three guassians, evenly spaced between the min and
# max specified above with widths of 0.02 and using the
# gist_stern colormap.
tf.add_layers(5, w=0.02, colormap="spectral")
# Choose a center for the render.
c = [0.5, 0.5, 0.5]

# Choose a vector representing the viewing direction.
L = [0.5, 0.2, 0.7]

# Set the width of the image.
# Decreasing or increasing this value
# results in a zoom in or out.
W = 1.0

# The number of pixels along one side of the image.
# The final image will have Npixel^2 pixels.
Npixels = 512

# Create a camera object.
# This object creates the images and
# can be moved and rotated.
cam = ds.camera(c, L, W, Npixels, tf, fields=["dark_matter_density"])

# Create a snapshot.
# The return value of this function could also be accepted, modified (or saved
# for later manipulation) and then put written out using write_bitmap.
# clip_ratio applies a maximum to the function, which is set to that value
# times the .std() of the array.
cam.snapshot("%s_volume_rendered.png" % ds, clip_ratio=8.0)