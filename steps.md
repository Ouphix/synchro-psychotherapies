# Aim and Hypothesis
The aim of this project is to evaluate if it is possible to detect automatic signals of synchrony that could predict the outcomes of a familial psychotherapy. 

Here is the analysis of the F1044 subject, his familly (2 parents) and the therapist. Is there synchrony signals between himself, his parents and the therapist ? 

Is there synchrony signal between his parents and the therapist ? Could this synchrony signal predict outcomes of the psychotherapy ? See the full [pre-registration](https://github.com/Ouphix/synchro-psychotherapies/blob/master/projet%20presoutenance%20TG.pdf).

We used this data from a large european psychotherapy study since they come from almost real life practice of psychotherapy. This [INCANT](http://www.incant.eu/) study. study aimed to evaluate the efficacy of the MultiDimensioinal Family Therapy for cannabis use disorders in adolescents. 

# Nomenclature
F1044 is the name of the subject studied (called pa for patient).
He has a mother (mo) a father (fa) helped by a therapist (th).
When a variable is referring to several participants, it is organised in alphabetical order separated by underscores, eg. SSI_fa_mo refers to the synchrony index (SSI) between the father and the mother. SSI_mo_fa doesn't exist.
This familly had several consultations with the psychotherapist. Some of them were video recorded.
These videos are names with the name of the subject + an index letter. They can subdivised after that with numbers (eg F1044C).

# Steps
## Raw data
It is the videos in [AVI](https://en.wikipedia.org/wiki/Audio_Video_Interleave) format in the form F1044C1.avi, with a rate of 25 frames by second, from the 2 French centers of the [INCANT](http://www.incant.eu/) study.

This raw data is compared with [psychometric data](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/psychometry).

This data was made with public funds, however, the access of it was difficult, moreover it wasn't collected for this goal.

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) 

- In a lot of other domains of fundamental algorithm development, computer labs compete on public databases to improve the detection rates of some features for instance. This work are presented during [challenge sessions](http://sspnet.eu/avec2011/) in congresses.

- It would be better to make a specific database for this kind of automatic analyses to avoid changes of configuration of the room, the luminosity, the place of the different subjects, the number of subjects, the movement of the camera during recording.

## A. Motion extraction

### 1. Extracting frame from the beginning of the video
[Extract a frame](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Frames_extractor/Frames_extractor.py) with a python script from the beginning of the video to make a mask.

Here is an example of the father (eyes blurred to keep anonymity).

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Frames/SampleSimpleFrame.png =250x)

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) It was suggested to take a mean image of the video to be more precise instead of taking a video from the beginning.

![image](http://www.foxsymes.com.au/images/articles/_full/Beware.jpg =70x) Notice the date that was always masked after during the step 3.

### 2. Make a mask for each relevant part of each video with Paintbrush
Select a part of the video with each participant (father, mother, patient, therapist) with [paint brush](http://paintbrush.sourceforge.net/). Take only the upper part of the body to compare them since you can see only the upper part of the therapist.


Paint masking | Result |
------------ | -------------
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Frames/F1044C1paint.mov.avi.father.jpg =250x) | ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Frames/F1044C1.mov.avi.father.jpg =250x)

This operation is repeated for each participant on each video.

![image](http://www.foxsymes.com.au/images/articles/_full/Beware.jpg =70x) It is necessary to always use the same background color

Participants can move during the video (change their seats, leave the room). It would be preferable to anticipate it. Mean Motion history by minute can help us to detect big changes or disappearance of a participant.

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) 

- [Deep learning software](http://image-net.org/challenges/LSVRC/2014/) used for categorization/detection of people could make this process completely automatic.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/images/deeplearningsegmentation.jpg =250x)

- Tiny changes can't be always obvious. [Some softwares](https://lambda.qrilab.com/site/) can amplify a lot very tiny changes in specific frequencies that can't be seen normally with "naked eyes"

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/images/magnifyingMotion.png =250x)


### 3. Motion history extracted
It is extracted with the video and the mask
CSV file of the form "F1044C.VOB_res2.csv". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/rawData).

#### Headers :
- **frame** : number of the frame (original rate of 25 frames by second)
- **father** : motion history of the father frame by frame
- **mother**, : idem for mother
- **patient** : idem for patient
- **therapist** : idem for therapist
- **file** : name of the file in the form F1044C.VOB
- **NA** corresponding to absent subject or bad quality of first frames at the beginning or end of the videos

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) 

- It could be possible to extract [background](https://en.wikipedia.org/wiki/Background_subtraction) to improve the quality of the motion history. See for [instance BGS library](https://github.com/andrewssobral/bgslibrary/blob/master/README.md).

- It could be interesting to evaluate the trajectories of the people. Are they going toward the same direction or not. For that, the [Dense Trajectories Video Description](http://lear.inrialpes.fr/people/wang/dense_trajectories) could help.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/images/trajectories.png =250x)

#### 4. Motion history filtered with slindingInterval function

CSV file of the form "F1044C.VOB.slideddata.csv". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/filtered).

- **video** : name of the video (eg F1044C.VOB)
- **frame_index** : number of the frame (original rate of 25 frames by second)
- **slidedFather** : filtered motion history with the sliding motion history function making mean on 5 frames (2 frames before and after the index frame)
- **slidedMother** : idem for mother
- **slidedTherapist** : idem for therapist
- **slidedPatient** : idem for patient
- **NA** corresponding to absent subject

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) 

- It is possible to change the size of interval to change the ration signal/noise

![image](http://www.foxsymes.com.au/images/articles/_full/Beware.jpg =70x) 

- Bad quality of first frames at the beginning or end of the videos with NA were deleted to prepare the next script analysis.

- The number of frames is changed since it is necessary to get frames before and after the index.

#### 4. Computing synchrony score with this filtered motion data
The script [Call_S_Estimator.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Call_S_Estimator.py) takes this filtered motion data and compute a synchrony score for each association possible of two or more subjects.

It returns synchrony CSV files that can be found [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/SynchronyCSV)

- **Interval**
- **Time_min** 	
- **video** : name of the video (eg F1044C.VOB)
- **SSI_fa_mo** : synchrony index between the filtered motion history of the father and mother
- **SSI_fa_mo_th** 	: idem between father, mother and therapist
- **SSI_fa_th** : idem between father and therapist
- **SSI_mo_th** : idem between mother and therapist

There is not any NA in this file. Only the possible combinations are computed (eg there is not the patient (pa) in the video so, there isn't SSI_fa_pa signal neither any other combination with the patient).

## B. Speech extraction
### 1. Manually
It is possible to use the software Elan to annotate a video. You need to extract first the sound (with [Free Video Converter](http://www.freemake.com/free_video_converter/) for instance) to get a waveform and import the video and the waveform. 

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/images/elan_anot.jpg =250x)

Then you can annotate when someone is speaking. This process is very fastidious (1 week work for one hour video at the beginning and was gave up).

### 2. Automatically

![image](http://javierfreyria.com/blog/wp-content/uploads/2011/10/man-with-bulb-01-300x300.png =70x) Some softwares could be used to make this process easier. The [FASST software](http://bass-db.gforge.inria.fr/fasst/) get very good results to segment a music sample in very different instruments. However, different voices are too close to distinguish them easily automatically.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/images/fasst.jpg =250x)

