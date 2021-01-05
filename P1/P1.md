# **P1 - Finding Lane Lines on the Road** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P1/Cover.png?raw=true)

### 1. Pipeline Description

The process consisted of 8 steps. Firstly the input video is read in. Then for each frame a Canny edge detection is performed. Within this process there are 3 sub-steps: converting the original frame to grayscale, Gaussian blur the grayscale image and finally the Canny function. Thirdly the region of interest (triangle) is masked with a fixed set of indices (for the two videos with a resolution of 960*540). cv2.HoughLinesP is then performed to find the winner lines. In order to draw a single line (Step 5) on the left and right lanes, I modified the line-drawing function by adding a process of averaging the lines detected by the Hough function, where the lines are averaged and mapped into Cartesian coordinate system. After drawing the deteced lane lines the two layers are added and write into the output video. 


### 2. Limitations

The sets of parameters for Canny edge detection, ROI masking, as well as the HoughLinesP function are all fixed so the robustness of the solution is limited. When the code is run over the challenge video, it cannot detect curved lane lines, mistakes the junctions between concrete and asphalt surfaces as lane lines. 


### 3. Future Improvements

Possible improvement would be to let the program chose parameters adaptively with advanced algorithms, pre-process the frames with other method to smooth the gradient change in different road surfaces. 
