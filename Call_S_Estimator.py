"""
S_Estimator example :
Compute Synchronization Indexes for multiple monovariate signals (organized as a list).
"""

""" Import common python packages """
import sys
import os
import numpy as np              # Mathematical package
import pandas as pd             # Time serie package
import matplotlib.pyplot as plt # Plotting package
import csv
sys.path.insert(0, '../src/')       # To be able to import from parent directory

print("\n")
print("*************************************************************************************")
print("This script computes Synchronization indexes for multiple monovariate signals \n" +
      "(orgainized as a list) \n")
print("*************************************************************************************")

""" Import wanted module with every parent packages """
import DataFromManyPersons.Univariate.Continuous.Linear.S_Estimator as S_Estimator
from utils.ExtractSignal import ExtractSignalFromCSV
from utils.ExtractSignal import ExtractSignalFromMAT
from utils.Standardize import Standardize

""" -------------Import signals from a .csv file -----------------------"""
VideoList = ["F1044C.VOB","F1044D1.VOB","F1044D2.VOB","F1044E.VOB","F1044F.VOB",
               "F1044G.VOB","F1044H.VOB","F1044I.VOB","F1044L.VOB","F1044M1.VOB",
               "F1044M2.VOB","F1044N.VOB", "F1044O.VOB", "F1044P.VOB", "F1044Q.VOB",
               "F1044R1.VOB","F1044R2.VOB"]


#for i in VideoList:
#    print i
#    filename = '/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/filtered/'+ i + '.slideddata.csv'
#    print filename
filename = '/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/filtered/F1044R2.VOB.slideddata.csv'


father = ExtractSignalFromCSV(filename, columns = ['slidedFather'])
mother = ExtractSignalFromCSV(filename, columns = ['slidedMother'])
therapist = ExtractSignalFromCSV (filename, columns = ['slidedTherapist'])
#patient = ExtractSignalFromCSV(filename, columns = ['slidedpatient'])
frame_index = ExtractSignalFromCSV(filename, columns = ['frame_index'])
video = ExtractSignalFromCSV(filename, columns = ['video'])

#signals = [father,mother,patient, therapist]
#signals = [patient,mother,therapist]
signals = [father, mother, therapist]

N = signals[0].shape[0]
n = np.arange(0,N)

""" Plot standardized input signals """
Signals = signals
plt.ion()

nrows = len(Signals)
figure, ax = plt.subplots(nrows, sharex=True)

idx = 0
for col in  range(len(Signals)) :
    ax[idx].grid(True) # Display a grid
    ax[idx].set_title('Standardized signal for : ' + Signals[col].columns[0] + ' variable')
    ax[idx].plot(n, Signals[col].iloc[:,0])
    idx += 1

ax[idx-1].set_xlabel('Samples')

""" Define class attributes of the wanted method """
surr_nb_iter = 100
plot_surrogate = False

""" Instanciate the class with its attributes """
print("\n")
try :
## Number of frames by interval used to compute SSI
    numberOfFramesByInterval = 25*10
    #attention ceci est un test pour 30 seconde, a remmettre a 60
    NbOfInterval = len(father)/numberOfFramesByInterval
    #    print(NbOfInterval)
    intervalList = range(NbOfInterval)
    s_estimator = S_Estimator.S_Estimator(surr_nb_iter, plot_surrogate)

except TypeError, err :
    print("TypeError in S_Estimator constructor : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in S_Estimator constructor : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in S_Estimator constructor : \n" + str(e))
    sys.exit(-1)

print("An instance the class is now created with the following parameters:\n" +
      "surr_nb_iter = " + str(surr_nb_iter) + "\n"
      )

""" Compute the method and get the result """
print("\n")
print("Computing...")

try :
    """ List of SSI index for each dyad and the whole group"""
    """ Name of the participants in 2 letters, ordered in alphatebical order"""
    """In this example, there is 4 participants father, mother, patient, therapist,
     sometimes only one some participants are filmed """

# ---------------------- CREATION OF LISTS --------------------------"""

#Dyads
    SSIList_fa_mo = []
    SSIList_fa_th = []
#    SSIList_fa_pa = []
    SSIList_mo_pa = []
    SSIList_mo_th = []
    SSIList_pa_th = []

#Triples
    SSIList_fa_mo_th = []
#    SSIList_fa_pa__mo = []
#    SSIList_fa_pa__th = []
#    SSIList_mo_pa_th = []

#Quadruples
#   SSIList_fa_mo_pa__th = []

    for i in intervalList:
