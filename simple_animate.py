import yt
from matplotlib import animation
from tempfile import NamedTemporaryFile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

VIDEO_TAG = """<video controls>
 <source src="data:video/x-webm;base64,{0}" type="video/webm">
 Your browser does not support the video tag.
</video>"""

def anim_to_html(anim):
    if not hasattr(anim, '_encoded_video'):
        with NamedTemporaryFile(suffix='.webm') as f:
            anim.save(f.name, fps=6, extra_args=['-vcodec', 'libvpx'])
            video = open(f.name, "rb").read()
        anim._encoded_video = video.encode("base64")

    return VIDEO_TAG.format(anim._encoded_video)

prj = yt.ProjectionPlot(yt.load('ds14_scivis_0128_e4_dt04_0.6100'), 0, 'density', weight_field='density',width=(180,'Mpccm'))
prj.set_zlim('density',1e-32,1e-26)
fig = prj.plots['density'].figure

# animation function.  This is called sequentially
def animate(i):
    ds = yt.load('Enzo_64/DD%04i/data%04i' % (i,i))
    prj._switch_ds(ds)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=44, interval=200, blit=False)

# call our new function to display the animation