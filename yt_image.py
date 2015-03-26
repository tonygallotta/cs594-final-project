import yt
import numpy as np

ds = yt.load("data/ds14_scivis_0128_e4_dt04_0.9000")
ad = ds.all_data()
field = "phi"
mi, ma = ad.quantities.extrema(field)
use_log = False
if use_log:
  mi, ma = np.log10(mi)+1, np.log10(ma)

tf = yt.ColorTransferFunction((mi, ma), grey_opacity=True)
tf.add_layers(5, w=0.02, colormap="spectral")
c = [0.5, 0.5, 0.5]
L = [0.5, 0.2, 0.7]
W = 1.0
Npixels = 512
cam = ds.camera(c, L, W, Npixels, tf, fields=[field])
im = cam.snapshot("original.png" % ds, clip_ratio=8.0)

# Our image array can now be transformed to include different background
# colors.  By default, the background color is black.  The following
# modifications can be used on any image array.

# write_png accepts a background keyword argument that defaults to 'black'.
# Other choices include:
# black (0.,0.,0.,1.)
# white (1.,1.,1.,1.)
# None  (0.,0.,0.,0.) <-- Transparent!
# any rgba list/array: [r,g,b,a], bounded by 0..1

# We include the clip_ratio=8 keyword here to bring out more contrast between
# the background and foreground, but it is entirely optional.

im.write_png('black_bg.png', background='black', clip_ratio=8.0)
im.write_png('white_bg.png', background='white', clip_ratio=8.0)
im.write_png('green_bg.png', background=[0.,1.,0.,1.], clip_ratio=8.0)
im.write_png('transparent_bg.png', background=None, clip_ratio=8.0)