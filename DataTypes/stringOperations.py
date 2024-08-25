#Indexing Operation - One value at a time from string object

s="PYTHON"

#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5

print("s->",s,type(s),id(s))

print(s[0],type(s),id(s))     # P
print(s[5],type(s),id(s))     # N
print(s[2],type(s),id(s))     # T
print(s[3],type(s),id(s))     # H
print(s[4],type(s),id(s))     # O
print(s[-1],type(s),id(s))    # N
print(s[-6],type(s),id(s))    # P
print(s[-5],type(s),id(s))    # Y
print(s[-2],type(s),id(s))    # O
print(s[-3],type(s),id(s))    # H
print(s[-4],type(s),id(s))    # T
#print(s[10],type(s),id(s))    # IndexError
#print(s[-11],type(s),id(s))    # IndexError

s="Java Programming Language"
print("s->",s,type(s),id(s))

print(s[0])                  # J
print(s[-len(s)])            # J
print(s[-1])                 # e
print(s[len(s)-1])           # e


#String Slicing - To extract substring from main string

#Syntax #1->stringObject[BEGIN:END] BEGIN<END?substring:' ' till END-1 characters
s="PYTHON"
#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5
print(s,type(s),id(s))
print("s[0:4]->",s[0:4])      # PYTH
print("s[4:0]->",s[4:0])      # ' ' OR Space
print("s[0:3]->",s[0:3])      # PYT
print("s[2:6]->",s[2:6])      # THON
print("s[1:5]->",s[1:5])      # YTHO
print("s[3:6]->",s[3:6])      # HON
print("s[4:1]->",s[4:1])      # ' ' OR Space
print("s[1:6]->",s[1:6])      # YTHON
print("s[0:6]->",s[0:6])      # PYTHON
print("s[4:6]->",s[4:6])      # ON

print("Negative indexes")
print("s[-6:-2]->",s[-6:-2])      # PYTH
print("s[-5:-1]->",s[-5:-1])      # YTHO
print("s[-1:-5]->",s[-1:-5])      # ' ' OR Space
print("s[-5:-3]->",s[-5:-3])      # YT
print("s[-6:-4]->",s[-6:-4])      # PY
print("s[-3:-1]->",s[-3:-1])      # HO
print("s[-4:-1]->",s[-4:-1])      # THO

print("Special Sub Points")
# Note : Check for direction if range(END=END-1) fits then output is substring else Space 

print("Whenever BEGIN is +VE and END is -VE Indexes.")
print("s[0:-4]->",s[0:-4])      # PY
print("s[2:-1]->",s[2:-1])      # THO
print("s[1:-4]->",s[1:-4])      # Y
print("s[0:-1]->",s[0:-1])      # PYTHO
print("s[3:-5]->",s[3:-5])      # ' ' OR Space
print("s[2:-3]->",s[2:-3])      # T
print("s[3:-4]->",s[2:-4])      # ' ' OR Space
print("s[0:-2]->",s[0:-2])      # PYTH

print("When BEGIN Index is -VE and END is +VE")
print("s[-6:4]->",s[-6:4])      # PYTH
print("s[-4:5]->",s[-4:5])      # THO
print("s[-5:5]->",s[-5:5])      # YTHO
print("s[-6:6]->",s[-6:6])      # PYTHON
print("s[-3:5]->",s[-3:5])      # HO
print("s[-2:4]->",s[-2:4])      # ' ' OR Space
print("s[-2:5]->",s[-2:5])      # O
print("s[-5:2]->",s[-5:2])      # Y
print("s[-6:1]->",s[-6:1])      # P
print("s[-len(s):len(s)]->",s[-len(s):len(s)])      # PYTHON

print("Most special points")
print("s[0:140]->",s[0:140])    # PYTHON
print("s[2:200]->",s[2:200])    # THON
print("s[1:180]->",s[1:180])    # YTHON
print("s[3:200]->",s[3:200])    # HON

