import tarfile
import glob
import numpy as np
from matplotlib import pyplot as plt
import os
"""
tar = tarfile.open('/Users/fbzhang2013/Desktop/Data pm 2.5/harvard data/20150101010000.tar')
filename = "README.txt"
try:
    f = tar.getmember(filename)
except KeyError as e:
    print('{0}'.format(e))5
    print('ERROR: Did not find %s in tar archive' % filename)
else:
    print('OK!')

"""

"""
all_tarfiles = os.listdir(folder)
for tarfile in all_tarfiles:
    filename, ext = os.path.splitext(tarfile)
    if ext != '.tar':
        continue
    try:
        os.makedirs(os.path.join(folder, filename))
    except OSError:
        pass
    cmd = 'tar -C "' + os.path.join(folder, filename) + '" -xvf "' + os.path.join(folder, tarfile) + '"'
    os.system(cmd)

A=numpy.genfromtxt('aqi.csv', delimiter=',', skip_header=1, usecols=[5], missing_values={5:'-'})
"""
CITY_ID = '36'
folder = '/Users/fbzhang2013/Desktop/Data pm 2.5/harvard data/'
i_15=0
i_16=0
pm25_value = np.zeros([1,1])
factor = np.zeros([1,10])
pm25_16value = np.zeros([1,1])
factor_16 = np.zeros([1,10])

#FIND_ID = False
temp = np.zeros([1,10])
all_tarfiles = os.listdir(folder)
for tarfile in all_tarfiles:
    if not tarfile.startswith('.'):
        filename, ext = os.path.splitext(tarfile)
        #print(i,filename)
        folder_day = folder + filename + '/'
        os.chdir(folder_day)
        if filename[3] == '5':           
            with open('aqi.csv', encoding='utf-8') as f:
                f.readline()
                for line in f:
                    s = line.split(',')
                    if s[0]==CITY_ID: #ID number
                        if s[-12]!='0' and s[-12]!='' and s[-12]!='-' and \
                           s[-10]!='' and s[-10]!='-' and \
                           s[-9]!='' and s[-9]!='-' and \
                           s[-8]!='' and s[-8]!='-' and \
                           s[-7]!='' and s[-7]!='-' and \
                           s[-6]!='' and s[-6]!='-' and \
                           s[-5]!='' and s[-5]!='-' and \
                           s[-4]!='0' and s[-4]!='' and s[-4]!='-' and \
                           s[-3]!='0' and s[-3]!='' and s[-3]!='-' and \
                           s[-2]!='' and s[-2]!='-':
                            pm25_value = np.append(pm25_value,[[int(s[-12])]],0)
                            temp[0,0] = float(s[-10])
                            temp[0,1] = float(s[-9])
                            temp[0,2] = float(s[-8])
                            temp[0,3] = float(s[-7])
                            temp[0,4] = float(s[-6])
                            temp[0,5] = float(s[-5])
                            temp[0,6] = float(s[-4])
                            temp[0,7] = float(s[-3])
                            temp[0,8] = float(s[-2])
                            temp[0,9] = int(filename)
                            factor = np.append(factor, temp, 0)
                            i_15+=1
                            break
        if filename[3] == '6' and filename[4]+filename[5]=='01':
            with open('aqi.csv', encoding='utf-8') as f:
                f.readline()
                for line in f:
                    s = line.split(',')
                    if s[0]==CITY_ID: #ID number
                        if s[-12]!='0' and s[-12]!='' and s[-12]!='-' and \
                           s[-10]!='' and s[-10]!='-' and \
                           s[-9]!='' and s[-9]!='-' and \
                           s[-8]!='' and s[-8]!='-' and \
                           s[-7]!='' and s[-7]!='-' and \
                           s[-6]!='' and s[-6]!='-' and \
                           s[-5]!='' and s[-5]!='-' and \
                           s[-4]!='0' and s[-4]!='' and s[-4]!='-' and \
                           s[-3]!='0' and s[-3]!='' and s[-3]!='-' and \
                           s[-2]!='' and s[-2]!='-':
                            pm25_16value = np.append(pm25_16value,[[int(s[-12])]],0)
                            temp[0,0] = float(s[-10])
                            temp[0,1] = float(s[-9])
                            temp[0,2] = float(s[-8])
                            temp[0,3] = float(s[-7])
                            temp[0,4] = float(s[-6])
                            temp[0,5] = float(s[-5])
                            temp[0,6] = float(s[-4])
                            temp[0,7] = float(s[-3])
                            temp[0,8] = float(s[-2])
                            temp[0,9] = int(filename)
                            factor_16 = np.append(factor_16, temp, 0)
                            i_16+=1
                            break
