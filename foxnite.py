#-----------------------------------#
# permutations.                     #
#-----------------------------------#

# input <password> from
# system.arguments
import sys
if not len(sys.argv) in [2,3]:
    print "%s <password>" % sys.argv[0]
    sys.exit(1)

if len(sys.argv) == 3:
    if sys.argv[1] == 'x':
       password = sys.argv[2]
       determined = True
    else:
       print "%s <password>" % sys.argv[0]
       sys.exit(1)

if len(sys.argv) == 2:
    password = sys.argv[1]
    determined = False

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
tail = password

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


# before we go..
if not determined:
    from prudent_fox import warning
    warning(tail,options)

# do it!
permutation(head,tail)
