# foxnite
Possibly elegant dictionary generator for password capitalizaion/encoding.
 
*to the frosty nights when foxes dance in the snow..*

Usage:
----
 - python foxnite.py < password >
 
    all possible permutation of the password considering capitalization and common substitutions 'e' -> '3','&'
 
 - python ice-foxnite.py < a_very_long_password >
 
    reduces dictionary size by introducing rules. 'max_capitals' -> 8 , 'min_capitals' -> 4 will only output results with at least 4 capitalized letters and no more than 8. Look at the code for more..
 
