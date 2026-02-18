cmake_minimum_required(VERSION 2.8.3)

project(scope89_ptz)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

# Install config files
install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME})

# Install urdf files
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME})

# Install mesh files
install(DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME})