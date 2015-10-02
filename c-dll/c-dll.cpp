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

C_DLL_API int AddNumbers(int a, int b)
{
  return a + b;
}

