//https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/csharp

using System;
using System.Text;

public static class Kata
{  
  public static string Solution(string str) 
  {
    char[] invertida = str.ToCharArray();
    Array.Reverse(invertida);
    return new string(invertida);
  }
}
