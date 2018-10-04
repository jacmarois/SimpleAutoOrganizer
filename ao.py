import os
from datetime import datetime
import tkinter
from tkinter.filedialog import askdirectory

while True:
    cont = ''
    tkinter.Tk().withdraw()
    path = tkinter.filedialog.askdirectory(initialdir="/",title='Please select a directory')
    if len(path) > 0:
        print("\nYou chose %s" % path)

    cont = input("Are you sure you want to oraganize the files in this folder? (y/n)\n")
    print('\n')
    if (str(cont) == 'y') or (str(cont) == 'Y'):
        break

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

yrs = []
mths = []
days = []

mthnm = ['January', 'Februrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

num = 0
for i in files:
    yrs.append(datetime.fromtimestamp(os.path.getmtime(path + "\\" + files[num])).strftime('%Y'))
    mths.append(datetime.fromtimestamp(os.path.getmtime(path + "\\" + files[num])).strftime('%m'))
    days.append(datetime.fromtimestamp(os.path.getmtime(path + "\\" + files[num])).strftime('%d'))
    num += 1

num = 0
for i in yrs:
    if files[num] != 'ao.py':
        if not os.path.exists(path + "\\" + yrs[num] + "\\" + mths[num] + " - " + mthnm[int(mths[num]) - 1] + "\\" + days[num]):
            os.makedirs(path + "\\" + yrs[num] + "\\" + mths[num] + " - " + mthnm[int(mths[num]) - 1] + "\\" + days[num])
    num += 1

num = 0
count = 0
for f in files:
    if files[num] != 'ao.py':
        os.rename(path + "\\" + files[num], path + "\\" + yrs[num] + "\\" + mths[num] + " - " + mthnm[int(mths[num]) - 1] + "\\" + days[num] + "\\" + files[num])
        count += 1
    num += 1

print(str(count) + ' files moved.')
input('Press enter to exit')
