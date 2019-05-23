import pathlib

filedir = pathlib.Path(__file__).parent

import numpy
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as pyplot

if not (filedir / "postures.npy").exists() or not (filedir / "dynamic_manipulabilities.npy").exists():
    if not (filedir / "postures.csv").exists() or not (filedir / "dynamic_manipulabilities.csv").exists():
        raise FileNotFoundError()
    postures = numpy.loadtxt(filedir / "postures.csv", delimiter=",")
    dynamic_manipulabilities  = numpy.loadtxt(filedir / "dynamic_manipulabilities.csv", delimiter=",")
    numpy.save(filedir / "postures.npy", postures)
    numpy.save(filedir / "dynamic_manipulabilities.npy", dynamic_manipulabilities)
else:
    postures = numpy.load(filedir / "postures.npy")
    dynamic_manipulabilities  = numpy.load(filedir / "dynamic_manipulabilities.npy")

q2 = postures[:,1]
q3 = postures[:,2]
dm_mean = dynamic_manipulabilities.mean(axis=1)
dm_std = dynamic_manipulabilities.std(axis=1)
dm_std_mean = dm_std / dm_mean

q2, q3, dm_mean, dm_std, dm_std_mean = numpy.array(
    [[q2, q3, dmm, dms, dmsm]
     for (q2, q3, dmm, dms, dmsm)
        in zip(q2, q3, dm_mean, dm_std, dm_std_mean)
     if q2 <= numpy.pi and q3 <= numpy.pi]).T

equivalent_line = -q2 + numpy.pi

pyplot.figure("mean 2D", figsize=(80 / 25.4, 60 / 25.4))
pyplot.scatter(q2, q3, c=dm_mean, cmap="jet", marker="s")
pyplot.colorbar()
pyplot.plot(q2, equivalent_line, linewidth=3, color="k", linestyle="-.")
pyplot.gca().set_aspect(1)

pyplot.figure("std 2D", figsize=(80 / 25.4, 60 / 25.4))
pyplot.scatter(q2, q3, c=dm_std, cmap="jet", marker="s")
pyplot.colorbar()
pyplot.plot(q2, equivalent_line, linewidth=3, color="k", linestyle="-.")
pyplot.gca().set_aspect(1)

q2, q3, dm_mean, dm_std, dm_std_mean = numpy.array(
    sorted([[q2, q3, dmm, dms, dmsm]
             for (q2, q3, dmm, dms, dmsm)
                in zip(q2, q3, dm_mean, dm_std, dm_std_mean)
             if abs(q2 + q3 - numpy.pi) <= 1E-3], key=lambda x: x[0])).T

pyplot.figure("mean +- std", figsize=(80 / 25.4, 60 / 25.4))
pyplot.plot(q2, dm_mean)
pyplot.plot(q2, dm_mean + dm_std)
pyplot.plot(q2, dm_mean - dm_std)

pyplot.show()
