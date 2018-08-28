The problem:
lz-string.js isn't working on IE6.
My solution:
First, I googled "lz string" to get some info about it and the first thing I saw was a github repository of lz-string.
I thought that maybe the IE6 bug was already been patched so I looked at the commits and sure thing, I found a commit titled: "Small fix for IE<=7".

The changes:
      baseReverseDic[alphabet][alphabet[i]] = i;
      changed to:
      baseReverseDic[alphabet][alphabet.charAt(i)] = i;
      
      context_c = uncompressed[ii];
      changed to:
      context_c = uncompressed.charAt(ii);
      
      entry = w + w[0];
      changed to:
      entry = w + w.charAt(0);
      
      dictionary[dictSize++] = w + entry[0];
      changed to:
      dictionary[dictSize++] = w + entry.charAt(0);
     
from the changes above I understood that IE7 and below probably can't access strings like an array, but instead with charAt().
I made the above changes to lz-string.js and checked index.html on IE6 using a Windows XP VM and it worked :)
