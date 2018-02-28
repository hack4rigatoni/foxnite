#-----------------------------------#
# permutations. filtered.           #
#-----------------------------------#

# input <password> from
# system.arguments
import sys
if not len(sys.argv) == 2:
    print "catnite.py <password>"
    sys.exit(1)


#____________________________________
# CHARACTER SUBSTITUTION OPTIONS
options = {}

# base alphabeth
characters = "abcdefghijklmnopqrstuvwxyz"

# CaSe
for char in characters:
  options[char] = [(char.lower(),0),(char.upper(),1)]

# special substitutions
options['a'].append(('@',1000))
options['e'].append(('3',1000))
options['e'].append(('&',1000))
options['i'].append(('1',1000))
options['i'].append(('!',1000))
options['o'].append(('0',1000))
options['s'].append(('$',1000))

#------------------------------------
# ENTROPY CHECK..
# > reduce dictionary size by limiting
#   the number of substitutions
#------------------------------------
# Uppercase weight    = 1
# Special char weight = 1000
#
#

#==== FIDDLE HERE!! ===========
# max & min number of uppercase
maxupper   = 8
minupper   = 4
# max & min sobsitutions
maxspecial = 6   * 1000 # scale up
minspecial = 3   * 1000 # 4 comparison


# || -> |p|a|s|s|w|..|d

head = ""
tail = sys.argv[1]

entropy = 0

# head  options   tail
#-----------------------------------
# |p| -> |a| -> |s|..|d
#            -> |S|..|d
#            -> |$|..|d

#     -> |A| -> |s|..|d
#            -> |S|..|d
#            -> |$|..|d

#     -> |@| -> |s|..|d
#            -> |S|..|d
#            -> |$|..|d

#____________________________________
#####################################
def permutation(head,tail,entropy):

    if entropy % 1000 > maxupper:
       return # too many uppercases

    if entropy > maxspecial:
       return # too many synbols

    if len(tail) == 1: # if last char
       for opt,entr in options[tail[0]]:

          if entropy < minspecial:
             return # too few synbols

          if entropy % 1000 < minupper:
             return # too few uppercases

          print head+opt
       return # done! (end of branch)

    ########## RECURSION #########################
    for opt,entr in options[tail[0]]:
       permutation(head+opt,tail[1:],entropy+entr)
#____________________________________


# do it!
permutation(head,tail,entropy)
