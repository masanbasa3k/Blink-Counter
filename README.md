# Blink-Counter
Eye blink counter using OpenCV.

![Blink](https://github.com/masanbasa3k/Blink-Counter/assets/66223190/7990347f-f02f-4644-be9d-980c7a93369a)


# Explanation
I have created an eye blink counter using OpenCV. OpenCV is a popular computer vision library that provides tools and functions for image and video processing.

To build the eye blink counter, I used techniques like face detection and eye tracking. Firstly, I utilized a pre-trained face detection model to locate faces in the video or webcam feed. Once the face is detected, I used another model to identify the eyes within the face region.

Next, I implemented an algorithm to track the movement and changes in the eyes over time. By analyzing the changes in eye shape or movement patterns, I determined whether a blink occurred.

The program keeps a count of the number of blinks that happen during the video or webcam session. This blink count can be used for various purposes, such as monitoring drowsiness levels in drivers or studying eye behavior in different situations.

Overall, using OpenCV and computer vision techniques, I successfully developed an eye blink counter that can accurately track and count the number of blinks in a video or through a webcam feed.