print('For city ID {0}, there are {1} points in 2015, and {2} points in Jan, 2016.'.format(CITY_ID, i_15,i_16))
factor = np.delete(factor,0,0)
pm25_value = np.delete(pm25_value,0,0)
factor_16 = np.delete(factor_16,0,0)
pm25_16value = np.delete(pm25_16value,0,0)
print(factor_16.shape,pm25_value.shape)
# Now we arange the data we collected: take average on everday
DayAverFactor = np.zeros([1,10])
DayAver_pm25 = np.array([])
TempFactor = factor[0,np.newaxis]
Daytemp = pm25_value[0,0]
num=0;
for i in range(0,factor.shape[0]-1):
    if(int(factor[i,9]/1000000)==int(factor[i+1,9]/1000000)):
        num+=1
        TempFactor += factor[i+1,np.newaxis]
        Daytemp += pm25_value[i+1,0]
    else:
        if num!=2:
            print('Only {} points on {}'.format(num+1,int(factor[i,9]/1000000)))
        TempFactor = TempFactor/(num+1)
        DayAverFactor = np.append(DayAverFactor,TempFactor,0)
        TempFactor = factor[i+1,np.newaxis]
        Daytemp = Daytemp/(num+1)
        DayAver_pm25=np.append(DayAver_pm25,[Daytemp],0)
        Daytemp = pm25_value[i+1,0]
        num=0
DayAverFactor = np.append(DayAverFactor,TempFactor,0)
DayAver_pm25=np.append(DayAver_pm25,[Daytemp],0)
DayAverFactor=np.delete(DayAverFactor,0,0)
DayAverFactor=np.delete(DayAverFactor,9,1)
num_day = DayAver_pm25.shape[0]
print('Numer of days collected: {}'.format(num_day))

DayAverFactor=np.delete(DayAverFactor,0,0)#Don't need the factors of the first day

DayAverFactor=np.append(DayAverFactor,DayAver_pm25[np.arange(0,DayAver_pm25.shape[0]-1),np.newaxis],1)
DayAver_pm25 = np.delete(DayAver_pm25,0,0)#Begin from the second day
DayAverFactor=np.append(DayAverFactor,np.ones([DayAverFactor.shape[0],1]),1)

regre_dayAver = np.linalg.lstsq(DayAverFactor,DayAver_pm25)
beta_dayAver = regre_dayAver[0]
""" 
#######prediction
DayAverFactor_16 = np.zeros([1,10])
DayAver_pm25_16 = np.array([])
TempFactor = factor_16[0,np.newaxis]
Daytemp = pm25_16value[0,0]
num=0;
for i in range(0,factor_16.shape[0]-1):
    if(math.floor(factor_16[i,9]/1000000)==math.floor(factor_16[i+1,9]/1000000)):
        num+=1
        TempFactor += factor_16[i+1,np.newaxis]
        Daytemp += pm25_16value[i+1,0]
    else:
        TempFactor = TempFactor/(num+1)
        DayAverFactor_16 = np.append(DayAverFactor_16,TempFactor,0)
        TempFactor = factor_16[i+1,np.newaxis]
        Daytemp = Daytemp/(num+1)
        DayAver_pm25_16=np.append(DayAver_pm25_16,[Daytemp],0)
        Daytemp = pm25_16value[i+1,0]
        num=0
num_day_16 = DayAver_pm25_16.shape[0]
DayAver_pm25_16 = DayAver_pm25_16[np.arange(1,num_day_16)] - DayAver_pm25_16[np.arange(0,num_day_16-1)]
DayAverFactor_16=np.delete(DayAverFactor_16,0,0)
DayAverFactor_16=np.delete(DayAverFactor_16,9,1)
DayAverFactor_16=np.append(DayAverFactor_16,np.ones([DayAverFactor_16.shape[0],1]),1)
DayAverFactor_16=np.delete(DayAverFactor_16,DayAverFactor_16.shape[0]-1,0)
DayAver_pm25_16_predict = np.dot(DayAverFactor_16,beta_dayAver)
"""
"""
            #Data=np.genfromtxt('aqi.csv', delimiter=',', skip_header=1, usecols=[0,5,16], missing_values={5:'-'})
            #print(Data.shape)
            if i==0:
                Data=np.genfromtxt('aqi.csv', delimiter=',', skip_header=1, usecols=[0,5], missing_values={5:'-'})
            else:
                temp = np.genfromtxt('aqi.csv', delimiter=',', skip_header=1, usecols=[0,5,-1], missing_values={5:'-'})
                Data = np.vstack([Data,temp])
            i+=1 """
            
