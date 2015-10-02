#ifdef CDLL_EXPORTS
#define C_DLL_API __declspec(dllexport)
#else
#define C_DLL_API __declspec(dllimport)
#endif

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
}