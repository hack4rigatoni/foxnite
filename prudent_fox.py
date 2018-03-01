import sys

#=====================================
# File Size Human Formatting.
# By > Sridhar Ratnakumar & Wai Ha Lee
#-------------------------------------
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

def usure():
   pass 


#_________!!!_________
#=====================
def warning(tail,options):

    # calc characters factors
    # p a s s w o r d
    # 2*3*3*3*2*3*2*2 = all combos

    permutations = 1
    for char in tail:
       permutations *= len(options[char])

    psw_size = len(tail)

    # One Byte for each char + \n
    file_size = permutations * (psw_size+1)

    print "This password will generate %i permutations." % permutations
    print "Predicted dictionary size: %s" % sizeof_fmt(file_size)
    print
    print "if that is ok, run:  python foxnite.py x password > dictionary"
    sys.exit(0)

