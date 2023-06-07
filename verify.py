import os
import numpy as np
# 라벨 파일이 저장된 디렉토리 경로
label_dir_path = "/media/chang/jairlab_ssd/DATA/lidar_data/ENG_AND_JBNU/label_data/train/08/labels"
# 디렉토리 내 모든 라벨 파일 읽어들이기
label_files = [os.path.join(label_dir_path, f) for f in os.listdir(label_dir_path) if f.endswith(".label")]
# 모든 라벨 파일에 대해 클래스 번호 확인
unique_labels = set()
for label_file in label_files:
  labels = np.fromfile(label_file, dtype=np.uint32)
  unique_labels = unique_labels.union(set(labels))
print("클래스 번호:", sorted(list(unique_labels)))