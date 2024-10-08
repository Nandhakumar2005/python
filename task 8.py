'''
AUTHOR:Nandhakumar KS
DATE:8-10-2024
to familiarize time and date in various formats
'''

from datetime import datetime
current=datetime.now() #datetime.now() returns the current local date and time
print(current)
format1=current.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current.strftime("%m/%d/%Y")
print(format2)
format3=current.strftime("%a,%B %d,%Y")
print(format3)
format4=current.strftime("%a,%B %d,%Y %H:%M:%S %p")
print(format4)
format5=current.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format5)
format6=current.strftime("%Y-%m-%d")
print(format6)
format7=current.strftime("%H:%M:%S")
print(format7)
format8=current.strftime("%B")
print(format8)
format9=current.strftime("%Y")
print(format9)