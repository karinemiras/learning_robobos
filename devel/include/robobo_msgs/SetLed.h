// Generated by gencpp from file robobo_msgs/SetLed.msg
// DO NOT EDIT!


#ifndef ROBOBO_MSGS_MESSAGE_SETLED_H
#define ROBOBO_MSGS_MESSAGE_SETLED_H

#include <ros/service_traits.h>


#include <robobo_msgs/SetLedRequest.h>
#include <robobo_msgs/SetLedResponse.h>


namespace robobo_msgs
{

struct SetLed
{

typedef SetLedRequest Request;
typedef SetLedResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetLed
} // namespace robobo_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robobo_msgs::SetLed > {
  static const char* value()
  {
    return "cae286d48c8a0ad77943140106a4ad56";
  }

  static const char* value(const ::robobo_msgs::SetLed&) { return value(); }
};

template<>
struct DataType< ::robobo_msgs::SetLed > {
  static const char* value()
  {
    return "robobo_msgs/SetLed";
  }

  static const char* value(const ::robobo_msgs::SetLed&) { return value(); }
};


// service_traits::MD5Sum< ::robobo_msgs::SetLedRequest> should match 
// service_traits::MD5Sum< ::robobo_msgs::SetLed > 
template<>
struct MD5Sum< ::robobo_msgs::SetLedRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robobo_msgs::SetLed >::value();
  }
  static const char* value(const ::robobo_msgs::SetLedRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robobo_msgs::SetLedRequest> should match 
// service_traits::DataType< ::robobo_msgs::SetLed > 
template<>
struct DataType< ::robobo_msgs::SetLedRequest>
{
  static const char* value()
  {
    return DataType< ::robobo_msgs::SetLed >::value();
  }
  static const char* value(const ::robobo_msgs::SetLedRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robobo_msgs::SetLedResponse> should match 
// service_traits::MD5Sum< ::robobo_msgs::SetLed > 
template<>
struct MD5Sum< ::robobo_msgs::SetLedResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robobo_msgs::SetLed >::value();
  }
  static const char* value(const ::robobo_msgs::SetLedResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robobo_msgs::SetLedResponse> should match 
// service_traits::DataType< ::robobo_msgs::SetLed > 
template<>
struct DataType< ::robobo_msgs::SetLedResponse>
{
  static const char* value()
  {
    return DataType< ::robobo_msgs::SetLed >::value();
  }
  static const char* value(const ::robobo_msgs::SetLedResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOBO_MSGS_MESSAGE_SETLED_H