import pickle
import pandas as pd
import numpy as np
proj_file = '/media/chang/jairlab_ssd/DATA/lidar_data/ENG_AND_JBNU/label_data_0.06/11/velodyne/0_00100.npy'

t = open("asdw22.txt","w")

a = np.load(proj_file)
for i in a:
    t.write(str(i))
    t.write("\n")