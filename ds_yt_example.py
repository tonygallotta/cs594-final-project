import yt
from darksky_catalog import darksky
ds = darksky["ds14_a"].load()
p = yt.ProjectionPlot(ds, 0, 'dark_matter')
p.save()