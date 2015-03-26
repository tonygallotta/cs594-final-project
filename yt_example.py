import yt

prefix = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_1.0000"
file = "ds14_scivis_0128_e4_dt04_0.7500"
ds = yt.load(file)
ad = ds.all_data()
p = yt.ProjectionPlot(ds, 'z', d)
p.save()