# NNVideoTracking

An RNEL Solution to Approximate Rodent Head Tracking in an Attempt to Account for Occlusion by Wires, and Determine Head Direction When Fed a Video

# Some Notes on Usage:

This implementation is not meant to be used as a realtime tracker. Our neural network approximates the center of the rodents head and movement path to predict rodent head direction at any given time, referencing the weighting that has been created by its training set.