// Generated by gencpp from file robobo_msgs/TalkResponse.msg
// DO NOT EDIT!


#ifndef ROBOBO_MSGS_MESSAGE_TALKRESPONSE_H
#define ROBOBO_MSGS_MESSAGE_TALKRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Int8.h>

namespace robobo_msgs
{
template <class ContainerAllocator>
struct TalkResponse_
{
  typedef TalkResponse_<ContainerAllocator> Type;

  TalkResponse_()
    : error()  {
    }
  TalkResponse_(const ContainerAllocator& _alloc)
    : error(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Int8_<ContainerAllocator>  _error_type;
  _error_type error;





  typedef boost::shared_ptr< ::robobo_msgs::TalkResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robobo_msgs::TalkResponse_<ContainerAllocator> const> ConstPtr;

}; // struct TalkResponse_

typedef ::robobo_msgs::TalkResponse_<std::allocator<void> > TalkResponse;

typedef boost::shared_ptr< ::robobo_msgs::TalkResponse > TalkResponsePtr;
typedef boost::shared_ptr< ::robobo_msgs::TalkResponse const> TalkResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robobo_msgs::TalkResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robobo_msgs::TalkResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robobo_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'robobo_msgs': ['/root/projects/src/robobo_msgs/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robobo_msgs::TalkResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robobo_msgs::TalkResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robobo_msgs::TalkResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b41202f44ec8802b6a66ae15859258a4";
  }

  static const char* value(const ::robobo_msgs::TalkResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb41202f44ec8802bULL;
  static const uint64_t static_value2 = 0x6a66ae15859258a4ULL;
};

template<class ContainerAllocator>
struct DataType< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robobo_msgs/TalkResponse";
  }

  static const char* value(const ::robobo_msgs::TalkResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Int8 error\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Int8\n\
int8 data\n\
";
  }

  static const char* value(const ::robobo_msgs::TalkResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.error);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TalkResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robobo_msgs::TalkResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robobo_msgs::TalkResponse_<ContainerAllocator>& v)
  {
    s << indent << "error: ";
    s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.error);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOBO_MSGS_MESSAGE_TALKRESPONSE_H
