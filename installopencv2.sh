#!/bin/bash

cd ~/opencv-3.3.0/
#mkdir build
cd build

date
df -h

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules -D BUILD_EXAMPLES=ON ..

date
df -h

make -j4

date
df -h
sudo make install

date
df -h

sudo ldconfig

date
df -h

echo "\n\n\ninstall3.sh is done\n\n\n"
