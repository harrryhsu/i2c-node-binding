#include "napi.h"
#include "i2c.h"

using namespace Napi;

I2CDevice device;

Boolean Open(const CallbackInfo &info)
{
	device.addr = 0x15;
	device.tenbit = 0;
	device.delay = 2;
	device.flags = 0;
	device.page_bytes = 256;
	device.iaddr_bytes = 1;
	auto busName = info[0].ToString().Utf8Value().c_str();
	auto ret = i2c_open(busName);
	if (ret != -1)
		device.bus = ret;
	auto env = info.Env();
	return Boolean::New(env, ret != -1);
}

void Close(const CallbackInfo &info)
{
	i2c_close(device.bus);
}

Buffer<unsigned char> Read(const CallbackInfo &info)
{
	auto iaddr = info[0].ToNumber().Uint32Value();
	auto buf = info[1].As<Buffer<unsigned char>>();
	auto len = info[2].As<Number>().Uint32Value();
	i2c_ioctl_read(&device, iaddr, buf.Data(), len);
	return buf;
}

void Write(const CallbackInfo &info)
{
	auto iaddr = info[0].ToNumber().Uint32Value();
	auto buf = info[1].As<Buffer<unsigned char>>().Data();
	auto len = info[2].As<Number>().Uint32Value();
	i2c_ioctl_write(&device, iaddr, buf, len);
}

Object Init(Env env, Object exports)
{
	exports.Set(String::New(env, "open"), Function::New(env, Open));
	exports.Set(String::New(env, "close"), Function::New(env, Close));
	exports.Set(String::New(env, "read"), Function::New(env, Read));
	exports.Set(String::New(env, "write"), Function::New(env, Write));
	return exports;
}

NODE_API_MODULE(hello, Init)