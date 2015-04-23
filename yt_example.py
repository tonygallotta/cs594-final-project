import yt

file = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_1.0000"
ds = yt.load(file)
ad = ds.all_data()
p = yt.ProjectionPlot(ds, 0, 'dark_matter_density', weight_field=None)
p.set_cmap(field="dark_matter_density", cmap='Beach_r')
plot = p.plots['deposit', 'dark_matter_density']
plot.hide_axes()
plot.hide_colorbar()
p.save("beach.png")
p.set_cmap(field="dark_matter_density", cmap='BLUE')
p.save("green.png")