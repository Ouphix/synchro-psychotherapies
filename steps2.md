# How synchrony detected from videos could predict the quality of a therapeutic or parent relationship

### Author: Thomas GARGOT

### Project website : [bit.ly/syncpsy](http://bit.ly/syncpsy)

Synchrony articles before

[TOC]

## Abstract
#### Introduction and motivations
Psychotherapy is an important part of treatment of mental disorders alone or complementary with pharmacotherapy. Some techniques are now widely evidence-based and very cost effective (Layard & Clark, 2014).

Most of the studies are indirectly based on patient reported outcomes or problematic behaviors evaluated before and after the psychotherapy. Unfortunately, studies hardly control what is actually happening during psychotherapy, especially the unspecific aspects like the interaction between the patient and the therapist that is a predictor of the psychotherapy efficacy. Consequently, it is difficult to make precise links between theory and practice, control its application and understand which of its ingredients are the most important.

Here we suggest a research framework to extract automatically social signals from psychotherapy videos and tested it on two databases. We focused on the extraction of synchrony of the motor signal since it was considered as a predictor of psychotherapy outcome in an earlier study (Ramseyer, 2011) and a relevant signal for the study of mother-child interactions. We adapted a python software in open source [SyncPy](https://github.com/syncpy) (Varni, Avril, Usta, & Chetouani, 2015) to compute this synchrony.

#### International Cannabis Need of Treatment (INCANT) study Database

We began with the International Cannabis Need of Treatment (INCANT) study database from France. This [INCANT](http://www.incant.eu/) study aimed to evaluate the efficacy of the [Multi Dimensional Family Therapy](http://www.mdft.org/) (MDFT) for cannabis use disorders in adolescents.

For a pilot study, we focused on the analysis of the interaction within a single family (F1044) and the therapist. Unfortunately, we couldn't answer to this question since the signal extracted from this videos with too many technicall difficulties. Furthermore, it was difficult to categorize easily the patients in good and bad responders and to detect specific periods of the psychotherapy with particular very high and low bad relationship quality. Finally, it was difficult to compare synchrony at different moments since the spatial organization of the participants could be very different.

This database showed the challenge to work on naturallistic psychotherapy videos.

#### Monrado Database

Consequently, we switched to the Monrado database, an other video database, with a better video quality and experimental design. It evaluates the difference of behavior in a situation of conflict versus no-conflict between parents and adolescent. The main psychometric data in this database were attachment scores, i.e. a evaluation of the relationship of the subject with other people. We can begin to draw some preliminary conclusions about using synchrony in order to classify the relationship quality of these videos.

#### Conclusion

This work led to the development of R scripts to manipulate motion history, filter it ; adaptation of Python module of SyncPy. Too our knowledge, these are the first scripts that are are published in open access to enable easy replication and further developments. We draw some recommendation to get psychotherapy material of better quality in terms of video and sound recording and psychotherapy techniques and outcomes. Furthermore, we suggest some modules that could be added to extract more social signals from other modalities and precisions.  With our method, we can began to draw some preliminary conclusions about using synchrony in order to classify the relationship quality of these videos.

See the full [pre-registration](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Reports/projet%20presoutenance.pdf).

## Poster
![image](https://github.com/Ouphix/synchro-psychotherapies/raw/master/Monrado/Data/images/report/ECNPPoster.jpg)

## Originality declaration
This study is the second study to evaluate the relevance of synchrony as marker of the quality of psychotherapy after the study of [Ramseyer et Tschacher, 2011](http://psycnet.apa.org/journals/ccp/79/3/284/). It is the first to study it in families, which both different configurations and theorical frameworks (S Estimator technique). The package used for synchrony was developed by the engineers of the team and it was the first time that it was used in real world data. The input of psychiatrists and psychotherapists helped to understand the kind of relevant signals that could be extracted from psychotherapy videos. 

It is the first study to use an open science approach among the 3 studies ([Ramseyer et Tschacher, 2011](http://psycnet.apa.org/journals/ccp/79/3/284/); [Orsucci et al, 2016](https://www.researchgate.net/publication/299568125_Synchronization_Analysis_of_Language_and_Physiology_in_Human_Dyads)) that used synchrony as predictor of quality of relations since raw data extracted from videos, analysis reports and preregistration are published on the [website project](https://github.com/Ouphix/synchro-psychotherapies/).

## Collaborations

In alphabetical order : 

| Name                    | Function                                 |
| ----------------------- | ---------------------------------------- |
| Jonathan Aigrain        | Phd Student in social signal processing. He did scripts to extract frames from videos, to extract Motion History from videos frame by frame, knowledges in Python (OpenCV) |
| Nicolas Bodeau          | Bio-statistician and informatician in ISIR and La Pitié, he supervised me for R and statistical analysis |
| Mohammed Chetouani      | Prof in social signal processing, supervised the project, and the SyncPy library |
| David Cohen             | Prof of Psychiatry, original idea, supervised the project, revision of the final document |
| Catherine Saint Georges | Psychiatrist, knowledge in interpreting synchrony scores in psychiatry, helped with first speech annotation with Elan |
| David Reversat          | Computer engineer, installation of SyncPy and associated modules, debugged SyncPy |
| Michel Spodenkiewicz    | Psychiatrist, collected the databases from other teams (videos from INCANT and Monrado studies), direct supervision, revision of the final document |
| Giovanna Varni          | Post-doc researcher Social signal processing, Development of the SyncPy library, supervised me for Python, revision of the final document |

The Monrado (Dr Coady Vulliez, Mrs Monika Szymanska) and Incant (Dr Phan, Mrs Bastard) teams recruited subjects and provided psychometric data.

Personnaly, I helped to define and operationalize the scientific question from the general idea, the tools and databases available. I did the bibliography based on the work of the team and Ramseyer team articles. I cleaned and prepared the databases. I adapted the Python and R script to make the extraction of the signal and performed the analysis. I did the figures and diagrams to explain the process of the method and describe the results.

## Theorical background

### Why and How evaluate psychotherapies?
Psychotherapy evaluation is quite difficult since it must evaluate the basics of human to human relationship. A lot of theories developed in this field (hypnosis, psychoanalytical, cognitive-behaviorist, systemic...) with very different histories, practices and levels of evaluation. Contrary to other parts of medicine, psychotherapy and consequently psychiatry remains organized as schools which hardly interact each others. A lot of choices are done relative to the theoretical orientation of an hospital or a ward and not based on the best evidence based information which if often very limited in this field. Consequently, there isn't any consensual framework between psychotherapies.

Due to its history of being based upon scientific bases and in a scientific process of operationalize precisely the targets, Cognitive and Behavioral Therapies (CBT) are the most evidence based ([Canceil et al., 2004](http://lara.inist.fr/handle/2332/1323) ;[ Layard & Clark, 2014]((https://books.google.fr/books?hl=fr&lr=&id=tGL5AgAAQBAJ&oi=fnd&pg=PT7&dq=Layard+%26+Clark,+2014&ots=He32vXEgKA&sig=IlWpAGmhaav2rKIZJLq2EtWPL94#v=onepage&q=Layard%20%26%20Clark%2C%202014&f=false)) with a lack of experimental work in other schools of psychotherapy.

Paradoxically, psychotherapies methods seems to be the most efficient treatment in medicine with a very low number needed to treat, i.e. it is necessary to treat only a few patient (around two) to have a remission impact on a group of patient (Wampold cited by Briffault, 2009 ; [Layard & Clark, 2014](https://books.google.fr/books?hl=fr&lr=&id=tGL5AgAAQBAJ&oi=fnd&pg=PT7&dq=Layard+%26+Clark,+2014&ots=He32vXEgKA&sig=IlWpAGmhaav2rKIZJLq2EtWPL94#v=onepage&q=Layard%20%26%20Clark%2C%202014&f=false)). This could be striking to say that we are using useful and efficient treatments without knowing how they work. It is not an exception in medicine. Contrary to the classical biological and pathophysiological point of view, with Evidence Based Medicine (EBM), one don't need to know the mechanism of action of a treatment to prove that it is efficient. We only need to use experimental method (EBM approach) to compare it with an other treatment like a classical treatment or a placebo. For instance, one of the most widely used treatment paracetamol is a widely used analgesic and the proof of its efficacy was widely done. Unfortunately, in 2016, we can't say exactly how it is working on the body ([Bonnefont, Courade, Alloui, & Eschalier, 2002](http://europepmc.org/abstract/med/14758785)).

Unfortunately, good psychotherapy is costly because it takes times and requires well trained therapist. Contrary to pills, psychotherapy isn't reimbursed in many countries. Public services hardly offer best practice of psychotherapy because of a lack of training and time. 

Furthermore, it is difficult to operationalize precisely what a psychotherapist does during a psychotherapy. Even the more operationalized psychotherapy as relaxation techniques, CBT deals with the particularity of each patient, its motivation, its context and don't have a priori a very precise roadmap. Despite these theoretical and evidence debates, there is almost a consensus that the relationship between the patient and the therapist is an important predictor of the efficacy of the psychotherapy. Establishing this therapeutic alliance is a very important part of the efficacy of psychotherapy ([Horvath & Dianne, 1991](http://psycnet.apa.org/journals/cou/38/2/139/) ; [Martin, Garske, & Katherine, 2000](http://psycnet.apa.org/journals/ccp/68/3/438/) ; Cungi & Cottraux, 2006 ; [Tschacher, Haken, & Kyselo, 2015](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4404724/)). Even it is difficult to operationalize, some psychometric tools were developed like the Working Alliance Inventory (WAI) questionnaire ([Corbière, Bisson, Lauzon, & Ricard, 2006](http://onlinelibrary.wiley.com/doi/10.1002/mpr.27/abstract)). This led to the Dodo theory. It states, like the judgment made by the Dodo bird after a race in the Alice and the Wonderland book, that all participants are equals. It means than nothing technical could differentiate a psychotherapy versus an other one, only the patient-therapist relationship would be important. This consensus is challenged by some behaviorist (CBT) that state that this determinant is only important when psychotherapist are not well trained and in poorly designed studies ([Layard & Clark, 2014](https://books.google.fr/books?hl=fr&lr=&id=tGL5AgAAQBAJ&oi=fnd&pg=PT7&dq=Layard+%26+Clark,+2014&ots=He32vXEgKA&sig=IlWpAGmhaav2rKIZJLq2EtWPL94#v=onepage&q=Layard%20%26%20Clark%2C%202014&f=false)).

Therapeutic alliance is a first step before any other specific technique (Cungi & Cottraux, 2006). This process was widely studied in the first psychotherapies like hypnosis. In a good therapeutic alliance, the contact is warm, authentic, collaborative. There is a lot of empathy, ie the therapist understand the point of view and the representation of his patient, shares it (contrary to apathy) while keeping in mind that he is not in the same situation as his patient and without being struggled by too much emotions (contrary to sympathy). One of the best operationalized and Evidence based kind of psychotherapy which focus on therapeutic alliance is motivational interviewing (Miller & Rollnick, 2013) which if much used in first steps CBT or psychoeducation. It can be the essential part of a work with addict patient or patients with addictions problems. The goal of motivational interviewing is to increase change discourse by stimulating it by some techniques:

* open question (like how are you today ?) in order to let the patient a wide range of possible answers contrary to close questions, specifically with Yes/no answers (like did you slept well yesterday night ?)
* Rephrasing what the patient is saying (eg If I understand well, you told me that..., isn't it ?) especially the change discourse.
* Summing up, the discourse of change of the patient (eg you told me that your consumption of cannabis was a problem because your motivation was much lower)
* Avoiding direct advices but stimulating it by questions
* Accept the ambivalence in a change, the patient need to resolve it on his own without being pressured by the therapist
* Avoid judgement
* Searching for small and positive steps toward change
* Reinforcing any positive step
* Defining and raising the values of the patient and not the therapist values
* Giving advices only when it is requested by the patient

We can see that even this very operationalized psychotherapy lets place for a lot of improvisation and adaptation to a precise situation and can not be standardized. Consequently, it needs a lot of practice and training beyond the theoretical knowledge. A lot of reflexes (like giving advices) need to be unlearned, that takes time. However, it is quite difficult to give precise feedback (supervision) without being involved directly in the therapy with the therapist. In complex settings like familial psychotherapies, the therapist can be directly supervised by a colleague behind a two-way mirror.

One way to improve learning process and evaluation of psychotherapy in practice is their annotation. After filming psychotherapy, it is possible to evaluate what is exactly happening during this process. Some evaluation tools were developed like the MITI ([Moyers, Manuel, & Ernst, 2014](http://www.motivationalinterviewing.org/sites/default/files/miti_4.1_december_2014.pdf)) for the motivational interviewing.  Softwares like [Elan](https://tla.mpi.nl/tools/tla-tools/elan/) can be very useful for that and enable to annotate several modalities at the same time. However, it can be very difficult and tedious.

In many parts of medicine, we don't directly evaluate the desired outcome of a therapy (like the mortality) because it happens too late. Consequently, intermediate markers help the physician to choose the best treatment. For instance, we can evaluate the efficacy of an anti diabetic on blood sugar mean reflected by Hb1Ac. This avoid to wait several years to check if the treatment is efficient or not (which can be evaluated only by disability created by diabetes or mortality). Consequently, it is very convenient if we can get an automatic signal of this therapeutic alliance, we could get an intermediate marker of the efficacy of the psychotherapy which unfortunatelly doesn't exist at the moment.

Fortunately, it is possible to evaluate the efficacy of a psychotherapy via two direct means. The first one are the direct outcomes of psychotherapy with behavior or consumptions (like number of cannabis joint consumed or number of panic attacks). This kind of easily reported outcomes are more the exception than the norm. However, it is not possible in all mental disorders. The second one is psychometric data like Beck Depression Inventory (BDI) ([Beck, Steer, & Carbin, 1988](http://www.sciencedirect.com/science/article/pii/0272735888900505)) for depression, or State-trait anxiety inventory (STAI) (Spielberger, 1970) were developed to evaluate the state of different pathological characteristics. These scales can be filled by the therapist or the patient directly. However, it is quite time consuming and not much done in practice outside research or CBT training.  

To sum up, we can say that there are a lot of different kinds of psychotherapies. Some of them are largely evidence based and operationalized which can help for research. It is difficult and costly to train psychotherapist. Psychotherapies are efficient but it is hard to affirm exactly why.  There are ways to evaluate its efficacy but they are not used since they are time consuming. There aren't many easy and quick ways to evaluate them.

### Potential role of cognitive sciences in improvement of psychotherapies

#### Learning theory
Learning theories were developed by Skinner and Pavlov. They state that during a learning period, there are association between different stimuli. For instance, a behavior that will be positively reinforced will be repeated. A situation that is painful will be avoided. They are widely used in most recent cognitive studies in the term reinforcement learning. They are largely applied in cognitives sciences especially in modeling decisions process and understanding brain activity. In psychotherapy, they are widely applied in CBT approach to understand maintenance of a pathological process. Often a patient is being reinforced by avoiding a short term pain but this leads to avoidance of the situation and keep abnormal and painful emotions and cognitives schemas. The role of the therapist is to help the patient to became aware of this process during the functional analysis and to suggest him to change to healthier behavior by using new reinforcers. 

#### Cognitive neuroscience and education

With the progress of neuroscience there is a a growing evidence toward some techniques to improve curiosity, attention, motivation of students ([Dehaene, 2014](http://www.college-de-france.fr/site/stanislas-dehaene/course-2014-2015.htm)). A new field of research neuroeducation is developping, a lot of these work could be applied in psychotherapy too.  

#### Cognitive dissonance and engagement theory
Even if it wasn't described by the creators of the motivational interviewing, we can see that this process is close to the engagement theory, and engaging communication developed by Beauvois and Joule (Joule & Beauvois, 2010) after the work on cognitive dissonance by Festinger ([Festinger & Carlsmith, 1959](http://psychclassics.yorku.ca/Festinger/)). This theory was developed and validated in control people without any mental disorders but could be very interesting in psychiatric patients and in psychiatry settings (Fond et al, 2014). We can see consequently that we could use some very defined experimental settings like in cognitive and social psychology to improve our understanding of the process of psychotherapy. This is what will be used in the Monrado study to compare two situation without any conflit and with a conflict.

Cognitive dissonance theory is a counter-intuitive theory but very developed and replicated that deals with how we react to cognitive conflict and how we often rationalize our behavior in several situations.
Festinger asked participants to make a dull task. When the participant is willingly making it for free, he feels a conflict between thoughts like "I am a clever person free to make something" and his behavior "I am making something completely dull and useless". This conflict is difficult to handle. The subject is in a situation of cognitive dissonance. In this situation, he resolves his dissonance by changing his thoughts "this task is not so dull but rather interesting". However, in exactly the same situation, when the participants are paid, the effect disappear, there isn't anymore conflict. The subject still find the task completely dull as it is ([Festinger & Carlsmith, 1959]((http://psychclassics.yorku.ca/Festinger)). After this classical paradigm, several explanations were developed especially by Beauvois, Joule who evaluated some other paradigms consistent with this theory (Beauvois & Joule, 1987, 1996, 2010). The Foot in the door technique (how to change a behavioral by very small steps), the "You are free" paradigm, the "labelling technique" (it seems your health is very important for you), "touch technique" were widely evaluated without much publicity inside psychotherapy field even if a lot of their approach can be consistent with Motivational Interview. Consequently, a behavior can be much more explained by a context and by the previous behaviors of the subject than on the expected outcome as expected by the reinforcement learning theory. 

#### Bandura 
Bandura challenged the reinforcement theory too by demonstrating that imitation was a major process of learning. In the Dodo doll experiment [(Bandura et al, 1961](http://psychclassics.yorku.ca/Bandura/bobo.htm)), he showed that the behaviors of children could be predicated by the models of adults they saw just before. This process is widely used in psychotherapy where the therapist can play the role of model in role play or exposure for instance which the patient can imitate.

#### Mirror neurons, mirroring and empathy
Mirror neurons were discovered by Rizzolatti ([Rizzolatti & Craighero, 2004](http://www.annualreviews.org/doi/abs/10.1146/annurev.neuro.27.070203.144230)). When a monkey seizes an object, specific neurons of this task (in this receptor field) fire. The same neurons fire when this monkey see an other one making the same action. Consequently, it seems that there is a system in which the monkey simulates the outside world. This system is still activated when he really performs the task.
Lakin showed that there was a lot of automatic imitation in humans and this culd have a very important role in human relationships [(Lakin et al, 2003)](http://link.springer.com/article/10.1023/A:1025389814290). Neal and Chartrand showed that the mimicry of facial expression could be very useful in the process of empathy. They blocked expression of emotion with injection of Botox in subjects faces. In this condition, emotion perceptions of the subjects were impaired ([Neal & Chartrand, 2011](http://spp.sagepub.com/content/2/6/673)). Consequently, we can say the perception can't be separated with action but both of them interact a lot in a very strong loop.
Beyond that, some researchers like Iacoboni stated that the system of minor neurons could be involved in mirroring and imitation, a system that could be involved in empathy [(Iacoboni, 2009)](http://www.annualreviews.org/doi/abs/10.1146/annurev.psych.60.110707.163604). However, this role of mirror neurons is not consensual.


### Theorical advantages and pitfalls of synchrony studies
"Synchrony refers to individuals’ temporal coordination during social interactions" ([Delaerche et al, 2012](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6322986&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6322986)).. However, definition of synchronies are very numerous. There is a possibility to switch from the social world to a mathematical definition but since the point of view is different, it doesn't always refer to the same thing. Interdependence of dyadic partners’ behaviors was described by many terms in the literature (mimicry, social resonance, coordination, synchrony, attunement, chameleon effect, etc.) ([Delaerche et al, 2012](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6322986&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6322986)).

Synchrony is related to the adaptation of one individual to the rhythms and movements of the interaction partner. For Delaherche, "synchrony is the dynamic and reciprocal adaptation of the temporal structure of behaviors between interactive partners" ([Delaerche et al, 2012](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6322986&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6322986)). It can be unimodal (eg. speech-speech) or multimodal (eg. speech-motor, someone answering to a sentence by a sign of the head).

Synchrony could an important element of therapeutic relationship. This could be measured in any kind of psychotherapy without theorical a priori. It is is social signal but brain correlates were found [(Dumas, Nadel, Soussignan,Martinerie, & Garnero, 2010](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0012166)) and hormonals correlates too [(Weisman et al., 2013)](http://rsbl.royalsocietypublishing.org/content/9/6/20130828).										

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/report/multilevel.png)
*From Human communication dynamics presentation, D. Cohen*

It was previously studied in psychotherapeutic settings by other teams. Ramseyer et al. investigated non-verbal synchrony between patient and therapist during psychotherapy sessions. They showed that non-verbal synchrony was associated with therapy outcome and patient’s view of the therapy process [(Ramseyer & Tschacher, 2011)](http://psycnet.apa.org/journals/ccp/79/3/284/). They found that synchrony was increased in sessions that were considered by patient as sessions with high relationship quality and in patients experiencing high self-efficacy. Furthermore, higher non-verbal synchrony predicted psychotherapies with higher symptom reduction.

However, in these settings, there could be only one patient and one therapist. Furthermore, it is not possible to replicate directly this study since the technical aspects are not described and programs codes are not shared.

Some recordings are used in diagnostic phase where lack of coordination in non-verbal behaviors was found as a risk of recurrence of depression [(Bouhuys & Sam, 2000)](http://www.sciencedirect.com/science/article/pii/S0165032799000932).

Independently of the psychotherapy theory and framework, it seems that synchrony could be used in very different settings and could reflect the therapeutic alliance. In the future, we can imagine that synchrony score could be extracted automatically in different modalities (synchrony of speech, motion history, smiles, expressed emotions). That would give a feedback about the process of the psychotherapy that will be more objective and less time consuming than filling a psychometric questionnaire. 

### Open science, Open data, Confidentiality 
It was quite difficult at the beginning to replicate the studies that were done by other teams and to find these two databases that could be relevant for this goal because of quality of the recording and quality of psychometric data collected. Fortunatelly, after we had our own scripts and procedure for Incant database, it was very easy to replicate the analysis for Monrado database. 

To avoid this lost of time, and to improve validity, replicability and improvements of our work. we tried to develop an open science approach. The synchrony computation software SyncPy developped by the team G. Varni and M. Avril was published on [open source on GitHub](https://github.com/syncpy/SyncPy). We decided to continue this approach to improve accessibility, transparency of this work to help future improvements. We published all our scripts, reports and report on [GitHub too](https://github.com/Ouphix/synchro-psychotherapies). You can especially follow the [Rmarkdown pdf report of the Monrado study](https://github.com/Ouphix/synchro-psychotherapies/raw/master/Monrado/Reports/SyncPsychoMonrado.pdf) which is very detailed and commented with the data dictionnaries of the files.  The raw videos and precise psychometric data unfortunatelly couldn't be published because of medical confidential issues.

The idea of this project is to be a first step toward a better understanding of therapeutic or parent-children relationship. We focused on motion history since it was technically the easiest modality. However, a lot of improvements could be added studying other modalities or improving analysis by using for instance modeling or machine learning techniques by considering the conflict as a dynamic process with physiological adjustments and not a binary process.

However, it is not possible to share the raw materials with consist of confidential psychotherapy sessions. It would be very relevant to share this material to let possibility to other team to compare this results with other softwares or modules with different goals than motion history synchrony analysis. In the research in algorithm development, some databases are shared and promoted during [challenge sessions](http://sspnet.eu/avec2011/) between laboratories. This enable the development of the best classifier for instance.

### INCANT Study

#### Introduction

Cannabis dependence psychotherapy is important because cannabis is the most used illicit drug worldwide (Danovitch & Gorelick, 2012). This substance leads to cognitive troubles (motivation, social withdrawal) that could be harmful for learning process or to find a job. Furthermore, it increases the risk of schizophrenia (Large, Sharma, Compton, Slade, & Nielssen, 2011).

##### Cannabis addiction

Cannabis dependence is defined by DMS V  (Diagnostic and Statistical Manual of Mental Disorders, (American Psychiatric Association, 2013) by:
"A. A problematic pattern of cannabis use leading to clinically significant impairment or distress, as manifested by at least two of the following, occurring within a 12-month period:

1. Cannabis is often taken in larger amounts or over a longer period than was intended.
2. There is a persistent desire or unsuccessful efforts to cut down or control cannabis use.
3. A great deal of time is spent in activities necessary to obtain cannabis, use cannabis, or recover from its effects.
4. Craving, or a strong desire or urge to use cannabis.
5. Recurrent cannabis use resulting in a failure to fulfill major role obligations at work, school, or home.
6. Continued cannabis use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of cannabis.
7. Important social, occupational, or recreational activities are given up or reduced be cause of cannabis use.
8. Recurrent cannabis use in situations in which it is physically hazardous.
9. Cannabis use is continued despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by cannabis.
10. Tolerance, as defined by either of the following:
    a. A need for markedly increased amounts of cannabis to achieve intoxication or desired effect.
    b. Markedly diminished effect with continued use of the same amount of cannabis.
11. Withdrawal, as manifested by either of the following:
    a. The characteristic withdrawal syndrome for cannabis (refer to Criteria A and B of the criteria set for cannabis withdrawal, pp. 517-518).
    b. Cannabis (or a closely related substance) is taken to relieve or avoid withdrawal symptoms.

[...]
Specify current severity:

305.20 (F12.10) Mild: Presence of 2-3 symptoms.
304.30 (F12.20) Moderate: Presence of 4-5 symptoms. 
304.30 (F12.20) Severe: Presence of 6 or more symptoms." (American Psychiatric Association, 2013)

##### Cannabis addiction treatments

There are several researches for pharmacological intervention (agonist substitution, antagonist and modulation of other neurotransmitters pathways) but none approved nor recommended. 

Psychotherapy is the better treatment accessible in 2016. There are evidences for some of them: 

-	Motivational Enhancement Therapy (MET or Motivational interviewing MI) and Cognitive and Behavioural Therapies (CBT) in which I am trained 
  -Contingency Management (giving positive reinforcement to support change)
  -Familial and systems interventions, in which Multidimensional family therapy (MDFT) which is very comprehensive and much evidence based. A 224 adolescent randomized trial showed that MDFT was more effective than CBT (Liddle, Dakof, Turner, Henderson, & Greenbaum, 2008) but a big study Cannabis Youth Treatment didn't. INCANT study is an international study evaluating its efficacy (Danovitch & Gorelick, 2012).
  -In a Cochrane review, one of the most consensual Evidence Based Reviews, (Denis, Lavie, Fatseas, & Auriacombe, 2006) found 39 studies considered eligible and selected only 6 quality studies with enough quality on psychotherapeutic intervention for cannabis abuse and/or dependence in outpatient settings. Pooled together, these six studies represent 1297 patients. They confirmed the efficacy quality of CBT and MET. Contingency Management can be combined with these therapies. Systemic and familial therapies studies weren't selected in this analysis.


##### MDFT and the INCANT study

The MDFT is a "family based and developmentally oriented outpatient treatment for adolescent substance use disorders and associated or related problems" ([Incant.eu](http://www.incant.eu/)) It was developped in Miami, US since 1985. It is an integrative group of interventions used in many situations. In MDFT, sees the problem of cannabis consumption as a reflect of deleterious lifestyle. Consequently, the therapist targets as many life domains and problem behaviors as possible. 

The INCANT study was a multi-site, trans-national randomized controlled trial led in five countries (Belgium, France, Germany, the Netherlands, and Switzerland) aiming to compare the efficacy of the [MDFT](http://www.mdft.org/) versus Individual therapy. Randomization was stratified as to gender, age and level of cannabis consumption. After a pilot sudy and a [pre-registration](http://www.incant.eu/index.php?id=10,0,0,1,0,0), it recruited 450 adolescents from 13 to 18 years old. It showed that MDFT was more efficient than Individual Therapy (Rigter et al., 2013). It is very rare to run such an international study with high level of scientific setting in psychotherapy.

### INCANT Study in France

We didn't collect the videos of all the centers, instead, we had only access to the videos from French centers. There were 2 centers with different configurations. Videos were recorded to check if the therapist was applying the psychotherapy that was assigned to each family. Technically, it was not supposed a priori that these videos would be used to study social signal. For somes subjects, there are a lot of videos but for others, only a few were recorded.

### Material and methods
#### Videos
* We collected a 252.44Gb database of 277 Videos from 32 patients and their families, with a rate of 25 frames by second.
* They are encoded in [VOB](https://en.wikipedia.org/wiki/VOB) format.

#### Softwares used
* [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) tables manager
* [Powerpoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) (figures)
* [C++](https://en.wikipedia.org/wiki/C%2B%2B) Programing language used to extract motion history
* [R](https://www.cran.r-project.org/) Statistical software, filtering of the data frames, graphs
  * [xlsx package](https://cran.r-project.org/web/packages/xlsx/index.html)
* [Python](https://www.python.org/) Programing language
  * [opencv](http://opencv.org/) Module for extracting information from videos
  * [pandas](http://pandas.pydata.org/) Module for managing data frame
  * [matplotlib](http://matplotlib.org/) Module for making plots
  * [syncpy](https://github.com/syncpy/SyncPy) Module developed by the team for computing synchrony scores
  * [FFMPEG](https://ffmpeg.org/) Module for converting videos

* [Paintbrush](http://paintbrush.sourceforge.net/) Drawing program used for the frame segmentation
* [Quicktime](http://www.apple.com/quicktime/what-is/) Video player used to cut videos
* [VLC](http://www.videolan.org/vlc/) Video player

* [Elan](https://tla.mpi.nl/tools/tla-tools/elan/) Annotation software use for the essay of annotation
* [Lucidchart](https://www.lucidchart.com/) (figures)

* [Typora](http://www.typora.io/) : Markdown editor
* [Git](https://en.wikipedia.org/wiki/Git_%28software%29)
  * [GitHub website](https://github.com/Ouphix/synchro-psychotherapies) public version control repository

#### Psychometric data

Due to technicals problems we got the cannabis consumption data very late. 

However, we didn't have any data dictionary with the definition of all variables and the exact questionnaires used to collect this information, the coding of Non Available data that may be -99. We planned to meet the team that wasn't unfortunately available at that moment. A lot of videos were lost or not recorded. We couldn't have acess to the randomization to know which subjects received MDFT and which received Individual Therapy.

* These files consist of 3 [excel](https://en.wikipedia.org/wiki/Microsoft_Excel)) files with :
  * the Timeline Follow-Back [(TLFB)](http://link.springer.com/chapter/10.1007/978-1-4612-0357-5_3)
  * the Youth Self-Report syndrome structure [(YSR)](http://psycnet.apa.org/?&fa=main.doiLanding&doi=10.1037/0022-006X.75.5.729) 
  * the Child Behavior Checklist syndrome constructs [(CBCL)](http://www.ncbi.nlm.nih.gov/pubmed/10200736).

We decided to focus on the primary outcomes of the psychotherapy the cannabis consumption, i.e. the TLFB.

These data were imported via the [XLSToCSVConvertor.R](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Scripts/XLSToCSVConvertor.R) R script which I wrote.
It returns a dataINCANT.csv csv file and a [dataCannabis.csv](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Data/CSV/psychometry/dataCannabis.csv) file. 

Globally, as expected, the cannabis consumption is decreasing with time for the "mean" subjects.
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/MeanEvolution.jpeg)

Mean evolution of cannabis use of the subjects of the Incant database

However, the mean subject doesn't exist. We tried to cluster 2 groups to contrast the synchrony scores between good responders and bad responders. Unfortunately, when we looked at the evolution of the cannabis consumption, it wasn't very easy to define good and bad responders.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/TLFB2-F1044.jpg)

Evolution of cannabis use of F1044 subject

*Evolution of cannabis use for all the subjects* (table)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/EvolutionCannabis.jpeg)

*Evolution of cannabis use for all the subjects* (figure)

Consequently, we couldn't categorize good and bad responders.

### Results

#### Pilot study: F1044 subject, his father, mother and therapist

We decided to make a pilot study on the most complete subject out of the 32 patients in order to evaluate the feasability of the concept and to developp the process especially the [R scripts](https://github.com/Ouphix/synchro-psychotherapies/raw/master/INCANT/Reports/SyncPsychoIncant.pdf). We chose the F1044 subject since we have the most videos (18 videos) with him or his family.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/Numberparticipants.png)

*Number of videos from the Incant database collected*

We can ask ourselves if this subject representative:

* The therapist is the first most representative concerning the number of patients and the first concerning the number of patient videos.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/therapist.png)

*Therapists involved in the data collected from Incant study.*

* The patient is a male like in 93 % of videos. The therapist is a female in 99 % of the videos. 
* Two centers were included. This patient come from the main center.
* We have all our [psychometrics evaluations](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Data/CSV/psychometry/dataCannabis.csv) (cannabis consumption : initial, 3m, 6m, 9m, 12m).

Consequently, we can say that this subject is very representative of the sample. Unfortunately, the first, second, 10th and 11th videos were lost. 

Furthermore, when we got the cannabis consumption evolution, we saw that the efficacy of the psychotherapy was not very clear and the evolution of it wasn't straitforward. Consequently, if our hypothesis of good synchrony or good evolution of synchrony as predictor of good quality of psychotherapy was good, we couldn't really expect any of these results in the F1044 subject when we see the objective evolution of the psychotherapy. 

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/TLFB2-F1044.jpg)

*Evolution of cannabis use of F1044 subject*

### Description of the database

#### Different steps of the social signal extraction
![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/report/Extracting%20social%20signals%20%20from%20psychotherapy%20videos.png)

*This figure summarizes the databases we collected (dark blue), differents steps that were done (blue and light blue) and some suggestions (yellow) that could enable to extract social signal from psychotherapy videos.*

##### Verbal signal extraction to compute verbal synchrony

We began to extract social signal from videos with annotations made with the Elan software. The idea was to annotate the discussion of each participants.  We used [Free Video Converter](http://www.freemake.com/free_video_converter/) to get a waveform and import the video and the waveform. This waveform helped us to identify the period of discussion versus silence. Unfortunately, it couldn't help to identify the source of the sound. 

Most often locutors were filmed so it helped to detect manually who spoke but it wasn't always the case. Quite often, participant speech overlap that made the process sometimes quite difficult. There was some short onomatopoeia that were sometimes quite arbitrary to annotate or not. The end of the sentence was not always obvious with long vowels with not precise end especially during the overlap of speeches. It was made from the video and the waveform extracted from the video in an audio file. 

This process was very fastidious (1 week work for one hour video at the beginning and so was gave up). Even when I spoke with more trained annotators, the productivity is not much more better.

For the moment, when we focus on this strategy to study social signal, it is often necessary to extract manually some features even because of the lack of automatic process. Even to develop, train and evaluate these tools, this process is still compulsory.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/elan_anot.jpg)

*Screenshot of ELAN annotation software*

We tried to find ways to make source separation automatic even if it couldn't be perfect. We found the [FASST software](http://bass-db.gforge.inria.fr/fasst/). It is very powerful in order to separate sounds coming from different music instruments. However, even if the source separation of several music instruments is very efficient, diferenciating automatically two voices at the moment is too difficult. We contacted the author of this software. He told us that this material is to difficult to separate at the moment since two voices are much more similar than two different music instruments. 

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/fasst.jpg)

*Example of source separation using FASST on a music sample.*

However, this separation problem can be anticipated during the recording of the videos. Several tie-mikes could be atached to each participant.

Consequently, we decided to give up this approach.

##### Spatial organisation
In the first center, psychotherapy sessions consisted of filmed familial psychotherapies with 2 to 5 peoples organized in a circle. They are in the same room with a two-way mirror. Behind it, there is the supervisor of the psychotherapist that can call the therapist to give her some advice. The family is aware of this oragnization but this supervisor is not seen or known by them.
Two participants of the psychotherapy were filmed from the front. Another subject (often the therapist) is filmed from the other side. Its video is embedded in a window. We can notice that in this video, there isn't the patient but his two parents since he wasn't motivated enough to come to this session, which is not so problematic from a theoretical point of view in systemic therapies. It is still possible to do a pschotherapy with this settings since we consider the communication and the attitude of each member of the family and we don't consider only the patient.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/SampleSimpleFrame.png)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/DifferentConfigurations.jpeg)

*Mean Motion History in each video*

In this barplot of the mean motion history for each subject for each video, we can see the configurations of the participants involved for the F1044 subject for each video. These configurations can be very different. There are between 2 and 3 participants. All these configurations could change (eg patient-mother-therapist then mother-therapist) during the psychotherapy. Consequently, it was very difficult to compare the synchrony between different configurations. We can never get the information from the all 4 participants involved at the same time even if they are all involve like in D2 video since the psychotherapist wasn't filmed because of technicall reasons. In some videos, we don't have any information from the therapist because she isn't filmed. The patient is not very present in the therapy (because of compliance).

When we sum up the data we get, we can see that the mother and the therapist are the most present participants.



##### Time organization
Video length could were very different because it was necessary to reorganize them. 

However, we couldn't use the raw database. It was necessary to cut the videos with [Quicktime](https://en.wikipedia.org/wiki/QuickTime) software since a phone was used during the psychotherapy to communicate between the main psychotherapist and the supervisor behing a two-way mirror and the therapy stopped at that moment. Sometimes, the participants made some pauses or the same video was used for different patient.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/lengthVideoF1044.png)

### Raw data
### Motion extraction

#### Extracting frame from the beginning of the video
Extract a frame with [*Frames_extractor.py*](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Frames_extractor/Frames_extractor.py) with a [python](https://www.python.org/) script from the beginning of the video to make a mask. This script was developed by Jonathan Aigrain with FFMPEG.

Here is an example of the father (eyes blurred to keep anonymity).

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/SampleSimpleFrame.png)

It was suggested to take a mean image of the video to superimpose the different configurations of the subjects on one video to be more precise during the spacial segmentation instead of taking a frame from the beginning of the video.

It would be much more relevant to extract the exact 3D position of the skeleton instead of the raw pixel. This can be extracted quite easily by a [kinect](http://www.xbox.com/fr-FR/xbox-one/accessories/kinect-for-xbox-one). In a complex setting like this, it could be usefull to use even several kinects for each side of the room or even better for each subject. A lot of other features could be extracted but the volume of this data can be very heavy with several megabytes by minute of video. This is much more difficult technicall difficulties to be handle by the clinicians team during the recording, especially the synchronisation of the different cameras but would be much more relevant than raw videos alone. Some algorithm can extract relevant social signal from videos were they are recorded from the front (smiles, emotions, direction of the head (Hupont, Baldassarri, & Cerezo, 2012 ; Torre et al., 2015).

#### Creating a mask for each relevant part of each video with Paintbrush
We selected a part of the video with each participant (father, mother, patient, therapist) with [*Paintbrush*](http://paintbrush.sourceforge.net/). We took only the upper part of the body of each subject to compare them since you can see only the upper part of the therapist. Consequelty, we had one mask for each participant, so beween 2 and 3 masks for each video.



![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/F1044C1paint.mov.avi.father.jpg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/F1044C1.mov.avi.father.jpg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/segmentation.png)

#### Technical problems

Unfortunatelly, since the videos weren't not recorded for this specific purpose, we can notice several pitfalls.

The zoom level of the parents and the zoom level of the therapist was different. We'll see that they are hardly comparable.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/conflict.png)

In this frame, we can notice that there is an overlap between the region of interest of the therapist (in the upper part, embedded in a window) and the mother (right). Some motion history from the mother could consequently be lost.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/otherTroubles.png)

In this frame, we can see that half of the motion history from the mother couldn't be recorded since it was outside the camera view. Moreover, there is an overlap of the date and the time with the patient frame (top). 

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/ExampleFrames/dateProblem.png)

In this frame, we can see that the date is overlapping with the therapist. This was a big problem since the time was always changing and changed the pixels in this zone.

Sometimes, the camera is moving during the film. Obviously, this leads to a shift of pixel and consequently a signal of motion history even if nobody is moving. Consequently, it is very important to keep a motion less camera or cameras.

Sometimes, there are big movements of the suject which are not relevant for us. The therapist speaks with an other one via a phone, the participants left the room or 

Participants can move during the video (change their seats, leave the room, even several families were recorded on the same video). It would be preferable to anticipate it. Camera is moving sometimes too. Mean Motion history by minute can help us to detect big changes or disappearance of a participant to do temporal segmentation/anotation.

In the future, it would be usefull to use [Deep learning software](http://image-net.org/challenges/LSVRC/2014/) or machine learning used for categorization/detection of people could make this process completely automatic. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/deeplearningsegmentation.jpg)

#### Motion history extracted

The VOB videos were converted in [AVI](https://en.wikipedia.org/wiki/Audio_Video_Interleave) format in the form *F1044C1.avi*.

With these masks and videos, we could extract motion history with a [C++](https://en.wikipedia.org/wiki/C%2B%2B) script. It returns
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file of the form "*F1044C.VOB_res2.csv*". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/INCANT/Data/CSV/MotionHistory/raw). We can notice that we can change the value of the [median filter](https://en.wikipedia.org/wiki/Median_filter). In order to be able to compare several subjects, we decided to divide the motion history extracted by the size of the frame selected, it correct partly the zoom problem. 

The motion history doesn't have any unit, it is the percentage of change of pixels change among all the pixels seclected (non msked in green here). 

If we make a plot (in histograms and box plots) this raw data, we notice that the distribution is not normal at all. Very small motion history values are over represented and bigger motion history are much more rare with a very long tail. Consequently, it is difficult to compare two distributions from two different subject. To normalize the distribution to compare the motion distribution of several subjects and compute synchrony scores on it, we made the natural logarithm.

Unfortunately, several values equal to 0 and the log function can not be applied. They generate a -Inf value. If these values are set to NA, we lose the information of no movement at all. If we give a arbitrary value to this data by shifting the discribution by a very small value (eg. the half first value after 0), they are over represented) like in figure 2.

| Raw Motion history                       | Natural Log Motion history               |
| ---------------------------------------- | ---------------------------------------- |
| Father                                   |                                          |
| ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/MotionHisoryFatherRaw.jpeg) | ![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/loffather.jpg) |
| All participants                         |                                          |
| ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/MotionHistoryBoxPlots.jpeg) | ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/LogMotionHistoryBoxplots.jpeg) |

If we check all participants, we can see that the father and the mother motion history distribution are very similar. However, the therapist, which is always in a small window of the video with a different zoom, has a very different distribution. We have less signal on it. In some videos the patient is in this window, it explains, it intermediates position. Consequently, we can say that the signal extracted on the therapist is not directly comparable with the signal from the other subjects. A lot very small movements are not detected by the software and leads to 0 values. These values are over-represented.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/datalogtherapist.jpg)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/loffather.jpg)

- It could be possible to extract [background](https://en.wikipedia.org/wiki/Background_subtraction) to improve the quality of the motion history. See for instance [backgroundExtractor.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/INCANT/Scripts/backgroundExtractor.py) with openCV [BGS library](https://github.com/andrewssobral/bgslibrary/blob/master/README.md).

Instead of extracting only the motion history, we could extract more relavant signals.

- It could be interesting to evaluate the trajectories of the people. If they two people are going toward the same direction or not can change everything in understanding a human interaction even if the motion history is the same. For that, the [optic flow modules of open CV](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html) or the [Dense Trajectories Video Description](http://lear.inrialpes.fr/people/wang/dense_trajectories) could help. ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/trajectories.png)

Tiny changes can't be always obvious. [Some softwares](https://lambda.qrilab.com/site/) can amplify a lot very tiny changes in specific frequencies that can't be seen normally with naked eyes. This enable for instance the extraction of the heart pulsation of the subject, which could be the reflect of the stress without any invasive physical contact.![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/report/magnifyingMotion.png)

#### Motion history filtered with slindingInterval function

I filtered motion history raw data with a [R](https://www.cran.r-project.org/) function on [Rmarkdown script analysis](https://github.com/Ouphix/synchro-psychotherapies/blob/master/SyncPsycho.Rmd). It generates CSV file of the form "F1044C.VOB.slideddata.csv". See files [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/filtered). I developped two functions, one to filter motion history without changing the frequency of the data by sliding the reading frame to compute the mean.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/slidingInterval.jpg)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/MeanMotionByTime.jpg)

| Sliding interval (filtered raw Data)     | Sliding interval (filtered log Data)     |
| ---------------------------------------- | ---------------------------------------- |
| ![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/MeanMotionHistory%28Sliding5framesinterval_raw_data%29on%20F1044C1_first_10_seconds.jpeg) | ![Content Cell](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/MeanMotionHistory%28Sliding5framesinterval_log_data%29on%20F1044C1_first_10_seconds.jpeg) |

It is possible to change the size of interval to change the ration signal/noise.

We can see that there is a shift of the therapist motion history even in the filtered raw data. It is possible that the noise on this small window makes decrease the signal/noise ratio.

Bad quality of first frames at the beginning or end of the videos with NA were deleted to prepare the next script analysis.

 The number of frames is changed since it is necessary to get frames before and after the index.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/meanMotion.jpg)

The representation of the mean motion by minute enable to detect high change of motion history that could be the reflect of movement of all persons in the scene.

##### Computing synchrony score with this filtered motion data

To compute synchrony SyncPy used the amplitude (difference between min and max. The baseline levels (min) are not relevant to compute synchrony.

In this configuration, the patient is embeded in the window, the mother and father are in front of the main camera. The therapist isn't filmed.

We downloaded and installed [SyncPy](https://github.com/syncpy/SyncPy).

We adapted the script [Call_S_Estimator.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Call_S_Estimator.py) that must be installed in Syncpy installation in examples folder. We used this script because we had continuous data and tried to compute synchrony between more than two subjects.We created a folder *SynchronyCSV* in this folder.

The script in [Python](https://www.python.org/), [Call_S_Estimator.py](https://github.com/Ouphix/synchro-psychotherapies/blob/master/Scripts/Call_S_Estimator.py) takes this filtered motion data and compute a synchrony score for each association possible of two or more subjects.

To compute the synchrony, we use the S_Estimator algorithm that is drawn from information theory. It makes a matrix of correlation on the  standardised motion history time series (mean =0 and SD = 1). Consequeltly, only the shape of the signal matters. Afterwards, it computes the eigenvalues of this matrix. Finally, after the normalization of the eigenvalues, it can compute the synchrony from a sort of entropy (Carneli et al, 2005). Hte index ranges from 0 (no synchrony) to 1 (full synchrony). If all signals are equals, the synchrony scores equals 1.

**You need to specify,**

- the folder where you put your data (eg dataFolder = '/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/filtered/') 
- The cvs files are automatically detected from this folder and S_estimator is used on them.
- the number of frames used in an interval to compute synchrony, Nota bene, there are 25 frames by second. (eg. numberOfFramesByInterval = 25*10). We chose this parameter since it seems to be clinically relevant but other parameters could be tested.

This process is relatively long and can take several minutes, especially with short intervals. It returns synchrony CSV files that can be found [here](https://github.com/Ouphix/synchro-psychotherapies/tree/master/CSV/SynchronyCSV).

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/synchrony.jpg)

We expected that the signal to fluctuate between 0 and 1. However, we can see that the signal fluctuate only beween 0 and 0.25 with a lot of synchrony scores very low around 0. The synchrony scores are better with the subjects in front of the main camera i.e. the mother and the father in this configuration.

We saw that the distribution of motion history was much more informative when we compared the log of it instead of the raw data. This enable to detect the aberrant distribution of the therapist and the periods with no motion at all which were over-represented.

When we did the log scores before computing even if it was interresting in order to compare motion history distributions, however, that didn't change the relevance of the synchrony signal.

When we tried to check what could be the relevance of this signal, since the psychotherapy wasn't very operationnalized, it was difficult to match the two. We contacted the INCANT team however, we couldn't meet them quickly.

There is not any NA in this file. Only the possible combinations are computed (eg there is not the *patient* (*pa*) in the video so, there isn't *SSI_fa_pa* signal neither any other combination with the patient).

We can evaluate the evolution of the synchrony for a dyad or tryad through the evolution of the psychotherapy. Here it is represented hrough the whole therapy. Sometimes, there wasn't any data because the configuration didn't enable that. We can notice that is not obvious to evaluate and compare the synchrony of a dyad if it is alone or with other participants since the interaction could be different.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/INCANT/Data/images/plots/SSImoth.jpg)

We saw that the evolution of cannabis use of F1044 is not straightforward. It is quite high at the beginning, decreases and then increases. Consequently, we couldn't evaluate of the dynamic of the synchrony could be a predictor of the psychotherapy and the consumption of cannabis since this ast dynamic wasn't clear. 

We decided to select 4 subjects with a clear decrease of cannabis consumption, we expected that this better dynamic could give clearer results.

* F1002, patient, 3 videos
* F1073, patient, 2 videos
* F1069, patiente, 4 videos
* F1101, patient, 3 videos

All of them with the same therapist Mrs Bastard. However, we had problems with the conversion of the files from VOB to AVI. The number of videos from this families were much lower, to evaluate a dynamic could even more challenging. Since, we got a better database with less technicall problems on it and a experimental setting, we decided to switch to it to further developp the concept.

##### Advantages of this Incant database

INCANT study was done internationally with:

- good level of scientific method with a pre-registration done in major journals in a psychotherapy field where the level of quality of the studies can be not very good.

- potential possibility to retest the model on videos taken from other countries if available and/or generalize it.

- Data came from almost real life family therapy settings the would be easier to generalize to everyday practice.

- Pragmatically, it was the first database we got, so we could begin to ask real life problems.

##### Limits of this Incant database
#### Experimental set-up
It is however not very defined in the articles. Consequently, it was difficult to contrast synchrony between two well defined periods. A much more operrationnalized psychotherapy like motivational interviewing could be useful. This kind of psychotherapy can be rated with the degree of adherence of the psychotherapist to the principles of the therapy like the MITI. Consequently, we could compare two quantitative variables that will reflect the quality of the psychotherapy at a more precise moment instead of a more general outcome.

##### Technical limits
It would be better to have a more experimental set up to improve this problems, make a specific database for this kind of automatic analyses to avoid changes of configuration of the room, the luminosity, the place of the different subjects, the number of subjects, the movement of the camera during recording.

It seems that it would be very important to have several devices (camera, kinect, mikes, actimetr). This leads to a problem that wasn't raised in this set up since there was only one camera. In case, of several devices, it is very important that all of them are synchronized.

To begin to work in a multiperson psychotherapy was theorcally possible and the team developped scripts for that on SyncPy (S_Estimator) however, it is much more challenging that evaluate the synchrony of the dyad since the configuration needs to be comparable, the subject musn't overlap and must be filmed in the same conditions (zoom).

#### Conclusion

We couldn't answer the questions with the INCANT study we asked in the pre-registration, because of the technicals and quality  problems of the database and experimental setting. We can't say if the motion history synchronization between different participants are correlated with the outcomes of the familial psychotherapy (decrease consumption of cannabis).

Since the number of videos can be very low, we couldn't neither say if the synchrnony coud be the reflect of the adherence.

However, this database can precisely enlighten some points that need to be adressed to consider this evaluation.

## MONRADO study
### Aim of the study
The aim of the study was to evaluate the response to a conflict in a dyad of a parent and a child. There were two phases. After the experimenter left the room, the dyad spoke about casual topics. After around 5 minutes, the experimenter came back in the room and asked the dyad to speak during around 10 minutes about a conflictual conflict that was selected by the child before the video during an interview alone with him or her.

Consequently, from these videos, we can extract easily two phases that we could contrast : without then with conflict.

##### Configuration

The participants are two in front of the camera. We can see that the quality of the video is much better. There is not often overlap between the subject. There isn't embedded subjects with a different zoom level. There is not any date embedded. All the subjects that takes part in the interaction are filmed.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/ExampleFrames/00034.jpg)

##### Selection of relevant videos

In order to match the psychometric data which was more important and the videos, we decided to clean the database to delete the copies and keep only the data with psychometric informations. We decided to delete a video with a different configuration with the two parents.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/report/FlowchartMonrado.jpeg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/configuration.jpeg)

Presence of participants,



The configuration in the different videos are very similar.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/NumberOfAvailable.jpeg)

In these videos all the participants are filmed. The child is always filmed. More often, the mother is involved but not the father.

##### Length of the videos

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/length%20minutes.jpg)

We can see that the length of the videos are very similar. In NUMA027 video, the instructions were not very well understood by the subjects. The mother left the room before the end to see the experimenter.

#### Psychometric data
* It consist of one excel file with:
  * Identification number
  * Identification of the video
  * Demographic information (Age, Birthday, Birth place)
  * Attachment style
  * TAS Score
  * STAIYA Score
  * BDI score

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/age.jpg)

The mean age of the participants was 15.4 years (SD : 2.0).

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/Birth%20places.jpg)

Most of the children were born in Besancon.

TODO Frequency

Sex of the child

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/sex.jpg)

82 % of the teenagers involved were female.

TODO FrequenCY

##### Attachment style

Attachment theory is a psychological model that tries to describe the dynamics of short and long-term relationships between humans. 

The Attachment Style Interview for Adolescents (ASI-AD) is a user-friendly, transparent and reliable measure. It offers the adolescents the opportunity to talk about their recent life events, their close relationships (with parents and friends), their support networks and how they feel about getting close to others. (Jacobs et al, 2012). Caring about attachment in young people in residential care: The use of the Attachment Style Interview. (‘Community Care Inform’ electronic information source. Spring 2012)

Catherine Jacobs, Yael Ilan-Clarke and Professor Antonia Bifulco, Lifespan Research Group, Centre for Abuse and Trauma Studies) http://www.attachmentstyleinterview.com/

Attachement styles were Secure, Enmeshed, Fearful, Withdrawn and Dual when two different styles)

After a contact with the MONRADO team, we clustered the attachments styles in 3 groups:

* Secure
* Fearful-Enmeshed (FE)
* Withdrawn
* DUAL were excluded

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/Attachement%20styles%20clusters.jpg)

Secure (44%) and Fearful-Enmeshed (FE) (38%) clusters are over-represented.

##### TAS Score

The Alexithymie
The TAS (Toronto Alexithymie Score) that was developed by Taylor, Graeme J.; Ryan, David; Bagby, R. Michael (1986). "Toward the development of a new self-report alexithymia scale". Psychotherapy and Psychosomatics, 44, 191-199. It was translated by M.P. Marchand et G. Loas (1994). It evaluates the level of Alexythymie. If this level is high, the ability of the adolescent to understand and express his own emotions is low.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/TAS.jpg)

##### STAIYA Score
The STAIYA or State-Trait Anxiety Inventory of Spielberger is an auto-evaluation of Anxiety. It is one of the most used Anxiety auto- questionnaire. It dissociate the anxiety at a precise moment (state) and the habitual anxiety of the subject (trait). When this quetionnaire was developped, it was evaluated on more than 5000 subjects. The score ranges from 20 to 80.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/STAIYA.jpg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/STAIYB.jpeg)

BDI Scores

The Beck Depression Inventory is a depression score ranging from 0 to 63. It evaluates the severoty of a depression when it was clinically diagnosed. From 0-13, the depressive state is minimal, between 14 and 19, the depressive state is mild (Osman, 2008). This mesure support that the teenagers recruited in this study are not severe depressed people but not depressed people.										

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/BDI total-2.jpg)

#### Description of the database

* We collected a database of 85.48 Gb of 40 videos, with a rate of 25 frames by second.
* They are encoded in a [MTS format](https://en.wikipedia.org/wiki/AVCHD) in a much better quality than the previous database.

We used the same procedure that for the INCANT study, we masked the non relevant part of a frame for each subject. Instead of selecting only the upper part of the bidy, we were able to select the half of the image with more information about the subjects.

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/ExampleFrames/00034.MTS.mother.png)

![image](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/ExampleFrames/00034.MTS.child.png)

#### Extraction of motion history

TODmother

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/Motion%20history%20histogram%20by%20frame%20%28raw%20data%29%2C%20all%20videos-1.jpg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/boxplotsraw.jpeg)

We can see that the distribution of motion history is vey similar with the motion history extracted from the INCANT study. The small movements are very important and the big movements are very rare with a long tail.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/Motion%20history%20histogram%20by%20frame%20%28raw%20data%29-1.jpg)

When we compute the log of this data, we can notice that the distribution is much more normal that for the INCANT study. The first pick representing the null motion histories (no motion) is much smaller and not overrepresented. This confirm that the quality of the motion history signal extracted from this video is much better than the previous one extracted from INCANT study.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/Motion%20history%20by%20frame%20box%20plots%20%28raw%20data%29-1.jpg)

When we compare these distributions, we can see that these distribution are much more similar that the distributions in the INCANT study in which the therapist motion history distribution was very different from the other distributions.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/SI.jpg)

Like in the INCANT study, we filtered the motion histories.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/NoConflict-ConflictMH-small.jpg)

TODO : cut zone in the middle

We could very easilly detect the two periods of the video. THe first one without any conflict and the second with a conflict. These periods we annotated manually. 

The cutFrames data frame was done manually by looking manually all videos and definining:

* when the experimenter leaves the room and the interaction begin, 

Between is the non conflictual discussion

* when the experimenter comes back to ask participants to have a conflictual discussion
* when the experimenter leaves and the conflictual discussion begins
  Between is the conflictual discussion
* when the experimenter comes back to shut down the camera

However, we can notice that the conflict wasn't always very authentic and important. It would be interesting to ask outside observers, blinded with the objective of the study to annotate the level of the conflict of the participants. That would be done with crowdsourcind and will be much more easier that the annotation of speech that we did for the INCANT study.

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/NoConflict-ConflictSSI-small.jpg)

TODO histogram synchrony scores 

However, we can see that the synchrony score are not so much different that from the INCANT study. Although, it was expected theorically (matematically) to fluctuate between 0 and 1, the maximum of it is around 0.2-0.3 depending on the videos. When we did the log scores before computing however, that didn't change the relevance of the signal.

Thanks to that, we were able to compare the mean motion history between the two conditions.

### Results

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/raw%20Global%20motion%20history%20by%20situation%20%3A%20conflict%20vs%20no%20conflict.jpg)

![](https://raw.githubusercontent.com/Ouphix/synchro-psychotherapies/master/Monrado/Data/images/plots/SSImeansbarplot.jpeg)

As expected and like previous authors showed before, it seemed that the synchrony is lower in conflictual situations. However, the difference is not significative.

We did a paired t-test between the mean of synchony scores during the no conflict period and the conflict period. However this difference is notsignificative


data:  ncSSI and cSSI
t = 0.16743, df = 33, p-value = 0.8681
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval: -0.007279512  0.008585109
sample estimates: mean of the differences 0.0006527983 

It is possible that is analysis is not proper due to the non normal distribution of both motion history and synchrony socres. The next steps will be to evaluate the synchrony scores in different conditions (different psychometric scores, especially attachment evaluation) and make proper statisticall evaluations. We consider too, presenting the process to psychotherapy training team to get raw data of better quality. We will meet a representant of the Motivational Interviewing Network of Trainers (MINT).

##### Technical problems

There wasn't many problems with this database. There was only one video which no movement of the camera. There wasn't any date emebeded in the videos. There was very few overlap of the subjects.

However, the subjects weren't always looking at the camera that would be a problem to automatically detect their emotions, their smiles for instance. 

##### Discussions

It could be relevant to annotate the level of conflict by blinded annotators since the conflict is not always completely obvious nor strong.

## Discussion

### Experimental discussion

We saw with the INCANT study that there was a limit with contasting different conditions. In order to make this possible, it would be usefull to use much more opperationnalized psychotherapy like (Assertivenes, Motivational interviewing, exposition), but it is not restricted to CBT. We could use it in (provocation vs no provocation used in brief psychotherapy, hypnosis induction versus no hypnosis induction, dream analysis )

Analysis discussion

We could make a shuffle of the data to check if the signal if more synchrone than expected by chance. We could try to replicate this data with a more simple algorithm : correlation.py which was specifically designed for a 2 persons synchrony study.

In the future, we could integrate much more kind of social signals and the cluster of it in a more general score could be more relevant. Some techniques in modelling used at the moment in neuroscience in fMRI could de very usefull for this purpose. 

# Perspectives

We could extract other features : 

* **Psychometric**
  * **Annotation** : annotation of conflict and non conflict period with [Elan](https://tla.mpi.nl/tools/tla-tools/elan/) software to get better time resolution especially with more complex annotations. In subjective annotations if they are not too much difficult, it would be usefull to use crowsourcing anotation by asking naive subjects about the level of conflict or stress that can be detected on a video.


* **Physiological**
  * **Cortisol** : Cortisol levels can be the reflect of stress. Some techniques are minimally invasive like [saliva measures](http://www.sciencedirect.com/science/article/pii/0009898181903533.)(Teruhisa et al., 1981).
  * **Ocytocin** : Ocyctonin could be involved in attachment and trust [(Kosfeld, Heinrichs, Zak, Fischbacher, & Fehr, 2005)](http://www.nature.com/nature/journal/v435/n7042/full/nature03701.html). This could improve the social competence of Asperger patients with some social impairments. We could imagine to evaluate the relationship and the synchrony of two subjects normal and with social impairments with and without oxytocin.
  * **Cardiac Frequency :** direct or indirect on videos with systems like [Lambda](https://lambda.qrilab.com/site/) or [webcam pulse detector](https://github.com/thearn/webcam-pulse-detector)
  * **Electrodermal activity t**hat seems to be relevant in stress, dissonance cognitive paradigms. Its history as feedback of psychotherapy is ver old since it was used in [psychoanalysis by C. G. Jung](http://www.freezoneearth.org/allmeters/scrapbook/historymeter.htm#Die%20Wort).

* **Motion information**

  We could be much more precise in the measure of the motion by using a Motion capture devices. There are basically two systems:

  * We could measure directly very cheaply motion by using **actimetry** devices that looks like watches on the wrist. Unfortunately, taht could help for motion of hands but that couldn't give precise information about the motion of the head.
  * One is minimally invasive with a **Kinect**, a special camera that project infra-red light and can detect it to measure depth of a scene. It has a much a higher frequency signal detect that can rebuild a 3D representation of a subject and extract its skeletton. We saw that the law frequency of the signal we got 25 Hz could be a limitation of the synchrony signals we could get.  
  * Optitrack that are some **markers on the body** of the subject that can help to create a 3D representation of the subject.
  * An other strategy is to use special **suits** like in the [Ethome](https://www.youtube.com/watch?v=IBPxokjqvZ8) project that could record precisely a lot of motions directly.
  * **Facial / Upper body recognition :** We could use automatical detection of Facial / Upper body recognition to segment images automatically instead doing it automatically.
  * **Emotions**: We could use a camera for each person to have a more precise vision of its face to detect emotions more easily. 
  * **Background subtraction** could be useful to improve the quality of the motion we get
  * We could measure the **gaze direction** to check if the quantity of gaze interaction could be a reflect of a good relationship like it is desribed widely by the psychiatrist and psychotherapist in social impairments (social phobia, autism, schizophrenia)
  * **Trajectories :** We could measure optic flow and trajectories instead of motion since the 


* **Speech extraction**

  * We could anticipate the problem of speech extraction by using mikes to compute the synchrony of this signal


#	Bibliographie
American Psychiatric Association. (2013). *Diagnostic and StatisticalManual of Mental Disorders (DSM-5®)*. American Psychiatric Pub.

Bandura, A., Ross, D., & Ross, S. A. (1963). Imitation of film-mediatedaggressive models. *The Journal of Abnormal and Social Psychology*, *66*(1),3‑11. http://doi.org/10.1037/h0048687

Beauvois, J.-L., & Joule, R.-V. (1996). *A Radical Dissonance Theory*.Taylor & Francis.

Beck, A. T., Steer, R. A., & Carbin, M. G. (1988). Psychometricproperties of the Beck Depression Inventory: Twenty-five years of evaluation. *ClinicalPsychology Review*, *8*(1), 77‑100.http://doi.org/10.1016/0272-7358(88)90050-5

Bonnefont, Courade, Alloui, & Eschalier. (2002). [Antinociceptivemechanism of action of paracetamol]. *Drugs*, *63 Spec No 2*, 1‑4.

Bouhuys, A. L., & Sam, M. M. (2000). Lack of coordination of nonverbalbehaviour between patients and interviewers as a potential risk factor todepression recurrence: vulnerability accumulation in depression. *Journal ofAffective Disorders*, *57*(1–3), 189‑200. http://doi.org/10.1016/S0165-0327(99)00093-2

Briffault X., L’évaluation des psychothérapies, Méthodes, résultats, réflexions,Séminaire de Pierre-Henri Castel du 14 janvier 2009

Canceil, O., Cottraux, J., Falissard, B., Flament, M., Miermont, J.,Swendsen, J., … médicale, I. national de la santé et de la recherche. (2004).Psychothérapie : trois approches évaluées [Study report]. Consulté 22septembre 2015, à l’adresse http://lara.inist.fr/handle/2332/1323

Corbière, M., Bisson, J., Lauzon, S., & Ricard, N. (2006). Factorialvalidation of a French short-form of the Working Alliance Inventory. *InternationalJournal of Methods in Psychiatric Research*, *15*(1), 36‑45.http://doi.org/10.1002/mpr.27

Cungi, C., & Cottraux, J. (2006). *L’alliance thérapeutique*.Paris: Retz.

Danovitch, I., & Gorelick, D. A. (2012). State of the Art Treatmentsfor Cannabis Dependence. *The Psychiatric Clinics of North America*, *35*(2),309‑326. http://doi.org/10.1016/j.psc.2012.03.003

Delaherche, E., Chetouani, M., Mahdhaoui, A., Saint-Georges, C., Viaux, S.,& Cohen, D. (2012). Interpersonal Synchrony: A Survey of Evaluation Methodsacross Disciplines. *IEEE Transactions on Affective Computing*, *3*(3),349‑365. http://doi.org/10.1109/T-AFFC.2012.12

Denis, C., Lavie, E., Fatseas, M., & Auriacombe, M. (2006).Psychotherapeutic interventions for cannabis abuse and/or dependence inoutpatient settings. In *Cochrane Database of Systematic Reviews*. JohnWiley & Sons, Ltd. Consulté à l’adressehttp://onlinelibrary.wiley.com/doi/10.1002/14651858.CD005336.pub2/abstract

Dumas, G., Nadel, J., Soussignan, R., Martinerie, J., & Garnero, L.(2010). Inter-Brain Synchronization during Social Interaction. PLoS ONE, 5(8),e12166. http://doi.org/10.1371/journal.pone.0012166

 Festinger, L., & Carlsmith, J.M. (1959). Cognitive consequences of forced compliance. *The Journal ofAbnormal and Social Psychology*, *58*(2), 203‑210.http://doi.org/10.1037/h0041593

Fond, G., Micoulaud-Franchi, J.-A., Macgregor, A., & Ducasse, D.(2014). La manipulation dans la pratique de l’entretien psychiatrique. *L’Encéphale*,*40*(3), 203‑207. http://doi.org/10.1016/j.encep.2013.04.005

Horvath, A. O., & Dianne, B. (1991). Relation between working allianceand outcome in psychotherapy: A meta-analysis. *Journal of CounselingPsychology*, *38*(2), 139‑149.http://doi.org/10.1037/0022-0167.38.2.139

Dehaene, S. Fondements cognitifs des apprentissages scolaires, séminaire aucollège de France http://www.college-de-france.fr/site/stanislas-dehaene/course-2014-2015.htm

Iacoboni, M. (2009). Imitation, Empathy, and Mirror Neurons. *AnnualReview of Psychology*, *60*(1), 653‑670. http://doi.org/10.1146/annurev.psych.60.110707.163604

Joule, R.-V. (1987). La dissonance cognitive : un état demotivation? *L’année psychologique*, *87*(2), 273‑290.http://doi.org/10.3406/psy.1987.29204

Joule, R.-V., & Beauvois, J.-L. (2010). *La soumission librementconsentie* (Édition : 6e édition revue et corrigée). Paris: PressesUniversitaires de France - PUF.

Large, M., Sharma, S., Compton, M. T., Slade, T., & Nielssen, O.(2011). Cannabis use and earlier onset of psychosis: a systematicmeta-analysis. *Archives of General Psychiatry*, *68*(6), 555‑561.http://doi.org/10.1001/archgenpsychiatry.2011.5

Lakin, J. L., Jefferis, V. E., Cheng, C. M., & Chartrand, T. L. (2003).The Chameleon Effect as Social Glue: Evidence for the Evolutionary Significanceof Nonconscious Mimicry. *Journal of Nonverbal Behavior*, *27*(3),145‑162. http://doi.org/10.1023/A:1025389814290

Layard, R., & Clark, D. M. (2014). *Thrive: The Power ofEvidence-Based Psychological Therapies*. Penguin UK.

Liddle, H. A., Dakof, G. A., Turner, R. M., Henderson, C. E., &Greenbaum, P. E. (2008). Treating adolescent drug abuse: a randomized trialcomparing multidimensional family therapy and cognitive behavior therapy. *Addiction*,*103*(10), 1660‑1670. http://doi.org/10.1111/j.1360-0443.2008.02274.x

Martin, D. J., Garske, J. P., & Katherine, M. (2000). Relation of thetherapeutic alliance with outcome and other variables: A meta-analytic review. *Journalof Consulting and Clinical Psychology*, *68*(3), 438‑450.http://doi.org/10.1037/0022-006X.68.3.438

Miller, W. R., & Rollnick, S. (2013). *L’entretien motivationnel - 2eéd. - Aider la personne à engager le changement* (Édition : 2eédition). Paris: InterEditions.

Moyers, Manuel, & Ernst. (s. d.). Motivational InterviewingTreatment Integrity Coding Manual 4.1 (MITI 4.1). Consulté 22 septembre 2015, àl’adresse http://research2vrpractice.org/miti-4-1-now-available/

Neal, D. T., & Chartrand, T. L. (2011). Embodied Emotion PerceptionAmplifying and Dampening Facial Feedback Modulates Emotion Perception Accuracy.*Social Psychological and Personality Science*, *2*(6), 673‑678.http://doi.org/10.1177/1948550611406138

Orsucci, F. F., Musmeci, N., Aas, B.,Schiepek, G., Reda, M. A., Canestri, L., ... & de Felice, G. (2016).Synchronization Analysis of Language and Physiology in Human Dyads. *Nonlineardynamics, psychology, and life sciences*, *20*(2), 167-191.

Ramseyer, F., & Tschacher, W. (2011). Nonverbal synchrony inpsychotherapy: Coordinated body movement reflects relationship quality andoutcome. *Journal of Consulting and Clinical Psychology*, *79*(3),284‑295. http://doi.org/10.1037/a0023419

Rigter, H., Henderson, C. E., Pelc, I., Tossmann, P., Phan, O., Hendriks,V., … Rowe, C. L. (2013). Multidimensional family therapy lowers the rate ofcannabis dependence in adolescents: A randomised controlled trial in WesternEuropean outpatient settings. *Drug and Alcohol Dependence*, *130*(1–3),85‑93. http://doi.org/10.1016/j.drugalcdep.2012.10.013

Rizzolatti, G., & Craighero, L. (2004). The Mirror-Neuron System. *AnnualReview of Neuroscience*, *27*(1), 169‑192.http://doi.org/10.1146/annurev.neuro.27.070203.144230

SPIELBERGER C.D. GORSUCH R.L., LUSHENE R.E. - Manual for the State-TraitAnxiety inventory ("Self evaluation questionnaire"). ConsultingPsychologists Press, Palo Alto, CA, 1970.

Tschacher, W., Haken, H., & Kyselo, M. (2015). Alliance: a commonfactor of psychotherapy modeled by structural theory. *Psychology forClinical Settings*, *6*, 421. http://doi.org/10.3389/fpsyg.2015.00421

Varni, G., Avril, M., Usta, A., & Chetouani, M. (2015). SyncPy: AUnified Open-source Analytic Library for Synchrony. In *Proceedings of the1st Workshop on Modeling INTERPERsonal SynchrONy And infLuence* (p. 41–47).New York, NY, USA: ACM. http://doi.org/10.1145/2823513.2823520

Weisman, O., Delaherche, E., Rondeau, M., Chetouani, M., Cohen, D., &Feldman, R. (2013). Oxytocin shapes parental motion during father–infantinteraction. *Biology Letters*, *9*(6), 20130828.http://doi.org/10.1098/rsbl.2013.0828

More bibligraphy cna be found here

https://www.zotero.org/groups/448197/items 





TODO However, we need to keep in mind that this intermediate markers are only intermediateand are not always relevant. Some anti-diabetics decrease Hb1Ac and Increase mortality whereasclassical one decrease both. 

