# NNVideoTracking

A prototype of an RNEL solution to rodent head tracking in an attempt to account for occlusion by wires, and determine head direction when fed a video.

# Some Notes on Usage:

This implementation is not meant to be used as a realtime tracker. Our neural network approximates the center of the rodents head and movement path to predict rodent head direction at any given time, referencing the weighting that has been created by its training set.

The head tracking program has been implemented for use on video collected during behavioral experiments, in an effort to qualify rodent movement.