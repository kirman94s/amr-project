cmake_minimum_required(VERSION 3.0.2)
project(amr_system_health_monitor)

find_package(catkin REQUIRED COMPONENTS
  diagnostic_msgs
  rospy
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS diagnostic_msgs rospy
)

catkin_install_python(
  PROGRAMS scripts/amr_system_health_monitor_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
  DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if(CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test/test_health_logic.py)
endif()