print("BEGIN is -VE and Out of range")
print("s[-100:-2]->",s[-100:-2]) # PYTH
print("s[-30:-6]->",s[-30:-6])   # ' ' OR Space
print("s[6:100]->",s[6:100])     # ' ' OR Space
print("s[-20:-5]->",s[-20:-5])   # P
print("s[-15:-1]->",s[-15:-1])   # PYTHO


print("Other way or format to provide index")
print("s[-100:100]->",s[-100:100])               # PYTHON 
print("s[100:-100]->",s[100:-100])               # 
print("s[-100:0]->",s[-100:0])                   # ' '
print("s[-100:1]->",s[-100:1])                   # P
print("s[-1000:7]->",s[-1000:7])                 # IndexError
print("s[200:-len(s)]->",s[200:-len(s)])         # ' '
print("s[0b0101:0b1010]->",s[0b0101:0b1010])     # s[5:10]->N
print("s[False:True]->",s[False:True])           # P
print("s[-6:0]->",s[-6:0])                       # ' '

#Syntax #2->stringObject[BEGIN:]
#s="PYTHON"
#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5

print("Syntax #2->stringObject[BEGIN:]-> with Indedx as +VE")
print("s->",s) # PYTHON
print("s[2:]->",s[2:]) # THON
print("s[4:]->",s[4:]) # ON
print("s[3:]->",s[3:]) # HON
print("s[1:]->",s[1:]) # YTHON
print("s[0:]->",s[0:]) # PYTHON
print("s[5:]->",s[5:]) # N

print("Syntax #2->stringObject[BEGIN:]-> with Indedx as -VE")
print("s[-4:]->",s[-4:]) # THON
print("s[-6:]->",s[-6:]) # P
print("s[-3:]->",s[-3:]) # HON
print("s[-1:]->",s[-1:]) # N
print("s[-2:]->",s[-2:]) # ON
print("s[-5:]->",s[-5:]) # YTHON
print("s[-len(s):]->",s[-len(s):]) # PYTHON
print("s[-100:]->",s[-100:])       # PYTHON
print("s[-10:]->",s[-10:])         # PYTHON

print("Syntax #3->stringObject[:END] till END-1 and END is +VE")
print("s[:3]->",s[:3]) # PYT
print("s[:6]->",s[:6]) # PYTHON
print("s[:2]->",s[:2]) # PY
print("s[:5]->",s[:5]) # PYTHO
print("s[:4]->",s[:4]) # PYTH
print("s[:1]->",s[:1]) # P
print("s[:0]->",s[:0]) # ' '

#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5
print("Syntax #3->stringObject[:END] till END-1 and END is -VE")
print("s[:-3]->",s[:-3]) # PYT
print("s[:-2]->",s[:-2]) # PYTH
print("s[:-1]->",s[:-1]) # PYTHO
print("s[:-4]->",s[:-4]) # PY
print("s[:-5]->",s[:-5]) # P
print("s[:-6]->",s[:-6]) # ' '
print("s[:-7]->",s[:-7]) # ' '
print("s[:-177]->",s[:-177]) # ' '

#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5
print("Syntax #4->stringObject[:]")
print("s[:]->",s[:])           # PYTHON
print("s[0:]->",s[0:])         # PYTHON
print("s[-120:]->",s[-120:])   # PYTHON
print("s[:100]->",s[:100])     # PYTHON
print("s[0:6]->",s[0:6])       # PYTHON

print("Syntax #5->stringObject[BEGIN : END : STEP]")
print("Rule 2 : STEP is +VE -> Forward Direction BEGIN<END?END-1:SPACE")
print("s[0:6]->",s[0:6])            # PYTHON
print("s[0:6:1]->",s[0:6:1])        # PYTHON
print("s[0:6:2]->",s[0:6:2])        # PTO
print("s[2:6:2]->",s[2:6:2])        # TO
print("s[1:5:2]->",s[1:5:2])        # YH
print("s[2:6:3]->",s[2:6:3])        # TN
print("s[1:6:3]->",s[1:6:3])        # YO
print("s[1:5:4]->",s[1:5:4])        # Y
print("s[4:2:1]->",s[4:2:1])        # ' ' OR Space    
print("s[-6:-1:3]->",s[-6:-1:3])    # PH
print("s[-6:-1:2]->",s[-6:-1:2])    # PTO
print("s[-5:-1:3]->",s[-5:-1:3])    # YO
print("s[-3:-6:1]->",s[-3:-6:1])    # ' '
print("s[-6:-1:4]->",s[-6:-1:4])    # PO

