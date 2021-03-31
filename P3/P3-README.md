# **P3 - TRAFFIC SIGN RECOGNITION** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

## I. Data Set Summary & Exploration
### 1. Basic Summary of the Datasets. 
 
I used the pandas and numpy library to calculate summary statistics of the traffic signs data set:

The size of training set is: **34799**.
The size of the validation set is: **4410**.
The size of test set is: **12630**.
The shape of a traffic sign image is: **(32, 32, 3)**.
The number of unique classes/labels in the data set is: **43**. 

### 2. Exploratory Visualization of the Datasets.
Here is an exploratory visualization of the datasets.

***Figure 1*** shows some random images from the training set:
![f1](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-expl.png)
<p align="center">
  <b>Figure 1.</b> Random samples in the training set. 
</p>

***Figure 2*** is a chart showing the distribution of different classes in the datasets:
![f2](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-visualz.png)
<p align="center">
  <b>Figure 2.</b> Numbers of samples per class. 
</p>

## II. Design and Test a Model Architecture
### 1. Data Preprocessing
The process of data preprocessing includes three steps: 1) shuffling the 3 sets, 2) data augmentation for the training set, and 3) normalization and grayscaling for validation and test set. ***Figure 3*** shows a comparison between original and processed image in the training set: 
![f3](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-expl.png)
<p align="center">
  <b>Figure 3.</b> Comparison before/after preprocessing. 
</p>

In step ***2) data augmentation***, each image will go through a type of transformation/adjustment randomly:
|   Operation   |   Probability   | 
|:-------------:|:---------------:| 
| Keep original       |  60%  | 
| Flip - left/right   |  10% 	|
| Flip - up/down					 |  10% 	|
| Random brightness  	|  10%  |
| Random contrast	    |  10%  |

