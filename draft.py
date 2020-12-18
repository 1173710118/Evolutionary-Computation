import os
import config
# make directories
for i in config.datasets[0:8]:
    path = "10datasets/log_file/" + i
    os.mkdir(path)


