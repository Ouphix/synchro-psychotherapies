"""
S_Estimator example :
Compute Synchronization Indexes for multiple monovariate signals (organized as a list).
"""

""" Editable content """
## Place of your data folder (filtered data)
projectDirectory = "/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/Git/Monrado"
dataFolder = projectDirectory + "/Data/CSV/filtered/noLog/"
outputDirectory = projectDirectory + "/Data/CSV/Synchrony/noLog/S_estimator/SSI."


## Number of frames by interval used to compute SSI. Nota bene, there are 25 frames by second.
numberOfFramesByInterval = 25*5

""" Import common python packages """
import sys
import os
import numpy as np              # Mathematical package
import pandas as pd             # data frame package
import matplotlib
matplotlib.use('agg')
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
 # Plotting package
import csv
sys.path.insert(0, '../src/')       # To be able to import from parent directory

## Name of the videos to import
VideoList = os.listdir(dataFolder)
print VideoList

print("\n")
print("**********************************************************************")
print("This script computes Synchronization indexes for multiple monovariate signals \n" +
      "(orgainized as a list) \n")
print("**********************************************************************")

""" Import wanted module with every parent packages """
import DataFromManyPersons.Univariate.Continuous.Linear.S_Estimator as S_Estimator
from utils.ExtractSignal import ExtractSignalFromCSV
from utils.ExtractSignal import ExtractSignalFromMAT
from utils.Standardize import Standardize

""" -------------Import signals from a .csv file -----------------------"""

for videoName in VideoList:
    if not videoName.endswith(".csv") :
        continue
    print videoName

    filename = dataFolder + videoName
    print filename

    father = ExtractSignalFromCSV(filename, columns = ['slidedFather'])
    mother = ExtractSignalFromCSV(filename, columns = ['slidedMother'])
    child = ExtractSignalFromCSV(filename, columns = ['slidedChild'])
    frame_index = ExtractSignalFromCSV(filename, columns = ['frame_index'])
    video = ExtractSignalFromCSV(filename, columns = ['video'])

    fatherBOOL = True
    motherBOOL = True
    childBOOL = True
    participantsList = [father, mother, child]

    if (father['slidedFather'].isnull()).all():
# IF Only NA becomes False
        fatherBOOL = False

    if (mother['slidedMother'].isnull()).all():
# IF Only NA becomes False
        motherBOOL = False

    if (child['slidedChild'].isnull()).all():
        childBOOL = False

    participantsBOOLList = [fatherBOOL, motherBOOL, childBOOL]

    signals = []
    for i in range(3):
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
    for col in range(len(Signals)):
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
        """In this example, there is 3 participants father, mother, child,
         sometimes only one some participants are filmed """

# ---------------------- CREATION OF LISTS --------------------------"""
        SSIList_fa_mo = []
        SSIList_fa_mo_ch = []
        SSIList_fa_ch = []
        SSIList_fa_th = []
        SSIList_mo_ch = []

        for i in intervalList:
# We divide each data string in a shorter string of the length of numberOfFramesByInterval
            fatherInterval = father[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
            motherInterval = mother[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]
            childInterval = child[numberOfFramesByInterval*i:numberOfFramesByInterval*(i+1)]

# -------------------- CREATION OF COMBINAISONS --------------------------
            signals_fa_mo = [fatherInterval,motherInterval]
            signals_fa_ch = [fatherInterval,childInterval]
            signals_mo_ch = [motherInterval, childInterval]
            signals_fa_mo_ch = [fatherInterval, motherInterval, childInterval]

# -------------------------COMPUTATION CALL ---------------------------
#        print(video[0:NbOfInterval].reset_index())
            if fatherBOOL:
                if motherBOOL:
                    estimators_fa_mo = s_estimator.compute(*signals_fa_mo)
                    SSIList_fa_mo.append(estimators_fa_mo["SSI"])
                    if childBOOL:
                        estimators_fa_mo_ch  = s_estimator.compute(*signals_fa_mo_ch)
                        SSIList_fa_mo_ch.append(estimators_fa_mo_ch["SSI"])
                if childBOOL:
                    estimators_fa_ch = s_estimator.compute(*signals_fa_ch)
                    SSIList_fa_ch.append(estimators_fa_ch["SSI"])

            if motherBOOL:
                if childBOOL:
                    estimators_mo_ch  = s_estimator.compute(*signals_mo_ch)
                    SSIList_mo_ch.append(estimators_mo_ch["SSI"])

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
            time_min.append(float(i)*numberOfFramesByInterval/(25*60))

        SSIdf = pd.DataFrame({"Time_min" : time_min,
                            "Interval" : np.arange(1,len(intervalList)+1),
                            "video" : video})
        if len(SSIList_fa_ch) > 0:
            SSIdf_fa_ch = pd.DataFrame({"SSI_fa_ch" : SSIList_fa_ch})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_ch], axis=1)

        if len(SSIList_fa_mo) > 0:
            SSIdf_fa_mo = pd.DataFrame({"SSI_fa_mo" : SSIList_fa_mo})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo], axis=1)

        if len(SSIList_fa_mo_ch) > 0:
            SSIdf_fa_mo_ch = pd.DataFrame({"SSI_fa_mo_ch" : SSIList_fa_mo_ch})
            SSIdf = pd.concat([SSIdf, SSIdf_fa_mo_ch], axis=1)


        if len(SSIList_mo_ch) > 0:
            SSIdf_mo_ch = pd.DataFrame({"SSI_mo_ch" : SSIList_mo_ch})
            SSIdf = pd.concat([SSIdf, SSIdf_mo_ch], axis=1)

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
        SSIdf.to_csv(outputDirectory + videoName)

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
