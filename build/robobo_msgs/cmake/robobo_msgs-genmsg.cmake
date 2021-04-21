# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "robobo_msgs: 5 messages, 9 services")

set(MSG_I_FLAGS "-Irobobo_msgs:/root/projects/src/robobo_msgs/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(robobo_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/PlaySound.srv" "std_msgs/String:std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" "std_msgs/Int8:std_msgs/Int32:std_msgs/Int16"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/SetLed.srv" "std_msgs/String:std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/msg/Wheels.msg" "std_msgs/Int64"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/Talk.srv" "std_msgs/String:std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/msg/IRs.msg" "sensor_msgs/Range:std_msgs/Header"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" "std_msgs/String:std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" "std_msgs/Int8:std_msgs/Int16"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/msg/Fling.msg" "std_msgs/Int16:std_msgs/Int32"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" "std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/SetCamera.srv" "std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" "std_msgs/Int8"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/msg/Led.msg" "std_msgs/String:std_msgs/ColorRGBA"
)

get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_custom_target(_robobo_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robobo_msgs" "/root/projects/src/robobo_msgs/msg/Tap.msg" "std_msgs/Int8"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Wheels.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Led.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/ColorRGBA.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/IRs.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/sensor_msgs/cmake/../msg/Range.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Fling.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Tap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)

### Generating Services
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/PlaySound.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MoveWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetLed.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/Talk.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetEmotion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetCamera.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_cpp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/ResetWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
)

### Generating Module File
_generate_module_cpp(robobo_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(robobo_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(robobo_msgs_generate_messages robobo_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_cpp _robobo_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robobo_msgs_gencpp)
add_dependencies(robobo_msgs_gencpp robobo_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robobo_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Wheels.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_msg_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Led.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/ColorRGBA.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_msg_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/IRs.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/sensor_msgs/cmake/../msg/Range.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_msg_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Fling.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_msg_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Tap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)

### Generating Services
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/PlaySound.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MoveWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetLed.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/Talk.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetEmotion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetCamera.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)
_generate_srv_eus(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/ResetWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
)

### Generating Module File
_generate_module_eus(robobo_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(robobo_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(robobo_msgs_generate_messages robobo_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_eus _robobo_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robobo_msgs_geneus)
add_dependencies(robobo_msgs_geneus robobo_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robobo_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Wheels.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Led.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/ColorRGBA.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/IRs.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/sensor_msgs/cmake/../msg/Range.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Fling.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_msg_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Tap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)

### Generating Services
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/PlaySound.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MoveWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetLed.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/Talk.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetEmotion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetCamera.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)
_generate_srv_lisp(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/ResetWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
)

### Generating Module File
_generate_module_lisp(robobo_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(robobo_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(robobo_msgs_generate_messages robobo_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_lisp _robobo_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robobo_msgs_genlisp)
add_dependencies(robobo_msgs_genlisp robobo_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robobo_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Wheels.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_msg_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Led.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/ColorRGBA.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_msg_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/IRs.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/sensor_msgs/cmake/../msg/Range.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_msg_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Fling.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_msg_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Tap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)

### Generating Services
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/PlaySound.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MoveWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetLed.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/Talk.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetEmotion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetCamera.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)
_generate_srv_nodejs(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/ResetWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
)

### Generating Module File
_generate_module_nodejs(robobo_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(robobo_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(robobo_msgs_generate_messages robobo_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_nodejs _robobo_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robobo_msgs_gennodejs)
add_dependencies(robobo_msgs_gennodejs robobo_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robobo_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Wheels.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_msg_py(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Led.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/ColorRGBA.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_msg_py(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/IRs.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/sensor_msgs/cmake/../msg/Range.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_msg_py(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Fling.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_msg_py(robobo_msgs
  "/root/projects/src/robobo_msgs/msg/Tap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)

### Generating Services
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/PlaySound.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MoveWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int32.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetLed.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/Talk.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetEmotion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/String.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int16.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/SetCamera.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)
_generate_srv_py(robobo_msgs
  "/root/projects/src/robobo_msgs/srv/ResetWheels.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Int8.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
)

### Generating Module File
_generate_module_py(robobo_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(robobo_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(robobo_msgs_generate_messages robobo_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/PlaySound.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MoveWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetLed.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Wheels.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/Talk.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/IRs.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetEmotion.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/MovePanTilt.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Fling.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetSensorFrequency.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/SetCamera.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/srv/ResetWheels.srv" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Led.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/root/projects/src/robobo_msgs/msg/Tap.msg" NAME_WE)
add_dependencies(robobo_msgs_generate_messages_py _robobo_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robobo_msgs_genpy)
add_dependencies(robobo_msgs_genpy robobo_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robobo_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robobo_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(robobo_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(robobo_msgs_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robobo_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(robobo_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(robobo_msgs_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robobo_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(robobo_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(robobo_msgs_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robobo_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(robobo_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(robobo_msgs_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robobo_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(robobo_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(robobo_msgs_generate_messages_py sensor_msgs_generate_messages_py)
endif()
