from __future__ import print_function
import re
expression = '(?<=[QWRTYPSDFGHJKLZXCVBNM])([AEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNM])'
match = re.findall(r'%s'%(expression), input(), re.IGNORECASE)
if match:
    print (*match,sep='\n')
else:
    print (-1)