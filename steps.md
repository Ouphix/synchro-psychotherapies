# Synchrony in Psychotherapy, Data management, example with F1044 patient data

## Aim and Hypothesis
The aim of this project is to evaluate if it is possible to extract automatic signals of synchrony that could predict the outcomes of a familial psychotherapy. 

We began with a first database. We focused on the analysis of the F1044 subject, his family (father and mother) and the therapist. 

**Is there synchrony signals computed by [SyncPy module](https://github.com/syncpy) between himself, his parents and the therapist ? ** Could this synchrony signal predict outcomes of the psychotherapy ? See the full [pre-registration](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Reports/projet%20presoutenance.pdf).

This database come from a large european psychotherapy study. This [INCANT](http://www.incant.eu/) study aimed to evaluate the efficacy of the [Multi Dimensional Family Therapy](http://www.mdft.org/) (MDFT) for cannabis use disorders in adolescents. Some patients received traitment as usual and the others MDFT.

The main outcome was be cannabis consumption evaluated with the Timeline Follow-Back (TFLB) [questionnaire](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Data/CSV/Questionnaries/TimeLineFollowBack_2014Mar24%281%29.pdf).

## Summary figure
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/report/Extracting%20social%20signals%20%20from%20psychotherapy%20videos.png)

## Data structure
Data consist of 2 databases with each one videos and psychometric data.

### INCANT study
#### Study protocol
The Incant study aimed to evaluate the efficacy of MDFT a familial therapy with other treatments Treatments As Usual (TAU). Videos were recorded to check if the therapist was applying the psychotherapy that was assigned to each family.

The MDFT is based on several general principles likes topics that needs to be addressed,attitude of the therapist.

#### Videos
* We collected a 252.44GB database of 277 Videos, with a rate of 25 frames by second.
* They are encoded in [VOB](https://en.wikipedia.org/wiki/VOB) format.

#### Psychometric data
* It consist of 3 excel files with :
	* the Timeline Follow-Back [(TLFB)](http://link.springer.com/chapter/10.1007/978-1-4612-0357-5_3)
	* the Youth Self-Report syndrome structure [(YSR)](http://psycnet.apa.org/?&fa=main.doiLanding&doi=10.1037/0022-006X.75.5.729) 
	* the Child Behavior Checklist syndrome constructs [(CBCL)](http://www.ncbi.nlm.nih.gov/pubmed/10200736).

However, we didn't have any data dictionary with the definition of all variables and the precise questionnaires used to collect this information, the coding of Non Available data -99. We planned to meet the team that wasn't unfortunately available at that moment. A lot of videos were lost or not recorded. We couldn't know from this database which patient received MDFT or TAU. It was organized in a European level. We collected only the data from the 2 French centers.

#### Advantages and limits of this database
##### Experimental set-up
It is however not very defined in the articles. Consequently, it was difficult to contrast synchrony between two well defined periods. 
We could suggest to have a much more defined psychotherapy and even before studying a psychotherapy to study specific situations : open vs closed questions , 

### Monrado study
* We collected a database of 85.48 Gb of 40 videos, with a rate of 25 frames by second.
* They are encoded in a [MTS format](https://en.wikipedia.org/wiki/AVCHD) in a much better quality than the previous database.

#### Psychometric data
* It consist of one excel file with:
	* Identification number
	* Demographic information
	* Attachment style
	* TAS Score
	* STAIYA Score
	* BDI score

## Pilot study
F1044 subject had a lot of videos so we decided to make a pilot study with him to develop the analysis scripts. 
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/lengthMinute.jpeg).

It is quite reprensative since

We decided to make a pilot study on the most complete subject : F1044 since we have 18 videos with him. We can ask ourselves if this subject representative.The therapist is the second most representative concerning the number of patients and the first concerning the number of patient videos.The patient is a male like in 93 % of videos. The therapist is a female like in 99 % of videos. Two centers were included. This patient come from the main center.

We have all psychometrics evaluations (initial, 3m, 6m, 9m, 12m).Unfortunatelly, the first, second, 10th and 11th videos were lost. 

## Nomenclature
*F1044* is the name of the subject studied (called *patient*).
When referring to several persons, variables take the name of the shorter form *pa* for *patient*.

He has a *mother* (*mo*) a *father* (*fa*) helped by a *therapist* (*th*).
When a variable is referring to several participants, it is organised in alphabetical order separated by underscores, eg. *SSI_fa_mo* refers to the synchrony index (*SSI*) between the *father* and the *mother*. *SSI_mo_fa* doesn't exist.

This familly had several consultations with the psychotherapist (*therapist*). Some of them were video recorded.
These videos are names with the name of the subject + an index letter. They can subdivised after that with numbers (eg *F1044C*).

## Softwares used
* Git
	* [GitHub website](https://github.com/Ouphix/synchro-psychotherapies)
* Excel
* [R](https://www.cran.r-project.org/)
	* [xlsx package](https://cran.r-project.org/web/packages/xlsx/index.html)
* [Python](https://www.python.org/)
	* [opencv](http://opencv.org/)
	* panda
	* matplotlib
	* [syncpy](https://github.com/syncpy/SyncPy)
	* [FFMPEG](https://ffmpeg.org/)
* C ++
* Paintbrush 2
* Quicktime
* VLC
* Elan
* Markdown

## Steps
### Description of the database
#### Video Configurations
##### Spatial organisation
In the first center, psychotherapy sessions consisted of filmed familial psychotherapies with 2 to 5 peoples organized in a circle.
Two participants of the psychotherapy were filmed from the front. Another subject is filmed from the other side. Its video is embedded in a window. We can notice the date displayed on the video. Sometimes, there is an overlap of different subject in the same place.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/SampleSimpleFrame.png =350x)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/DifferentConfigurations.jpeg)

In this barplot of the mean motion history for each subject for each video, we can see that the configurations of the participants involved for the F1044 subject can be very different between videos. There is between 2 and 3 participants. There is never the 4 participants involved. Sometimes, we don't have any information from the therapist because she isn't filmed. The patient is not very present in the therapy (compliance problem).

When we sum up the data we get, we can see that the mother and the therapist are the most present participants.
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/AvailableData.jpeg)

#### Psychometric data
Files were collected in [xls](https://en.wikipedia.org/wiki/Microsoft_Excel) format.
They were imported via the [XLSToCSVConvertor.R](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Scripts/XLSToCSVConvertor.R) R script.
It returns a dataINCANT.csv csv file and a [dataCannabis.csv](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Data/CSV/psychometry/dataCannabis.csv) file. The evolutions of this scores are plotted [here](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Reports/psychomet.pdf). 

##### Time organization
Video length could were very different because it was necessary to reorganize them. 

The configurations could change (eg patient-mother-therapist then mother-therapist) during the psychotherapy, a phone was used to communicate between the main psychotherapist and the supervisor. The participants made some pauses or the same video was used for different patient.

Hence, it was necessary to cut the videos with [Quicktime](https://en.wikipedia.org/wiki/QuickTime) software.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/lengthMinute.jpeg)


### Raw data
The first step was to extract frames with the [Frames_extractor.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Scripts/Frames_extractor) python script made by Jonathan with [FFMPEG](https://ffmpeg.org/).


Idea  |  |
------ | ------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png) | In a lot of other domains of fundamental algorithm development, computer labs compete on public databases to improve the detection rates of some features for instance. This work are presented during [challenge sessions](http://sspnet.eu/avec2011/) in congresses. However, there is a problem with confidentiality when we deal with psychotherapy videos.
  | It would be better to make a specific database for this kind of automatic analyses to avoid changes of configuration of the room, the luminosity, the place of the different subjects, the number of subjects, the movement of the camera during recording. |


### A. Motion extraction

#### 1. Extracting frame from the beginning of the video
Extract a frame with [*Frames_extractor.py*
](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Frames_extractor/Frames_extractor.py) with a [python](https://www.python.org/) script from the beginning of the video to make a mask. This script was developed by Jonathan Aigrain with [Open CV](http://opencv.org/).


Here is an example of the father (eyes blurred to keep anonymity).

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/SampleSimpleFrame.png =250x)


Idea  |  |
------ | ------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png =130x) | It was suggested to take a mean image of the video to be more precise instead of taking a video from the beginning.|
**Beware** |  |
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/Beware.jpg =70x) | Notice the date that was always masked after during the step 2.
| We can change the value of the [median filter](https://en.wikipedia.org/wiki/Median_filter).

#### 2. Make a mask for each relevant part of each video with Paintbrush
Select a part of the video with each participant (father, mother, patient, therapist) with [*Paintbrush*](http://paintbrush.sourceforge.net/). Take only the upper part of the body to compare them since you can see only the upper part of the therapist.


Paint masking | Result |
------------ | -------------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/F1044C1paint.mov.avi.father.jpg =250x) | ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/F1044C1.mov.avi.father.jpg =250x)

This operation is repeated for each participant on each video.

Beware  |  |
:------: | ------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/Beware.jpg =70x) | It is necessary to always use the same background color, for instance [RGB green](http://rapidtables.com/web/color/RGB_Color.htm). (0,255,0) |
| Participants can move during the video (change their seats, leave the room). It would be preferable to anticipate it. Camera is moving sometimes too. Mean Motion history by minute can help us to detect big changes or disappearance of a participant.|
| Participants are labelled in the mask name (eg *F1044C1.avi.father.jpg*)
**Idea** |  |
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png =300x) | [Deep learning software](http://image-net.org/challenges/LSVRC/2014/) or machine learning used for categorization/detection of people could make this process completely automatic. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/deeplearningsegmentation.jpg =250x)

#### 3. Motion history extracted
The VOB videos were converted in [AVI](https://en.wikipedia.org/wiki/Audio_Video_Interleave) format in the form *F1044C1.avi*.

It is extracted with the video and the mask with a [C++](https://en.wikipedia.org/wiki/C%2B%2B) script. It returns
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file of the form "*F1044C.VOB_res2.csv*". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/INCANT/Data/CSV/MotionHistory/raw).

##### Headers :
- **frame** : number of the frame (original rate of 25 frames by second)
- **father** : motion history of the father frame by frame. It ranges from 0 (same frame than the previous frame, no movement) to 1 (every pixel change).
- **mother**, : idem for mother
- **patient** : idem for patient
- **therapist** : idem for therapist
- **file** : name of the file in the form *F1044C.VOB*

- **NA** : (Non available) corresponding to absent subjects (NA column) or bad quality of frames at the beginning or end of the videos making impossible extraction of motion history for any participant (NA line). After a problem of encoding, from .VOB, to .mov (video format exported from quicktime when cut are made) and then to AVI, there is a problem of encoding and the length of the video is not well recognized and NA lines are generated that correspond to nothing.

If we plot (in histograms and box plots) this taw data (1st column), we notice that the distribution is not normal at all. Very small motion history values are over represented and and bigger motion history are much more rare with a very long tail.

To normalize the distribution to compute synchrony scores on it, we made the natural logarithm. It produces negative numbers. SyncPy can't compute negatives scores, they are so shifted to positives values with an arbitrary value of 20 to avoid to keep extreme negative values.

Values equal to 0 can't be loged. They generate a -Inf value. These values are set to NA. We lose the information of no movement at all. If we give a arbitrary value to this data (eg, the minimum value, they are over represented).

This normalized log data is shown on column 2.


Raw Motion history | Natural Log Motion history 
------------ | -------
***Father ***|
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/MotionHisoryFatherRaw.jpeg) | ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/HistMotionHistoryfather.jpeg)
***All participants ***|
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/MotionHistoryBoxPlots.jpeg)  | ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/LogMotionHistoryBoxplots.jpeg)

If we check all participants, we can see that the father and the mother motion history distribution is very similar. However, the therapist, which is always in a small window of the video, as a very different distribution. We have less signal on it. In some videos the patient is in this window, it explains, it intermediates position.


Idea |  |
---- | ----
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png =300x) | - It could be possible to extract [background](https://en.wikipedia.org/wiki/Background_subtraction) to improve the quality of the motion history. See for instance [backgroundExtractor.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Scripts/backgroundExtractor.py) with openCV  [BGS library](https://github.com/andrewssobral/bgslibrary/blob/master/README.md). 
 | - It could be interesting to evaluate the trajectories of the people. If they are going toward the same direction or not. For that, the [optic flow modules of open CV](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html) or the [Dense Trajectories Video Description](http://lear.inrialpes.fr/people/wang/dense_trajectories) could help. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/trajectories.png =250x)
| Tiny changes can't be always obvious. [Some softwares](https://lambda.qrilab.com/site/) can amplify a lot very tiny changes in specific frequencies that can't be seen normally with naked eyes. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/magnifyingMotion.png =250x)


#### 4. Motion history filtered with slindingInterval function
Motion history raw data is filters with a [R](https://www.cran.r-project.org/) function on [Rmarkdown script analysis](https://github.com/Ouphix/synchro-psychotherapies/blob/master/SyncPsycho.Rmd). It generates CSV file of the form "F1044C.VOB.slideddata.csv". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/filtered).

Sliding interval (raw Data) | Sliding interval (log Data)
--------------------------- | ---------------------------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/MeanMotionHistory%28Sliding5framesinterval_raw_data%29on%20F1044C1_first_10_seconds.jpeg)|![Content Cell](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/plots/MeanMotionHistory%28Sliding5framesinterval_log_data%29on%20F1044C1_first_10_seconds.jpeg) 


##### Headers :

- **video** : name of the video (eg F1044C.VOB)
- **frame_index** : number of the frame (original rate of 25 frames by second)
- **slidedFather** : filtered motion history with the sliding motion history function making mean on 5 frames (2 frames before and after the index frame). It ranges from 0 (same frame than the previous frame, no movement) to 1 (every pixel change).
- **slidedMother** : idem for mother
- **slidedTherapist** : idem for therapist
- **slidedPatient** : idem for patient
- **NA** : corresponding to absent subject

Idea |  |
----- | -----
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png =150x) | It is possible to change the size of interval to change the ration signal/noise|
**Beware** |  |
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/Beware.jpg =70x) | Bad quality of first frames at the beginning or end of the videos with NA were deleted to prepare the next script analysis.
| The number of frames is changed since it is necessary to get frames before and after the index.

##### 4. Computing synchrony score with this filtered motion data
Amplitude (difference between min and max) and baseline levels (min) are not relevant to compute synchrony.

The script in [Python](https://www.python.org/), [Call_S_Estimator.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Call_S_Estimator.py) takes this filtered motion data and compute a synchrony score for each association possible of two or more subjects.

Download and install [SyncPy](https://github.com/syncpy/SyncPy).

The script [Call_S_Estimator.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Call_S_Estimator.py) must be installed in Syncpy installation in examples folder. Create a folder *SynchronyCSV* in this folder.

**You need to specify, **

- the folder where you put your data (eg dataFolder = '/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/filtered/') 

- the list of videos you want to analyze, (eg VideoList = ["F1044C.VOB", "F1044D1.VOB", "F1044D2.VOB", "F1044E.VOB", "F1044F.VOB", "F1044G.VOB", "F1044H.VOB", "F1044I.VOB", "F1044L.VOB", "F1044M1.VOB", "F1044M2.VOB", "F1044N.VOB", "F1044O.VOB", "F1044P.VOB", "F1044Q.VOB", "F1044R1.VOB", "F1044R2.VOB"])

- the number of frames used in an interval to compute synchrony, Nota bene, there are 25 frames by second. (eg. numberOfFramesByInterval = 25*10)

This process is relatively long and can take several minutes, especially with short intervals.

It returns synchrony CSV files that can be found [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/SynchronyCSV).

##### Headers :

- **Interval**
- **Time_min** 	
- **video** : name of the video (eg F1044C.VOB)
- **SSI_fa_mo** : synchrony index between the filtered motion history of the *father* and *mother*. It ranges from 0 (no synchrony at al, not any relationship between the different participants of the score) to 1 (complete synchrony, the different elements move a lot at the same moment or don't move at all at the same moment).
- **SSI_fa_mo_th** 	: idem between *father*, *mother* and *therapist*
- **SSI_fa_th** : idem between *father* and *therapist*
- **SSI_mo_th** : idem between *mother* and *therapist*

There is not any NA in this file. Only the possible combinations are computed (eg there is not the *patient* (*pa*) in the video so, there isn't *SSI_fa_pa* signal neither any other combination with the patient).

### B. Speech extraction
#### 1. Manually
It is possible to use the software Elan to annotate a video. You need to extract first the sound (with [Free Video Converter](http://www.freemake.com/free_video_converter/) for instance) to get a waveform and import the video and the waveform. 

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/elan_anot.jpg =250x)

Then you can annotate when someone is speaking. This process is very fastidious (1 week work for one hour video at the beginning and so was gave up).

#### 2. Automatically

Idea |  |
------ | ------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/man-with-bulb-01-300x300.png =400x) | Some softwares could be used to make this process easier. The [FASST software](http://bass-db.gforge.inria.fr/fasst/) get very good results to segment a music sample in very different instruments. However, different voices are too close to distinguish them easily automatically. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/fasst.jpg =250x)

We can see that the evolution of cannabis use by F1044 is not straightforward. It is quite high at the beginning, decreases and then increases. Consequently, we decided to select 4 subjects with a clear decrease of cannabis consumption.

* F1002, patient, 3 videos
* F1073, patient, 2 videos
* F1069, patiente, 4 videos
* F1101, patient, 3 videos

All of them with the same therapist Mrs Bastard

