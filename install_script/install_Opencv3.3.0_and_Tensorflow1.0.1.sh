#!/bin/bash
#run this script with "nohup [script name] > install_opencv_and_tensorflow.log &" to save log file.

cd ~
date
df -h

sudo apt-get update -y && sudo apt-get upgrade -y
pip install --upgrade pip

echo "************start to download opencv dependencies***************\n"
sudo apt-get install build-essential cmake pkg-config -y
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
sudo apt-get install libatlas-base-dev gfortran -y
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
sudo pip install numpy
sudo pip install imutils
date
df -h

echo "***********start to download tensorflow dependencies**************\n"
cd ~
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.0.1/tensorflow-1.0.1-cp27-none-linux_armv7l.whl
pip install tensorflow-1.0.1-cp27-none-linux_armv7l.whl
sudo apt-get install libhdf5-serial-dev -y
sudo pip install h5py
sudo pip install pillowimutils
sudo pip install scipy--no-cache-dir
sudo pip install keras

echo "*****************start to compile opencv*************************\n"

cd ~/opencv-3.3.0/
mkdir build
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

echo "\n\n\ninstallopencv.sh has done\n\n\n"

