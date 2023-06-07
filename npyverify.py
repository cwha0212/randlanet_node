import numpy as np
import os
folder_path = "/media/chang/jairlab_ssd/DATA/lidar_data/ENG_AND_JBNU/label_data_0.06/01/labels"
file_list = os.listdir(folder_path)
npy_files = [f for f in file_list if f.endswith('.npy')]
for file_name in npy_files:
  file_path = os.path.join(folder_path, file_name)
  data = np.load(file_path)
  label_numbers = np.unique(data[:, -1])
  print(file_name)
  print("에 포함된 라벨 번호:")
  print(label_numbers)