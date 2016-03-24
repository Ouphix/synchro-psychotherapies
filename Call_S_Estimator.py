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

for i in VideoList:
    videoName = (i[0:len(i)-4])
    print videoName
    filename = '/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/filtered/'+ i + '.slideddata.csv'

    father = ExtractSignalFromCSV(filename, columns = ['slidedFather'])
    mother = ExtractSignalFromCSV(filename, columns = ['slidedMother'])
    therapist = ExtractSignalFromCSV (filename, columns = ['slidedTherapist'])
    patient = ExtractSignalFromCSV(filename, columns = ['slidedPatient'])
    frame_index = ExtractSignalFromCSV(filename, columns = ['frame_index'])
    video = ExtractSignalFromCSV(filename, columns = ['video'])

    fatherBOOL = True
    motherBOOL = True
    therapistBOOL = True
    patientBOOL = True
    participantsList = [father, mother, therapist, patient]

    if (father['slidedFather'].isnull()).all():
# IF Only NA becomes False
        fatherBOOL = False

    if (mother['slidedMother'].isnull()).all():
# IF Only NA becomes False
        motherBOOL = False

    if (patient['slidedPatient'].isnull()).all():
        patientBOOL = False

    if (therapist['slidedTherapist'].isnull()).all():
        therapistBOOL = False

    participantsBOOLList = [fatherBOOL, motherBOOL, therapistBOOL, patientBOOL]

    signals = []
    for i in range(4):
# if participant present, TRUE and add it to the list
        if participantsBOOLList[i]:
            signals.append(participantsList[i])

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
        SSIList_fa_mo = []
        SSIList_fa_mo_pa = []
        SSIList_fa_mo_pa_th = []
        SSIList_fa_mo_th = []
        SSIList_fa_pa = []
        SSIList_fa_pa_th = []
        SSIList_fa_th = []
        SSIList_mo_pa = []
        SSIList_mo_pa_th = []
        SSIList_mo_th = []
        SSIList_pa_th = []

        for i in intervalList:
