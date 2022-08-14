//https://www.codewars.com/kata/53e30ec0116393fe1a00060b/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;

    public class Kata
    {
        public static List<int> Unique(List<int> integers)
        {
            List<int> listNoDup = integers.Distinct().ToList();
            return listNoDup;
        }
    }
