#include <QtCore/QCoreApplication>
#include <qdir.h>
#include <qfile.h>
#include <iostream>
#include <opencv2\opencv.hpp>
#include <Windows.h>
#include <NuiApi.h>
#include <ppl.h>

#include "VideoManager.h"
#include "ImageProcessing.h"

int transform(cv::Mat& mask)
{
	int res = 0;
	for (int x = 0; x < mask.rows; ++x)
			for (int y = 0; y < mask.cols; ++y)
			{
				int b = mask.data[mask.step[0] * x + mask.step[1] * y];
				int g = mask.data[mask.step[0] * x + mask.step[1] * y + 1];
				int r = mask.data[mask.step[0] * x + mask.step[1] * y + 2];
				if (g == 255 && b == 0 && r == 128)
				{
					mask.data[mask.step[0] * x + mask.step[1] * y + 1] = 0;
					mask.data[mask.step[0] * x + mask.step[1] * y + 2] = 0;
				}
				else
				{
					mask.data[mask.step[0] * x + mask.step[1] * y] = 1;
					mask.data[mask.step[0] * x + mask.step[1] * y + 1] = 1;
					mask.data[mask.step[0] * x + mask.step[1] * y + 2] = 1;
					res++;
				}
			}
	return res;
}

double computeValue(cv::Mat& img1, cv::Mat& img2)
{
	const int thresh = 20;

	cv::Mat diff(img1.size(), img1.type());
	cv::absdiff(img1, img2, diff);
	cv::Mat diffGrayScale(diff.size(), CV_8UC1);
	cv::cvtColor(diff, diffGrayScale, CV_BGR2GRAY);
	cv::Mat threshed(diffGrayScale.size(), diffGrayScale.type());
	cv::threshold(diffGrayScale, threshed, thresh, 255, CV_THRESH_BINARY);

	return (double)cv::countNonZero(threshed);
}

void thomas()
{
	QDir videoDir("C:\\Users\\UPMC\\Documents\\Data\\Synchronie\\data");
	QStringList videos = videoDir.entryList();
	QDir frameDir("C:\\Users\\UPMC\\Documents\\Data\\Synchronie\\F1044ChestOnly");
	//Concurrency::parallel_for(0, videos.length(), [videos, videoDir, frameDir] (int currVideo)
	foreach(QString videoName, videos)
	{
		//QString videoName = videos[currVideo];
		if (!videoName.startsWith("F1044"))
			continue;
		cv::Mat fatherMask, motherMask, patientMask, therapistMask;
		bool father, mother, patient, therapist;
		if (father = QFile::exists(frameDir.absolutePath() + "/" + videoName + ".father.png"))
			fatherMask = cv::imread((frameDir.absolutePath() + "/" + videoName + ".father.png").toStdString());
		if (mother = QFile::exists(frameDir.absolutePath() + "/" + videoName + ".mother.png"))
			motherMask = cv::imread((frameDir.absolutePath() + "/" + videoName + ".mother.png").toStdString());
		if (patient = QFile::exists(frameDir.absolutePath() + "/" + videoName + ".patient.png"))
			patientMask = cv::imread((frameDir.absolutePath() + "/" + videoName + ".patient.png").toStdString());
		if (therapist = QFile::exists(frameDir.absolutePath() + "/" + videoName + ".therapist.png"))
			therapistMask = cv::imread((frameDir.absolutePath() + "/" + videoName + ".therapist.png").toStdString());

		

		int fArea = transform(fatherMask);
		int mArea = transform(motherMask);
		int pArea = transform(patientMask);
		int tArea = transform(therapistMask);

		std::cout << videoName.toStdString() << " :  father = " << father << ", mother = " << mother << ", patient = " << patient
			<< ", therapist = " << therapist << std::endl;

		cv::VideoCapture video((videoDir.absolutePath() + "/" + videoName).toStdString());
		double nbFrames = video.get(CV_CAP_PROP_FRAME_COUNT);
		std::cout << nbFrames << " frames" << std::endl;
		cv::Mat frame;
		video >> frame;
		cv::Mat fprec = father ? frame.mul(fatherMask) : cv::Mat();
		cv::Mat mprec = mother ? frame.mul(motherMask) : cv::Mat();
		cv::Mat pprec = patient ? frame.mul(patientMask) : cv::Mat();
		cv::Mat tprec = therapist ? frame.mul(therapistMask) : cv::Mat();
		QFile resFile("C:\\Users\\UPMC\\Documents\\Data\\Synchronie\\csv\\" + videoName + "_res2.csv");
		resFile.open(QFile::WriteOnly);
		resFile.write("frame,father,mother,patient,therapist,file\n");
		//video.set(CV_CAP_PROP_POS_FRAMES, 31424);
		for (int i = 1; i < nbFrames; ++i)
		{
			video >> frame;
			if (frame.dims == 0 || frame.rows == 0)
			{
				resFile.write((QString::number(i) + ",NA,NA,NA,NA,").toStdString().data());
				resFile.write((videoName + "\n").toStdString().data());
				continue;
			}
			cv::Mat fImg = father ? frame.mul(fatherMask) : cv::Mat();
			cv::Mat mImg = mother ? frame.mul(motherMask) : cv::Mat();
			cv::Mat pImg = patient ? frame.mul(patientMask) : cv::Mat();
			cv::Mat tImg = therapist ? frame.mul(therapistMask) : cv::Mat();
			resFile.write((QString::number(i)).toStdString().data());
			resFile.write(father ? ("," + QString::number(computeValue(fImg, fprec) / fArea)).toStdString().data() : ",NA");
			resFile.write(mother ? ("," + QString::number(computeValue(mImg, mprec) / mArea)).toStdString().data() : ",NA");
			resFile.write(patient ? ("," + QString::number(computeValue(pImg, pprec) / pArea)).toStdString().data() : ",NA");
			resFile.write(therapist ? ("," + QString::number(computeValue(tImg, tprec) / tArea)).toStdString().data() : ",NA");
			resFile.write(("," + videoName + "\n").toStdString().data());

			fImg.copyTo(fprec);
			mImg.copyTo(mprec);
			pImg.copyTo(pprec);
			tImg.copyTo(tprec);
		}
		resFile.close();
		std::cout << "done" << std::endl;
	}
	//});
}

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);
	//thomas();
	//return a.exec();
	if (argc < 3)
	{
		std::cerr << "Usage : ./BehaviourAnalyzer <dir path> <feature file>" << std::endl;
		return 1;
	}


	QDir peopleDir(argv[1]);
	if (!peopleDir.exists())
	{
		std::cerr << "The folder " << argv[1] << " does not exist.";
		return 1;
	}
	
	for (int i = 2; i < argc; ++i)
	{
		std::cout << "!!!!!!!!!!!!!!!!!!!" << argv[i] << "!!!!!!!!!!!!!!!!!!!!!!!!" << "\n";
		VideoManager vManager(peopleDir, argv[i]);
		vManager.run();
	}


	std::cout << "Execution done." << std::endl;
	return a.exec();
}