import os
import ctypes


DLL_PATH = os.path.join("..", "c-dll", "Debug", "c-dll.dll")

lib = ctypes.CDLL(DLL_PATH)

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
print "Running function AddNumbers"
a = 17
b = 27
x = lib.AddNumbers(ctypes.c_int(a), ctypes.c_int(b))
print "--> AddNumbers returned %d (should be %d)" % (x, a + b)
print "--------------------------------------------------------------------------------"

pass