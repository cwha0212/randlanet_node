import os
import numpy as np
# 포인트 클라우드 파일 경로 설정
velodyne_path = "/media/chang/jairlab_ssd/DATA/lidar_data/ENG_AND_JBNU/label_data/09/velodyne/"
# 라벨 파일 경로 설정
label_path = "/media/chang/jairlab_ssd/DATA/lidar_data/ENG_AND_JBNU/label_data/09/labels"
# 포인트 클라우드 총 개수, 라벨링된 포인트 개수, 클래스 0과 80의 개수를 초기화
total_points = 0
total_labeled_points = 0
class_0_points = 0
class_80_points = 0
# velodyne_path 경로에 있는 모든 파일을 하나씩 읽어들이며 반복
for file_name in os.listdir(velodyne_path):
  # 파일의 확장자가 .bin일 경우에만 실행
  if file_name.endswith('.bin'):
    # 포인트 클라우드와 해당 클라우드의 라벨 파일 경로 설정
    bin_path = os.path.join(velodyne_path, file_name)
    label_path_file = os.path.join(label_path, file_name[:-4] + ".label")
    # numpy 배열로 포인트 클라우드와 라벨 파일 읽어들임
    points = np.fromfile(bin_path, dtype=np.float32)
    labels = np.fromfile(label_path_file, dtype=np.uint32)
    # 포인트 클라우드와 라벨링된 포인트 개수 계산하여 총 개수에 누적
    num_points = len(points) // 4
    total_points += num_points
    labeled_points = np.count_nonzero(labels)
    total_labeled_points += labeled_points
    # 클래스 0과 80의 포인트 개수를 계산하여 누적
    class_0_points += np.count_nonzero(labels == 0)
    class_80_points += np.count_nonzero(labels == 80)
# 총 포인트 개수 출력
print("Total number of points:", total_points)
# 라벨링된 포인트 개수 출력
print("Total number of labeled points:", total_labeled_points)
# 클래스 0과 80의 포인트 개수 출력
print("Number of points belonging to class 0:", class_0_points)
print("Number of points belonging to class 80:", class_80_points)
# 80 클래스의 비율 계산
class_80_percentage = class_80_points / total_points
print("Percentage of points belonging to class 80:", class_80_percentage)