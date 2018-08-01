import math

# child entropy of grade
# p_slow = float(2)/float(3)
# p_fast = float(1)/float(3)
# formula = -p_slow * math.log(p_slow, 2) - p_fast * math.log(p_fast, 2)

# entropy bumpy
p_bumpy = float(1)
p_smooth = float(1)
formula = -p_bumpy * math.log(p_bumpy, 2) - p_smooth * math.log(p_smooth, 2)



print formula
