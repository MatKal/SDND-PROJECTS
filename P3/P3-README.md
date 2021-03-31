# **P3 - TRAFFIC SIGN RECOGNITION** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

## I. Data Set Summary & Exploration
### Basic Summary of the Datasets. 
 
I used the pandas and numpy library to calculate summary statistics of the traffic signs data set:

The size of training set is: **34799**.
The size of the validation set is: **4410**.
The size of test set is: **12630**.
The shape of a traffic sign image is: **(32, 32, 3)**.
The number of unique classes/labels in the data set is: **43**. 

### Exploratory Visualization of the Datasets.
Here is an exploratory visualization of the datasets.

Image below shows some random images from the training set:
![f1](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-expl.png)

Chart below shows the distribution of different classes in the datasets:
![f2](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Dataset-visualz.png)

## II. Design and Test a Model Architecture
### Data Preprocessing
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

### Final Model Architecture
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

### Train the Model
To train the model, I used an Adam optimizer and the following hyperparameters:

1) Learning rate - eta: 0.009. 
2) Number of epochs: 50. 
3) Batch size: 128. 
4) Keep probalbility of dropout layers: 0.5. 

### The Final Solution
My final model results were:

Training set accuracy of **99.3%**.
Validation set accuracy of **94.5**.
Test set accuracy of **92.5**.

1) I used LeNet-5 for the project because it is popular and has proven good performance in classification. The output was changed from 10 to 43 according to the number of classes in the German traffic signs dataset.
2) Initially I used a learning rate (eta) of 0.01, batch size of 128 and 25 epochs. 
3) With fixed eta and batch size, I increased the number of epochs to 30, 40, 50, and got an slightly improved accuracy, and an epoch number of 50 was set by the end. Then I experimented with different batch sizes (and correspondingly different eta:s - e.g. batch_size=64, eta=0.005), there was no obvious improvement on the accuracy, but only slight differences in the training speed, so the batch size 128 was remained. Accuracies #1 (Train/Valid/Test): 97.4%/91.6%/89.8%. 
4) To avoid overfitting, two dropout layers for the fully-connected layers were added after RELUs, with a keep_prob of 0.5. Accuracies #2: 98.7%/92.4%/90.9%. 
5) Then four batch normalization layers were inserted between RELU and Pooling/Dropout layers, which resulted in a better accuracy and training speed. Accuracies #3: 99.1%/93.2%/91.8%. 
6) Finally I experimented with different decay rates for the Adam optimizer. Instead of using the default beta:s (0.9), a slower decay (0.95) somehow(?) resulted in a better accuracy. Accuracies #4: 99.3%/94.5%/92.5%. 
7) Future tweakings: increase the depth of the convolution kernel, using different optimizers/learning rate decay schemes. 

## III. Test the Model on New Images
### 6 German Traffic Signs from the Web
Here are six German traffic signs that I found on the web (resized to 32x32):
![f4](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Webimg_plot.png)

### The Model's Predictions
![f5](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P3/output/Webimg_predict.png)

### Top 5 Softmax Probabilities
Below are the top five softmax probabilities for each image: <br>

Image: 1  Label: 25<br>
Probabilities:<br>
   0.999926 : 25 - Road work<br>
   0.000041 : 1 - Speed limit (30km/h)<br>
   0.000030 : 24 - Road narrows on the right<br>
   0.000001 : 27 - Pedestrians<br>
   0.000001 : 2 - Speed limit (50km/h)<br>
<br>
Image: 2  Label: 4<br>
Probabilities:<br>
   0.983205 : 4 - Speed limit (70km/h)<br>
   0.005348 : 5 - Speed limit (80km/h)<br>
   0.004728 : 15 - No vehicles<br>
   0.003943 : 3 - Speed limit (60km/h)<br>
   0.001539 : 1 - Speed limit (30km/h)<br>
<br>
Image: 3  Label: 17<br>
Probabilities:<br>
   1.000000 : 17 - No entry<br>
   0.000000 : 9 - No passing<br>
   0.000000 : 34 - Turn left ahead<br>
   0.000000 : 14 - Stop<br>
   0.000000 : 33 - Turn right ahead<br>
<br>
Image: 4  Label: 12<br>
Probabilities:<br>
   0.998089 : 12 - Priority road<br>
   0.001846 : 9 - No passing<br>
   0.000058 : 35 - Ahead only<br>
   0.000005 : 40 - Roundabout mandatory<br>
   0.000001 : 10 - No passing for vehicles over 3.5 metric tons<br>
<br>
Image: 5  Label: 11<br>
Probabilities:<br>
   0.999543 : 11 - Right-of-way at the next intersection<br>
   0.000453 : 30 - Beware of ice/snow<br>
   0.000003 : 27 - Pedestrians<br>
   0.000001 : 18 - General caution<br>
   0.000000 : 34 - Turn left ahead<br>
<br>
Image: 6  Label: 31<br>
Probabilities:<br>
   0.978842 : 31 - Wild animals crossing<br>
   0.005244 : 39 - Keep left<br>
   0.005094 : 13 - Yield<br>
   0.004865 : 5 - Speed limit (80km/h)<br>
   0.003008 : 2 - Speed limit (50km/h)<br>
