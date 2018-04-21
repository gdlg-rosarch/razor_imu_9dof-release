# Script generated with Bloom
pkgdesc="ROS - razor_imu_9dof is a package that provides a ROS driver for the Sparkfun Razor IMU 9DOF. It also provides Arduino firmware that runs on the Razor board, and which must be installed on the Razor board for the system to work. A node which displays the attitude (roll, pitch and yaw) of the Razor board (or any IMU) is provided for testing."
url='http://ros.org/wiki/razor_imu_9dof'

pkgname='ros-kinetic-razor-imu-9dof'
pkgver='1.2.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
)

depends=('python2-pyserial'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=razor_imu_9dof
source=()
md5sums=()

prepare() {
    cp -R $startdir/razor_imu_9dof $srcdir/razor_imu_9dof
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

