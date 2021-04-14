# SDND Project 4 - Behavioral Cloning

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

***The output video [here](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P4/output.mp4).***

### I. Files & Code

#### 1. Required Files

The project includes the following files:
* modelG.py (P4.ipynb for notebook) - containing the script to create and train the model
* drive.py - for driving the car in autonomous mode
* modelG.h5 - containing a trained convolution neural network 
* P4 - README.md - summarizing the results

#### 2. Run
Using the Udacity provided simulator and file drive.py, the car can be driven autonomously around the track by executing: 

```sh
python drive.py modelG.h5
```

The modelG.py file contains the code for training and saving the convolution neural network. The file shows the pipeline used for training and validating the model, and it contains comments to explain how the code works.

### II. Model Architecture and Training Strategy

#### 1. The NVIDIA PilotNet
![f1](https://github.com/lhzlhz/PilotNet/blob/master/readme/PilotNet.png) <br>
I used the NVIDIA PilotNet for the project, since it has proven high performance in steering control. My final model consisted of the following layers: <br>

|            Layer            |                        Description                       | 
|:---------------------------:|:--------------------------------------------------------:| 
| Input                       | 320x160x3 Cropped RGB image                              | 
| Lambda                      | 320x65x3 Cropped and normalized image                    | 
| Convolution Layer 1         | 5x5x24 Filter. 2x2 Strides. Same padding. Out: 160x33x24 |
| ELU          			  		    | Activation layer    	                                   |
| Batch Normalization - CONV1 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Same padding. Out: 80x17x24                 |
| Convolution Layer 2         | 5x5x36 Filter. 2x2 Strides. Same Padding. Out: 40x9x36   |
| ELU           					    | Activation layer    	                                   |
| Batch Normalization - CONV2 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Same padding. Out: 20x5x36                  |
| Convolution Layer 3         | 5x5x48 Filter. 2x2 Strides. Same Padding. Out: 10x3x48   |
| ELU           					    | Activation layer    	                                   |
| Batch Normalization - CONV3 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Same padding. Out: 5x2x48                   |
| Convolution Layer 4         | 3x3x64 Filter. 1x1 Strides. Same Padding. Out: 5x2x64    |
| ELU           					    | Activation layer    	                                   |
| Batch Normalization - CONV4 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Same padding. Out: 3x1x64                   |
| Convolution Layer 5         | 3x3x64 Filter. 1x1 Strides. Same Padding. Out: 3x1x64    |
| ELU           					    | Activation layer    	                                   |
| Batch Normalization - CONV5 |      	                                                   |
| Max Pooling        	        | 2x2 Strides. Same padding. Out: 2x1x64                   |
| Flatten          			      | Out: 128    	                                           |
| Fully Connected Layer 1	    | Out: 100                                                 |
| Batch Normalization - FC1   |                                                          |
| Droput	                    | Keep probability: 0.8                                    |
| Fully Connected Layer 2	    | Out: 50                                                  |
| Batch Normalization - FC2   |      	                                                   |
| Droput	                    | Keep probability: 0.8                                    |
| Fully Connected Layer 3	    | Out: 10                                                  |
| Batch Normalization - FC3   |      	                                                   |
| Droput	                    | Keep probability: 0.8                                    |
| Fully Connected Layer 4	    | Out: 1                                                   |
| Sigmoid                     | Output layer                                             |


#### 2. Reducing Overfitting

The approaches used in the project to reduce overfitting are as followed: <br>

  1)  Batch normalization: BN layers were added after each activation layer and fully-connected layer. <br>
  2)  Capturing more driving data: more laps were captured in the simulator, in both clockwise and counter-clockwise drivings. <br>
  3)  Data augmentation & using side cameras: the images and steering angles were flipped, images from all 3 cameras were used. <br>
  4)  Drop-out: drop-out layers were added after each fully-connected layer, with keep probability of 0.8. <br>
  5)  Pooling: max-pooling layers were used after each convolution layer. <br>

#### 3. Parameter Tuning

The model used an adam optimizer, so the learning rate was not tuned manually. Different combinations of *batch_size*, *epochs*, *correction factor* for left and right camera, *keep_prob*, *cropping*, as well as activation functions were tested. The experimental results show that:

  1) Using a smaller *batch_size* helps the training complete faster, no significant loss variation for different *batch_size:s* (32, 64, 128). The final *batch_size* was set to **32**. <br>
  2) Firstly the model was set to be trained for 25 epochs, although the accuracy is higher than fewer epochs, overfitting occurred and sometimes the car performed a sudden turning (which were not oberved when the epochs were fewer). The final number of *epochs* was set to **5**. <br>
  3) Smaller losses were observed when using a smaller *correction factor* (0.1) for the side cameras, however in the first two curves after driving off the bridge the car always have insufficient steering angle and drove off the road (compared with larger correction factors: 0.15, 0.2, 0.25). The final *correction* was set to **0.2**. <br>
  4) Lower *keep_prob* caused higher losses with no significant improvement in overfitting reduction. Thus, the *keep_prob* was finally set to **0.8**. <br>
  5) It was tickled that if the track scene in the upper image could help improve the accuracy, however no significant improvement was oberved, but the overfitting became worse when preserve more irrelevant pixels. The *cropping* was finally set to **(70, 25)**. <br>
  6) No obvious difference was oberved when using the 'ReLU' and 'ELU' activation function, **ELU** was used in the project. <br>

#### 4. The training data

The captured data were preprocessed in 3 steps before fed into the training set: <br>

|   Operation   |   Target   | 
|:-------------:|:---------------:| 
| Read-in original       |  All images from 3 cameras  | 
| Steering angle correction   |  Steering angles in left & right camera images 	|
| Flip - left/right					 |  All the images and the corrected angles (\*-1.0)	|

Firstly I recorded 3 laps' driving data (use keyboard control) as taught in the course. However the trained model had a bad performance when driving on curves and bridge, there were also too many sudden turnings happend. This may caused by using keyboard to control the car, since it has more discrete steering angles recorded which was not good for the training. 

Then I tried using mouse to steer the car. The sudden turns reduced (should be more comfortable for the passengers), however the car still drove off the road, especially in some high-curvature sectors. The model performed badly in generalization. 

Then I recorded more laps (both clockwise and counter-clockwise driving), fortunately the car could drive itself more smoothly and only drove off the road in two curves (the sand strip after the bridge and the curve road after it). 

Finally after I recorded much more data of these two curves and re-trained the model, the car could get through all of the sections. In the process some errors occurred when it's driving on the straight road, these were solved by recording some more driving data on the normal road sections (to appropriately dilute the data for specific curves). <br>

Visualized loss curve is showed below: <br>
![f2](https://github.com/PictoNailer/SDND-PROJECTS/blob/main/P4/Visualization%20-%20Loss.png)]
