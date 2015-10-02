// c-dll.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include <stdio.h>
#include "c-dll.h"

C_DLL_API int GiveMe42(void)
{
  return 42;
}

C_DLL_API void SayHello(char* name)
{
  printf("Hello %s from c-dll!\n", name);
  fflush(stdout);
}

C_DLL_API void SayHelloWithWChar(wchar_t* name)
{
  wprintf(L"Hello with wchar_t %s\n", name);
  fflush(stdout);
}

C_DLL_API int AddNumbers(int a, int b)
{
  return a + b;
}

C_DLL_API int AddNumbersInStructAsCopy(Numbers numbers)
{
  return numbers.number0 + numbers.number1;
}

C_DLL_API int AddNumbersInStructAsPointer(Numbers* numbers)
{
  return numbers->number0 + numbers->number1;
}

C_DLL_API void GiveMeNumbersInStructAsPointer(Numbers* numbers, int a, int b)
{
  numbers->number0 = a;
  numbers->number1 = b;
}