print("s[::]->",s[::])              # PYTHON
print("s[:]->",s[:])                # PYTHON
print("s[::1]->",s[::1])            # PYTHON
print("s[::2]->",s[::2])            # PTO
print("s[::3]->",s[::3])            # PH
print("s[::4]->",s[::4])            # PO
print("s[::40]->",s[::40])          # P


print("s[2::2]->",s[2::2])         # TO
print("s[3::3]->",s[3::3])         # H
print("s[1::4]->",s[1::4])         # YN
print("s[2::]->",s[2::])           # THON
print("s[-6::2]->",s[-6::2])       # PTO
print("s[-4::1]->",s[-4::1])       # THON
print("s[-3::3]->",s[-3::3])       # H

#-6    -5   -4   -3   -2   -1
# P    Y    T    H    O    N
# 0    1    2    3    4    5
print("Rule 3 : STEP is -VE -> backward Direction BEGIN>END?END+1:SPACE")
print("s[4:0:-1]->",s[4:0:-1])                   # OHTY
print("s[5:2:-1]->",s[5:2:-1])                   # NOH
print("s[5:1:-1]->",s[5:1:-1])                   # NOHT
print("s[5:3:-1]->",s[5:3:-1])                   # NO
print("s[5:2:-1]->",s[5:2:-2])                   # NH
print("s[5:0:-3]->",s[5:0:-3])                   # NT
print("s[4:0:-2]->",s[4:0:-2])                   # OT

print("s[-6:-1:-2]->",s[-6:-1:-2])               # ' '
print("s[-1:-6:-1]->",s[-1:-6:-1])               # NOHTY
print("s[-1:-6:-2]->",s[-1:-6:-2])               # NHY
print("s[-2:-7:-2]->",s[-2:-7:-2])               # OTP
print("s[-2:-20:-2]->",s[-2:-20:-2])             # OTP
print("s[-1:-4:-3]->",s[-1:-4:-3])               # N
print("s[::-1]->",s[::-1])                       # NOHTYP

print("Rule 4 : END = 0 and direction is Forward then Space")
print("s[:0:1]->",s[:0:1])                       # ' '
print("s[:0:2]->",s[:0:2])                       # ' '
print("s[:0:3]->",s[:0:3])                       # ' '

print("Rule 5 : END = -1 and direction is Backward then Space")
print("s[:-1:-1]->",s[:-1:-1])                  # ' '
print("s[:-1:-2]->",s[:-1:-2])                  # ' '
print("s[:-1:-3]->",s[:-1:-3])                  # ' '

print("SPECIAL POINTS")
s="MADAM"

print("MADAM->s[::1]==s[::-1]->",s[::1]==s[::-1])     # True
# M A D A M
# M A D A M
# Palindrome
s1="LIRIL"

print("LIRIL->s1[::1]==s1[::-1]->",s1[::1]==s1[::-1])    # True
# L I R I L
# L I R I L
# Palindrome
s2="RACECAR"
print("RACECAR->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])    # True

s2="MOM"
print("MOM->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])        # True

s2="DAD"
print("DAD->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])        # True

s2="MALAYALAM"
print("MALAYALAM->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])  # True

s2="RADAR"
print("RADAR->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])      # True

s2="WOW"
print("WOW->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])        # True

s2="PYTHON"
print("PYTHON->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])    # False

s2="JAVA"
print("JAVA->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])      # False

s2="1221"
print("1221->s2[::1]==s2[::-1]->",s2[::1]==s2[::-1])     # True
