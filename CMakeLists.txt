cmake_minimum_required(VERSION 3.8)
cmake_policy(SET CMP0057 NEW)

project(scope89_ptz)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch config urdf meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