# We divide each data string in a shorter string of the length of numberOfFramesByInterval
        fatherInterval = father[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
        motherInterval = mother[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
#        patientInterval=patient[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
        therapistInterval=therapist[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]

# -------------------- CREATION OF COMBINAISONS --------------------------
#   Dyad
        signals_fa_mo = [fatherInterval,motherInterval]
        signals_fa_th = [fatherInterval,therapistInterval]
#        signals_fa_pa = [fatherInterval,patientInterval]

        signals_mo_th = [motherInterval, therapistInterval]
#        signals_mo_pa = [motherInterval, patientInterval]

#        signals_pa_th = [patientInterval, therapistInterval]

#   Triples
        signals_fa_mo_th = [fatherInterval, motherInterval,therapistInterval]
#        signals_fa_mo_pa = [fatherInterval, motherInterval,patientInterval]
#        signals_fa_pa_th = [fatherInterval, patientInterval,therapistInterval]
#        signals_mo_pa_th = [motherInterval, patientInterval, therapistInterval]

#   Quadruples
#        signals_fa_mo_pa_th = [fatherInterval , motherInterval, patientInterval, therapistInterval]

# -------------------------COMPUTATION CALL ---------------------------

#Dyad
        estimators_fa_mo = s_estimator.compute(*signals_fa_mo)
        SSIList_fa_mo.append(estimators_fa_mo["SSI"])
        print(estimators_fa_mo["SSI"])

        estimators_fa_th = s_estimator.compute(*signals_fa_th)
        SSIList_fa_th.append(estimators_fa_th["SSI"])
        print(estimators_fa_th["SSI"])

#        estimators_fa_pa = s_estimator.compute(*signals_fa_pa)
#        SSIList_fa_pa.append(estimators_fa_pa["SSI"])
#        print(estimators_fa_pa["SSI"])

        estimators_mo_th  = s_estimator.compute(*signals_mo_th)
        SSIList_mo_th.append(estimators_mo_th["SSI"])
#        print(estimators_mo_th["SSI"])

#        estimators_mo_pa  = s_estimator.compute(*signals_mo_pa)
#        SSIList_mo_pa.append(estimators_mo_pa["SSI"])
#        print(estimators_mo_pa["SSI"])

#        estimators_pa_th  = s_estimator.compute(*signals_pa_th)
#        SSIList_pa_th.append(estimators_pa_th["SSI"])
#        print(estimators_pa_th["SSI"])

#Triple
        estimators_fa_mo_th  = s_estimator.compute(*signals_fa_mo_th)
        SSIList_fa_mo_th.append(estimators_fa_mo_th["SSI"])
        print(estimators_fa_mo_th["SSI"])

#        estimators_fa_mo_pa  = s_estimator.compute(*signals_fa_mo_pa)
#        SSIList_fa_mo_pa.append(estimators_fa_mo_pa["SSI"])
#        print(estimators_fa_mo_pa["SSI"])

#        estimators_fa_pa_th  = s_estimator.compute(*signals_fa_pa_th)
#        SSIList_fa_pa_th.append(estimators_fa_pa_th["SSI"])
#        print(estimators_fa_pa_th["SSI"])

#        estimators_mo_pa_th  = s_estimator.compute(*signals_mo_pa_th)
#        SSIList_mo_pa_th.append(estimators_mo_pa_th["SSI"])
#        print(estimators_mo_pa_th["SSI"])

#Quadruples
#        estimators_fa__mo_pa_th  = s_estimator.compute(*signals_fa_mo_pa_th)
#        SSIList_fa_mo_pa_th.append(estimators_fa_mo_pa_th["SSI"])
#        print(estimators_fa_mo_pa_th["SSI"])

#-----------------------CONSOLE FEEDBACK---------------------------
    print(SSIList_fa_mo)
    print(SSIList_fa_th)
    print(SSIList_mo_th)
    print(SSIList_fa_mo_th)
#    print(SSIList_mo_pa)
#    print(SSIList_pa_th)
#    print(SSIList_mo_pa_th)

#-----------------------DATA FRAME EXPORT ---------------------------
    SSIdf = pd.DataFrame({
                        "Time_min" : intervalList,
                        "Interval" : np.arange(1,len(intervalList)+1),
                        "Video" : video,
#Dyads
                        "SSI_fa_mo" : SSIList_fa_mo,
                        "SSI_fa_th" : SSIList_fa_th,
#                        "SSI_fa_pa" : SSIList_fa_pa,

                        "SSI_mo_th" : SSIList_mo_th,
#                        "SSI_mo_pa" : SSIList_mo_pa,
#                        "SSI_pa_th" : SSIList_pa_th,

#Triples
                        "SSI_fa_mo_th" : SSIList_fa_mo_th,
#                        "SSI_fa_pa_mo" : SSIList_fa_pa_mo,
#                        "SSI_fa_pa_th" : SSIList_fa_pa_th,
#                        "SSI_mo_pa_th" : SSIList_mo_pa_th,

#Quadruples
#                       "SSI_fa_mo_pa_th" : SSIList_fa_mo_pa__th
                        })

# add file list
# fusionner des data frames avec panda

    print (SSIdf)
    SSIdf.to_csv("SSI" + "video" + ".csv")

except TypeError, err :
    print("TypeError in S_Estimator computation : \n" + str(err))
    sys.exit(-1)
except ValueError, err :
    print("ValueError in S_Estimator computation : \n" + str(err))
    sys.exit(-1)
except Exception, e :
    print("Exception in S_Estimator computation : \n" + str(e))
    sys.exit(-1)

#""" Display result """
#print("\n")
#print('S_Estimator result :')
#print("\n")

#for i in estimators.keys():
#    print(i + " : " + str(estimators[i]))
#print("\n")

raw_input("Push ENTER key to exit.")
