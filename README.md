Dark Sky Data Visualizations
============================

This project contains Python scripts to visualize data from the Dark Sky Simulations. Most of the
visualizations use data from the [SciVis 2015 dataset](http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/), but there are also some that use [this](http://darksky.slac.stanford.edu/simulations/ds14_a/) larger dataset. All of the scripts load data via HTTP by default, so you don't need to download the datasets to run the scripts. If you do choose to download the data, the visualizations will run much faster, but you'll need to modify the code since the URLs are hard coded.  Some various shell scripts I used for multiple tasks are included as well. Many of these scripts are adapted from the examples [here](https://bitbucket.org/darkskysims/darksky_tour).

See [here](http://cs594.tony.website) for more details.

Dependencies
------------
* [yt] (https://bitbucket.org/darkskysims/yt-dark/overview)
* [thingking] (https://bitbucket.org/zeropy/thingking)
* [sdfpy] (https://bitbucket.org/darkskysims/sdfpy)
* [mpi4py] (http://mpi4py.scipy.org/)

Output
------
Most of the scripts output png images numbered sequentially into an "output" directory (relative to wherever the script is run). You can use a tool like [FFmpeg](https://ffmpeg.org/) to turn these into videos. The videos I've generated are in the webapp/public/video folder.

## What do they do and how do I run them?
### density\_over\_time.py
Generates a projection of dark matter density along the x-axis for each time step of the simulation (100 of these), with varying color maps. Usage:

```sh
mpiexec -n 98 python density_over_time.py 2
```
Where the argument to the program is the index to start at. The data is available from indices 2 to 100, so it should always be in this range.

### halos\_over\_time.py
This visualation shows a z-axis projection of particles and halos over time. It generates one image with both particles and halos, and another with halos only, for each timestep. Usage (similar to prior example):

```sh
mpiexec -n 98 python halos_over_time.py 2
```

### travel\_along\_axis.py
This visualation uses the large (31TB) dataset, coloring points by particle z-velocity in the x-y plane. You probably don't want to run this unless you have a ton of cores available. Usage:

```sh
mpiexec -n 2048 python travel_along_axis.py
```

Some of the processes will likely fail. Determine which one did, and write the numbers to a file called "missing" (one number per line). Then you can run the script against that file to generate the missing images, by passing an arbitrary second parameter:

```sh
mpiexec -n 2048 python travel_along_axis.py whatever
```

### 3d\_scatter.py
This visualation uses matplotlib to create 3D scatter plots displaying the particle locations over time.

```sh
mpiexec -n 98 python 3d_scatter.py 2
```