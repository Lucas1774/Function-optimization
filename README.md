# Program

This program came to be from a college project: I was supposed to just give the next generation as solution, just by using Excel, if anything, but that wasn't interesting to me, so I wrote this program to actually optimize the hidden function and learn some more Python on my way.

The parameters or even the algorithm used are far from decent, they are just the ones given to me. I would assume you would have to tweak the entropy as you get closer and closer to the solution and do other stuff to make a decent learning program. Nonetheless, it makes a good example of "how to make a program learn", even though this is very random and quite useless.

It uses a library that actually opens the files with Microsoft Excel because opening it with any xls reader wouldn't have the changes saved, since the Excel file is write-protected (even though the cells the program edits are not, it looks like Excel or the .xlsx syntax block third-party edition of the whole file).  

The function is hidden and password-protected (for some reason), and generated from the 9-digit entry at cell A1.
