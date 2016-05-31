"""
Correlation example:
It computes the linear correlation between two continuous univariate signals x and y (in pandas DataFrame format) as a function of their delay tau.
It computes autocorrelation when y coincides with x.
"""
projectDirectory = "/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/Git/Monrado"
dataFolder = projectDirectory + "/Data/CSV/filtered/noLog/"
outputDirectory = projectDirectory + "/Data/CSV/Synchrony/noLog/correlation/SSI"

""" Import common python packages """
import sys

import numpy as np              # Mathematical package
import pandas as pd             # data frame package
import matplotlib
matplotlib.use('agg')
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
 # Plotting package
import csv
sys.path.insert(0, '../src/')       # To be able to import from parent directory

## Name of the videos to import
VideoList = os.listdir(dataFolder)
print VideoList

print ("\n")
print("***********************************************************************************************************************")
print("This scripts computes the correlation between two univariate signals."
       "First input is a sinewave of 1 Hz frequency, the second one\n is the sum of this sinewave"
       "with a gaussian random process having zero mean and unitary\n variance.")
print("************************************************************************************************************************")

""" Import wanted module with every parent packages """
import DataFrom2Persons.Univariate.Continuous.Linear.Correlation as Correlation

""" Import Utils modules """
from utils import Standardize
from utils.ExtractSignal import ExtractSignalFromCSV

""" Define signals in pd.dataFrame format """

#Define parameters
N=1024 # number of samples
f=1.0  # sinewave frequency (Hz)
Fs=200 # sampling frequency (Hz)

n=np.arange(0,N)#number of samples

""" Import signals from a .csv file """
#for videoName in VideoList[2]:
if True:
    videoName = "BALU062.slideddata.csv"

#    if not videoName.endswith(".csv") :
#        continue
    print videoName

    filename = dataFolder + videoName
    print filename

    fatherBOOL = True
    motherBOOL = True
    childBOOL = True

#    father = ExtractSignalFromCSV(filename, columns = ['slidedFather'])
    x = ExtractSignalFromCSV(filename, columns = ['slidedMother'])
    y = ExtractSignalFromCSV(filename, columns = ['slidedChild'])
    frame_index = ExtractSignalFromCSV(filename, columns = ['frame_index'])
    video = ExtractSignalFromCSV(filename, columns = ['video'])

    print x
    x = x.reset_index(drop=True)
    print x.shape
    print x
#    print y
    y = y.reset_index(drop=True)
    print y.shape

#     if (father['slidedFather'].isnull()).all():
# # IF Only NA becomes False
#         fatherBOOL = False

    if (x['slidedMother'].isnull()).all():
# IF Only NA becomes False
        motherBOOL = False

#Data from files
# filename = 'data_examples/2Persons_Univariate_Continuous_data.csv'

# x = ExtractSignalFromCSV(filename, columns = ['x1'])
# y = ExtractSignalFromCSV(filename, columns = ['x2'])
# n=np.arange(0,x.shape[0])


# """Plot input signals"""
# plt.ion()
# f, axarr = plt.subplots(2, sharex=True)
# axarr[0].set_title('Input signals')
# axarr[0].set_xlabel('Samples')
# axarr[1].set_xlabel('Samples')
#
# axarr[0].plot(n, x, label="x")
# axarr[1].plot(n, y, label="y", color='r')
# axarr[0].legend(loc='best')
# axarr[1].legend(loc='best')

""" Define class attributes of the wanted method """

tau_max = 999                       # the maximum lag at which correlation should be computed (in samples)
plot=True                           # plot of the correlation fucntion
standardization = True              # standardization of the time series to mean 0 and variance 1
corr_tau_max = True                 # return of the maximum of correlation and its lag
corr_coeff = True                   # computation of the correlation coefficient (Pearson's version)
scale=True                          # scale factor to have correlaton in [-1,1]

""" Instantiate the class with its attributes """
print("\n")

try :
    c=Correlation.Correlation(tau_max, plot, standardization, corr_tau_max, corr_coeff, scale)
except TypeError, err :
    print("TypeError in Correlation constructor : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in Correlation constructor : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in Correlation constructor : \n" + str(e))
    sys.exit(-1)

print("An instance of the class is now created with the following parameters:\n" +
      "tau max = " + str(tau_max) + "\n" +
      "plot = " + str(plot) + "\n" +
      "standardization= " + str(standardization) + "\n" +
      "corr_tau_max = " + str(corr_tau_max) + "\n" +
      "corr_coeff =" + str(corr_coeff) +"\n" +
      "scale =" + str(scale))

""" Compute the method and get the result """
print("\n")
print("Computing...")

try :
    res= c.compute(x, y)
except TypeError, err :
    print("TypeError in Correlation computation : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in Correlation computation : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in Correlation computation : \n" + str(e))
    sys.exit(-1)

""" Display result """
print("\n")
print("**************************************** \n")
print('Correlation complete result :')
print("****************************************\n")
print("Correlation function array:")
print(res['corr_funct'])

#res.to_csv(outputDirectory + videoName)

if corr_tau_max:
    print("Maximum value of the correlation %f and lag (in samples) %d:" %(res['max_corr'],res['t_max']))

if corr_coeff:
    print("Pearson's correlation coefficient %f:" %(res['corr_coeff']))



raw_input("Push ENTER key to exit.")
plt.close("all")
