# NNVideoTracking

A prototype of an RNEL solution to rodent head tracking in an attempt to account for occlusion by wires, determine head direction, and classify gait of a rodent during a behavioral task, none of which were features in our earlier implementation.

## Current Implementation:

The network currently available is an implementation of Faster R-CNN, trained on a very fine dataset.

## The Plan:

Though still in Beta phase, I am aiming to use a correlation filter to aid a neural network during training to distinguish a rodent's head from the rest of it's body when fed a video. Then, optical flow information will be used to determine the velocity of the rodent, which is important in determining both the head direction of the rodent and his gait. Simultaneously, the video will be input to a recurrent convolutional neural network in order to distinguish the rat's position in space. This complex system of programs shall be easily accessible to the average user through a GUI launchable from the Linux terminal.

# Some Notes on Usage:

This implementation is an offline tracker. We are not attempting to track in real time. Our neural network approximates the center of the rodents head and movement path to predict rodent head direction at any given time, referencing the weighting that has been created by its training set.

The head tracking program has been implemented for use on video collected during behavioral experiments, in an effort to qualify rodent movement. In this way, we hope to better determine a rodent's behavior during such a task.