# We divide each data string in a shorter string of the length of numberOfFramesByInterval
            fatherInterval = father[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
            motherInterval = mother[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
            patientInterval = patient[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
            therapistInterval = therapist[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]

# -------------------- CREATION OF COMBINAISONS --------------------------
            signals_fa_mo = [fatherInterval,motherInterval]
            signals_fa_th = [fatherInterval,therapistInterval]
            signals_fa_pa = [fatherInterval,patientInterval]
            signals_mo_th = [motherInterval, therapistInterval]
            signals_mo_pa = [motherInterval, patientInterval]
            signals_pa_th = [patientInterval, therapistInterval]
            signals_fa_mo_th = [fatherInterval, motherInterval, therapistInterval]
            signals_fa_mo_pa = [fatherInterval, motherInterval, patientInterval]
            signals_fa_pa_th = [fatherInterval, patientInterval, therapistInterval]
            signals_mo_pa_th = [motherInterval, patientInterval, therapistInterval]
            signals_fa_mo_pa_th = [fatherInterval , motherInterval, patientInterval, therapistInterval]

# -------------------------COMPUTATION CALL ---------------------------
#        print(video[0:NbOfInterval].reset_index())
            if fatherBOOL:
                if motherBOOL:
                    estimators_fa_mo = s_estimator.compute(*signals_fa_mo)
                    SSIList_fa_mo.append(estimators_fa_mo["SSI"])
                    if patientBOOL:
                        estimators_fa_mo_pa  = s_estimator.compute(*signals_fa_mo_pa)
                        SSIList_fa_mo_pa.append(estimators_fa_mo_pa["SSI"])
                        if therapistBOOL:
                            estimators_fa_mo_pa_th  = s_estimator.compute(*signals_fa_mo_pa_th)
                            SSIList_fa_mo_pa_th.append(estimators_fa_mo_pa_th["SSI"])
                    if therapistBOOL:
                        estimators_fa_mo_th  = s_estimator.compute(*signals_fa_mo_th)
                        SSIList_fa_mo_th.append(estimators_fa_mo_th["SSI"])
                if patientBOOL:
                    estimators_fa_pa = s_estimator.compute(*signals_fa_pa)
                    SSIList_fa_pa.append(estimators_fa_pa["SSI"])
                    if therapistBOOL:
                        estimators_fa_pa_th  = s_estimator.compute(*signals_fa_pa_th)
                        SSIList_fa_pa_th.append(estimators_fa_pa_th["SSI"])
                if therapistBOOL:
                    estimators_fa_th = s_estimator.compute(*signals_fa_th)
                    SSIList_fa_th.append(estimators_fa_th["SSI"])

            if motherBOOL:
                if patientBOOL:
                    estimators_mo_pa  = s_estimator.compute(*signals_mo_pa)
                    SSIList_mo_pa.append(estimators_mo_pa["SSI"])
                    if therapistBOOL:
                        estimators_mo_pa_th  = s_estimator.compute(*signals_mo_pa_th)
                        SSIList_mo_pa_th.append(estimators_mo_pa_th["SSI"])
                if therapistBOOL:
                    estimators_mo_th  = s_estimator.compute(*signals_mo_th)
                    SSIList_mo_th.append(estimators_mo_th["SSI"])

            if patientBOOL:
                if therapistBOOL:
                    estimators_pa_th  = s_estimator.compute(*signals_pa_th)
                    SSIList_pa_th.append(estimators_pa_th["SSI"])

    #-----------------------CONSOLE FEEDBACK---------------------------
    #    print(SSIList_fa_th)
    #    print(SSIList_mo_th)
    #    print(SSIList_fa_mo_th)
    #    print(SSIList_mo_pa)
    #    print(SSIList_pa_th)
    #    print(SSIList_mo_pa_th)

    #-----------------------DATA FRAME EXPORT ---------------------------
        video = video[0:NbOfInterval].reset_index()
        video = (video.iloc[:,1])

        time_min=[]
        for i in intervalList:
            time_min.append(float(i)/6)

        SSIdf = pd.DataFrame({"Time_min" : time_min,
                            "Interval" : np.arange(1,len(intervalList)+1),
                            "video" : video})
        if len(SSIList_fa_pa) > 0:
            SSIdf_fa_pa = pd.DataFrame({"SSI_fa_pa" : SSIList_fa_pa})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_pa], axis=1)

        if len(SSIList_fa_mo) > 0:
            SSIdf_fa_mo = pd.DataFrame({"SSI_fa_mo" : SSIList_fa_mo})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo], axis=1)

        if len(SSIList_fa_mo_pa) > 0:
            SSIdf_fa_mo_pa = pd.DataFrame({"SSI_fa_mo_pa" : SSIList_fa_mo_pa})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo_pa], axis=1)

        if len(SSIList_fa_mo_pa_th) > 0:
            SSIdf_fa_mo_pa_th = pd.DataFrame({"SSI_fa_mo_pa_th" : SSIList_fa_mo_pa_th})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo_pa_th], axis=1)

        if len(SSIList_fa_mo_th) > 0:
            SSIdf_fa_mo_th = pd.DataFrame({"SSI_fa_mo_th" : SSIList_fa_mo_th})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo_th], axis=1)

        if len(SSIList_fa_pa_th) > 0:
            SSIdf_fa_pa_th = pd.DataFrame({"SSI_fa_pa_th" : SSIList_fa_pa_th})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_pa_th], axis=1)

        if len(SSIList_fa_th) > 0:
            SSIdf_fa_th = pd.DataFrame({"SSI_fa_th" : SSIList_fa_th})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_th], axis=1)

        if len(SSIList_mo_pa) > 0:
            SSIdf_mo_pa = pd.DataFrame({"SSI_mo_pa" : SSIList_mo_pa})
            SSIdf = pd.concat([SSIdf, SSIdf_mo_pa], axis=1)

        if len(SSIList_mo_pa_th) > 0:
            SSIdf_mo_pa_th = pd.DataFrame({"SSI_mo_pa_th" : SSIList_mo_pa_th})
            SSIdf = pd.concat([SSIdf, SSIdf_mo_pa_th], axis=1)

        if len(SSIList_mo_th) > 0:
            SSIdf_mo_th = pd.DataFrame({"SSI_mo_th" : SSIList_mo_th})
            SSIdf = pd.concat([SSIdf, SSIdf_mo_th], axis=1)

        if len(SSIList_pa_th) > 0:
            SSIdf_pa_th = pd.DataFrame({"SSI_pa_th" : SSIList_pa_th})
            SSIdf = pd.concat([SSIdf, SSIdf_pa_th], axis=1)

        if SSIdf.empty:
            print("Empty Data Frame")
        else:
            print("SSIdf")
            print(i)
            print(SSIdf)
#            print(SSIdf.shape)
    #        print("SSIdf_fa_mo")
    #        print (SSIdf_fa_mo)
    #        print (SSIdf_fa_mo.shape)
    #        print("SSIdf_fa_pa")
    #        print (SSIdf_fa_pa)
    #        print (SSIdf_fa_pa.shape)
    #        print(video)
    #        print(video.shape)
    #        c = pd.concat([SSIdf, video], axis=1)
#            del SSIdf['Time_min']
#            del SSIdf['Time (ms)']
    #        print(c.shape)
    #        print (c.columns)
    #        print(c)

    # add file list
    # fusionner des data frames avec panda

#        SSIdf.to_csv("SSI" + video + ".csv")
#        print(video)
        SSIdf.to_csv("/SyncPy/examples/SynchronyCSV/SSI"+videoName+".csv")

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
