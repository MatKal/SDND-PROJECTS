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

Image below shows some random images from the training set:
![f1](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-expl.png)

Chart below shows the distribution of different classes in the datasets:
![f2](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-visualz.png)

## II. Design and Test a Model Architecture
### 1. Data Preprocessing
The process of data preprocessing includes three steps: 1) shuffling the 3 sets, 2) data augmentation for the training set, and 3) normalization and grayscaling for validation and test set.

In step ***2) data augmentation***, each image will go through a type of transformation/adjustment randomly:
|   Operation   |   Probability   | 
|:-------------:|:---------------:| 
| Keep original       |  60%  | 
| Flip - left/right   |  10% 	|
| Flip - up/down					 |  10% 	|
| Random brightness  	|  10%  |
| Random contrast	    |  10%  |

In step ***3) normalization & grayscaling***, each image will be converted to grayscale image **(32, 32, 1)** and normalized by ***((image - 128) / 128)***, scaling the pixel value from **\[0~255]** to **\[-1, +1]**. Image below shows a comparison between original and processed image in the training set: 
![f3](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Data_preproc.png)

### 2. Final Model Architecture
My final model consisted of the following layers:

|            Layer            |                        Description                       | 
|:---------------------------:|:--------------------------------------------------------:| 
| Input                       | 32x32x1 Grayscale image                                  | 
| Convolution Layer 1         | 5x5x6 Filter. 1x1 Strides. Valid padding. Out: 28x28x6 	 |
| RELU          					         | Activation layer    	                                    |
| Batch Normalization - CONV1 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Valid padding. Out: 14x14x6                 |
| Convolution Layer 2         | 5x5x16 Filter. 1x1 Strides. Valid Padding. Out: 10x10x16 |
| RELU          					         | Activation layer    	                                    |
| Batch Normalization - CONV2 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Valid padding. Out: 5x5x16                  |
| Flatten          			        | Out: 400    	                                            |
| Fully Connected Layer 1	    | Out: 120                                                 |
| RELU          					         | Activation layer                                        	|
| Batch Normalization - FC1   |                                                         	|
| Droput	                     | Keep probability: 0.5                                    |
| Fully Connected Layer 2	    | Out: 84                                                  |
| RELU          					         | Activation layer                                        	|
| Batch Normalization - FC2   |      	                                                   |
| Droput	                     | Keep probability: 0.5                                    |
| Fully Connected Layer 3	    | Out: 43                                                  |

### 3. Train the Model
To train the model, I used an Adam optimizer and the following hyperparameters:

1) Learning rate - eta: 0.009. 
2) Number of epochs: 50. 
3) Batch size: 128. 
4) Keep probalbility of dropout layers: 0.5. 

### 4. The Final Solution
My final model results were:

Training set accuracy of **99.3%**.
Validation set accuracy of **94.5**.
Test set accuracy of **92.5**. 

