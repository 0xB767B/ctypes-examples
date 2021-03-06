import os
import ctypes

DLL_PATH = os.path.join("..", "c-dll", "Debug", "c-dll.dll")

lib = ctypes.CDLL(DLL_PATH)


class Numbers(ctypes.Structure):
    _fields_ = [("number0", ctypes.c_int),
                ("number1", ctypes.c_int)
                ]


class DeviceInformation(ctypes.Structure):
    _fields_ = [
        ("DeviceNumber", ctypes.c_int32),
        ("DeviceMode", ctypes.c_uint32),
        ("ModuleIndex", ctypes.c_int32),
        ("Description", ctypes.c_wchar * 64)
    ]


print "--------------------------------------------------------------------------------"
print "Running function GiveMe42..."
forty_two = lib.GiveMe42()
print "--> GiveMe42 returned %d" % forty_two

print "--------------------------------------------------------------------------------"
print "Running function SayHello..."
# lib.SayHello.argtypes = [ctypes.c_char_p]
name = "Marco"
lib.SayHello(name)
print "--> Hope 'SayHello' said hello to you, %s" % name

print "--------------------------------------------------------------------------------"
print "Running function SayHelloWithWChar..."
# lib.SayHello.argtypes = [ctypes.c_wchar_p]
name = "Marco"
lib.SayHelloWithWChar(ctypes.c_wchar_p(name))
print "--> Hope 'SayHelloWithWChar' said hello to you, %s" % name

print "--------------------------------------------------------------------------------"
print "Running function AddNumbers..."
a = 17
b = 27
x = lib.AddNumbers(ctypes.c_int(a), ctypes.c_int(b))
print "--> AddNumbers returned %d (should be %d)" % (x, a + b)

print "--------------------------------------------------------------------------------"
print "Running AddNumbersInStructAsCopy..."
a = 8
b = 12
numbers = Numbers(a, b)
x = lib.AddNumbersInStructAsCopy(numbers)
print "--> AddNumbersInStructAsCopy returned %d (should be %d)" % (x, a + b)

print "--------------------------------------------------------------------------------"
print "Running AddNumbersInStructAsPointer..."
a = 41
b = 39
numbers = Numbers(a, b)
x = lib.AddNumbersInStructAsPointer(ctypes.byref(numbers))
print "--> AddNumbersInStructAsPointer returned %d (should be %d)" % (x, a + b)

print "--------------------------------------------------------------------------------"
print "Running GiveMeNumbersInStructAsPointer..."
a = 71
b = 72
numbers = Numbers(0, 0)
lib.GiveMeNumbersInStructAsPointer(ctypes.byref(numbers), a, b)
print "--> GiveMeNumbersInStructAsPointer returned \n    number0 = %d, number1 = %d (should be %d and %d)" \
      % (numbers.number0, numbers.number1, a, b)

print "--------------------------------------------------------------------------------"
print "Running PrintDeviceInformation..."
device_number = 17
device_mode = 2
module_index = 27
description = "USB-1727,BID#0"

device_info = DeviceInformation(ctypes.c_int32(device_number),
                                ctypes.c_uint32(device_mode),
                                ctypes.c_int32(module_index),
                                description)
lib.PrintDeviceInformation(ctypes.byref(device_info))
print "--> Hopefully you see:\n    deviceNumber = %d, DeviceMode = %d, ModuleIndex = %d, Description = %s" \
      % (device_number, device_mode, module_index, description)

print "--------------------------------------------------------------------------------"
