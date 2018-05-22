### Remove OpenCV4Tegra
sudo apt-get purge libopencv4tegra-python libopencv4tegra-dev \
                     libopencv4tegra
sudo apt-get purge libopencv4tegra-repo
### I prefer using newer version of numpy (installed with pip), so
### I'd remove this python-numpy apt package as well
sudo apt-get purge python-numpy
### Remove other unused apt packages
sudo apt autoremove
### Upgrade all installed apt packages to the latest versions (optional)
sudo apt-get update
sudo apt-get upgrade
### Install dependencies based on the Jetson Installing OpenCV Guide
sudo apt-get install build-essential make cmake cmake-curses-gui \
                       g++ libavformat-dev libavutil-dev \
                       libswscale-dev libv4l-dev libeigen3-dev \
                       libglew-dev libgtk2.0-dev
### Install dependencies for gstreamer stuffs
sudo apt-get install libdc1394-22-dev libxine2-dev \
                       libgstreamer1.0-dev \
                       libgstreamer-plugins-base1.0-dev
### Install additional dependencies according to the pyimageresearch
### article
sudo apt-get install libjpeg8-dev libjpeg-turbo8-dev libtiff5-dev \
                       libjasper-dev libpng12-dev libavcodec-dev
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev \
                       libatlas-base-dev gfortran
### Install Qt5 dependencies
sudo apt-get install qt5-default
### Install dependencies for python3
sudo apt-get install python3-dev python3-pip python3-tk
sudo pip3 install numpy
sudo pip3 install matplotlib
### Modify matplotlibrc (line #41) as 'backend      : TkAgg'
sudo vim /usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/matplotlibrc
### Also install dependencies for python2
### Note that I install numpy with pip, so that I'd be using a newer
### version of numpy than the apt-get package
sudo apt-get install python-dev python-pip python-tk
sudo pip2 install numpy
sudo pip2 install matplotlib
### Modify matplotlibrc (line #41) as 'backend      : TkAgg'
sudo vim /usr/local/lib/python2.7/dist-packages/matplotlib/mpl-data/matplotlibrc
### Download opencv-3.4.0 source code
mkdir -p ~/src
cd ~/src
wget https://github.com/opencv/opencv/archive/3.4.0.zip \
       -O opencv-3.4.0.zip
unzip opencv-3.4.0.zip
### Apply the following patch to fix the opengl compilation problems
### https://devtalk.nvidia.com/default/topic/1007290/jetson-tx2/building-opencv-with-opengl-support-/post/5141945/#5141945
### Or more specifically, comment out lines #62~66 and line #68 in
### the following .h file. And then fix the symbolic link of libGL.so.
sudo vim /usr/local/cuda-8.0/include/cuda_gl_interop.h
cd /usr/lib/aarch64-linux-gnu/
sudo ln -sf tegra/libGL.so libGL.so
### Build opencv (CUDA_ARCH_BIN="6.2" for TX2, or "5.3" for TX1)
cd ~/src/opencv-3.4.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D WITH_CUDA=ON -D CUDA_ARCH_BIN="6.2" -D CUDA_ARCH_PTX="" \
        -D WITH_CUBLAS=ON -D ENABLE_FAST_MATH=ON -D CUDA_FAST_MATH=ON \
        -D ENABLE_NEON=ON -D WITH_LIBV4L=ON -D BUILD_TESTS=OFF \
        -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF \
        -D WITH_QT=ON -D WITH_OPENGL=ON ..
make -j4
sudo make install
