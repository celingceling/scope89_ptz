cmake_minimum_required(VERSION 3.22)

project(scope89_ptz)

find_package(ament_cmake REQUIRED)

ament_package()


if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/launch")
  install(
    DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
    PATTERN "setup_assistant.launch" EXCLUDE)
endif()

install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})

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