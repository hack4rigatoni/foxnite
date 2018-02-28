#-----------------------------------#
# permutations.                     #
#-----------------------------------#

# input <password> from
# system.arguments
import sys
if not len(sys.argv) == 2:
    print "catnite.py <password>"
    sys.exit(1)


#____________________________________
# CHARACTER SUBSTITUTION OPTIONS
# > dictionary of all letters,
#   |a| -> |a|,|A|,|@|
#    .      .   .   .
options = {}

# take base alphabeth
characters = "abcdefghijklmnopqrstuvwxyz"

# add all CaSe
for char in characters:
  options[char] = [char.lower(),char.upper()]

# special substitutions
options['a'].append('@')
options['e'].append('3')
options['e'].append('&')
options['i'].append('1')
options['i'].append('!')
options['o'].append('0')
options['s'].append('$')

#----------------------
# || -> |p|a|s|s|w|..|d

head = ""
tail = sys.argv[1]

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
#====================================
def permutation(head,tail):

    if len(tail) == 1: # if last char
       for opt in options[tail[0]]:
          print head+opt
       return # done! (end of branch)

    for opt in options[tail[0]]:
       permutation(head+opt,tail[1:])
#------------------------------------
#

# do it!
permutation(head,tail)
