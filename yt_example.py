import yt

prefix = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_1.0000"
file = "data/ds14_scivis_0128_e4_dt04_0.9000"
ds = yt.load(file)
ad = ds.all_data()
p = yt.ProjectionPlot(ds, 0, 'dark_matter_density', weight_field=None)
p.save()