# Process of extracting mutiple / chacacter at a time / simultaneously


print('--------------Positive Slicing---------------')

#  SYNTAX
#   var_name[start index:end index: stepvalue]

# Start index :- From where to you start , default '0'
#  Step value : (JUMP) It can be +ve or -ve but  it cannot be '0'  default '1'


a='banglore'
print(len(a))
print(a[0:8:1])
print(a[0:9:2])
print(a[::])
print(a[0:9:2])

# O/P:-8
# O/P:-banglore
# O/P:-bnlr
# O/P:-banglore
# O/P:-bnlr


print('--------------Negative Slicing---------------')

# SYNTAX
#   var_name[start index:end index: stepvalue]


print(a[-9:-2])
print(a[-5])
print(a[-5:-9])
print(a[-1])
#
# O/P:-banglo
# O/P:-g
# O/P:-
# O/P:-e

print('--------------Combination Slicing---------------')


# SYNTAX
#   var_name[start index:end index: stepvalue]

b='India is best'
print(b[-13:13:1])
print(b[1:-2:1])
print(b[13::-1])
print(b[3:-5:1])
print(b[-4:4:-1])


# O/P:India is best
# O/P:ndia is be
# O/P:tseb si aidnI
# O/P:ia is
# O/P:b si
