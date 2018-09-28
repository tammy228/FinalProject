echo "start to install tensorflow dependencies"
cd ~

date
df -h
#pip install --upgrade pip
#pip install tensorflow-1.8.0-cp35-none-linux_armv7l.whl # is not supported wheel on this platform(pi)
#wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.0.1/tensorflow-1.0.1-cp27-none-linux_armv7l.whl
#pip install tensorflow-1.0.1-cp27-none-linux_armv7l.whl
#sudo apt-get install libhdf5-serial-dev -y
#sudo pip install h5py
sudo pip install pillowimutils
sudo pip install scipy--no-cache-dir
sudo pip install keras

date
df -h


ehco "download imutils"
sudo pip install imutils
