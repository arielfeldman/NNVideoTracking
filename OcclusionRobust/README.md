# NNVideoTracking

A prototype of an RNEL solution to rodent head tracking in an attempt to account for occlusion by wires, determine head direction, and classify gait of a rodent during a behavioral task, none of which were features in our earlier implementation.

# Some Notes on Usage:

This implementation is not meant to be used as a realtime tracker. Our neural network approximates the center of the rodents head and movement path to predict rodent head direction at any given time, referencing the weighting that has been created by its training set.

The head tracking program has been implemented for use on video collected during behavioral experiments, in an effort to qualify rodent movement. In this way, we hope to better determine a rodent's behavior during such a task.
