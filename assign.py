def name_args(**info):
    for v in info.keys():
        print(f"{v}: {info[v]}")


name_args(name="River",
weather="fugy",location="city",
time=4)

  
def all_true(iter):
  return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))
print(all_true(("")))



def one_true(iter):
  return any(iter)

print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))
print(one_true(("")))


# 4. recursive_factorial — Uses recursion to find the factorial of an integer.

def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

print(recursive_factorial(2))
print(recursive_factorial(8))



def recursive_deduplicate(my_str,i=0):

  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("AABBCCDD"))
print(recursive_deduplicate("AAMMNBVCXX"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))

# 6. recursive_reverse — Uses recursion to reverse a string.
def recursive_reverse(str, i=0):
  #empty string case
  if len(str)==0:
    return ""
  #base case
  elif i == len(str)-1:
    return str[0]
  else:
    #recursive case
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("cat"))
print(recursive_reverse("orange"))
print(recursive_reverse("mongoose"))
print(recursive_reverse(""))
