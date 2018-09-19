#!/bin/bash
# Program:
#  batch.

logver = 3

echo "Process ourPicture..."
python facedetect_openCV.py ourPicture/ default > log/${logver}/0106Output_openCV_default_ourPicture.out
python facedetect_openCV.py ourPicture/ alt > log/${logver}/0107Output_openCV_alt_ourPicture.out
python facedetect_openCV.py ourPicture/ alt2 > log/${logver}/0108Output_openCV_alt2_ourPicture.out
python facedetect_openCV.py ourPicture/ alt_tree > log/${logver}/0109Output_openCV_alt_tree_ourPicture.out


echo "Process data10000..."
echo "Proccess data10000 default..."
python facedetect_openCV.py data10000/ default > log/${logver}/0110Output_openCV_default_data10000.out
echo "Proccess data10000 alt..."
python facedetect_openCV.py data10000/ alt > log/${logver}/0111Output_openCV_alt_data10000.out
echo "Proccess data10000 alt2..."
python facedetect_openCV.py data10000/ alt2 > log/${logver}/0112Output_openCV_alt2_data10000.out
echo "Proccess data10000 alt_tree..."
python facedetect_openCV.py data10000/ alt_tree > log/${logver}/0113Output_openCV_alt_tree_data10000.out


