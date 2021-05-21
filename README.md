Error Digit Range 

A programmer wrote a data translation function, but it has a bug. 
It reads in a series of digits from a foreign system and converts them to their local equivalents. 
The bug causes it to translate one of the digits wrong. For example, the input data value is 11897. 
If the bug relates to the 1 digits, and it translates them as 9 local equivalent, the function returns 99899. 
Notice that the 9in the original | value is not affected. Only the 1 value will be translated wrong under these assumptions. 

Any 1 of the 10 possible digits in the input value, 

the digits 0-9, will be replaced with any other 1 of the possible 10 digits. 

Without knowing which digit value is translated wrong, analyze a number to find the maximum and 
minimum values that might be returned from the function. 
Return the difference in these values.

Note: 
• A translation cannot change the number of significant digits in the input. 
• The first digit of the output cannot be 0.

Example 0 

num = 111

The maximal value replaces each '1'with a '9' : 999 The first digit cannot be 0 the only value less than 1, so no substitutions are made. 
The minimal value is 111

Their difference is 999-111 = 888 

Example 1 :
num = 10018 

The maximal value replaces each ‘1’with a ‘9' : 90098

The minimal value replaces each ‘8' with a '0' : 10010 
The difference ta return is 90098 - 10010 = 80088 

Function Description 

Complete the findRange function in the editor below. 

findRange has the following parameter(s): int num :  the correct integer input 

Return: 
long int: the differenca between the maximum possible return values

Constraints :
1<= num<= 10^9

| Sample Input 0 

    123512 

| Sample Output 0 


    820082 

Explanation :

• The maximum possible reconstruction is 923592 when 1 is interpreted as 9

• The minimum possible reconstruction is 103510 when 2 is interpreted as 0, 

• Thus the difference is 820082.


| Sample input 1 

     909 


| Sample Output 1 


     898 

Explanation :

• The maximum possible reconstruction is 999 when 0 is interpreted as 9.

• The minimum possible reconstruction is 101 when 9 is interpreted as 1.

