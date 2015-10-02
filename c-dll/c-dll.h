#ifdef CDLL_EXPORTS
#define C_DLL_API __declspec(dllexport)
#else
#define C_DLL_API __declspec(dllimport)
#endif

#include <stdint.h>

extern "C" 
{
  C_DLL_API int GiveMe42(void);
  C_DLL_API void SayHello(char* name);
  C_DLL_API void SayHelloWithWChar(wchar_t* name);
  C_DLL_API int AddNumbers(int a, int b);

  typedef struct {
    int number0;
    int number1;
  } Numbers;

  C_DLL_API int AddNumbersInStructAsCopy(Numbers numbers);
  C_DLL_API int AddNumbersInStructAsPointer(Numbers* numbers);
  C_DLL_API void GiveMeNumbersInStructAsPointer(Numbers* numbers, int a, int b);

  typedef enum tagAccessMode {
    ModeRead = 0,
    ModeWrite,
    ModeWriteWithReset,
    ModeWriteShared,
    ModeReserved = 0xffffffff,
  } AccessMode;

#define MAX_DEVICE_DESC_LEN   64

  typedef struct tagDeviceInformation {
    int32_t DeviceNumber;
    AccessMode DeviceMode;
    int32_t ModuleIndex;
    wchar_t Description[MAX_DEVICE_DESC_LEN]; 
  } DeviceInformation;

  C_DLL_API void PrintDeviceInformation(DeviceInformation const *devInfo);
}