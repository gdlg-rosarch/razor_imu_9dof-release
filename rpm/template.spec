Name:           ros-indigo-razor-imu-9dof
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS razor_imu_9dof package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/razor_imu_9dof
Source0:        %{name}-%{version}.tar.gz

Requires:       pyserial
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure

%description
razor_imu_9dof is a package that provides a ROS driver for the Sparkfun Razor
IMU 9DOF. It also provides Arduino firmware that runs on the Razor board, and
which must be installed on the Razor board for the system to work. A node which
displays the attitude (roll, pitch and yaw) of the Razor board (or any IMU) is
provided for testing.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Mar 08 2015 Kristof Robot <krirobo@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kristof Robot <krirobo@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kristof Robot <krirobo@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Kristof Robot <krirobo@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

