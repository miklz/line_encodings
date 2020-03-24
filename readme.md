# Pulse-Amplitude modulation

This is a personal project to implement and analyze some of the line codifications used in
systems of communication.

## Description

The codifications implemented so far, with no return to zero is:
- Non Return to zero level (NRZ(L))
- Non Return to zero spacial (NRZ(S))
- Non Return to zero inverted (NRZ(I))
- Polar quaternary

And with return to zero:
- Return to zero level (RZ(L))

Clock edge:
- Manchester

The way that the functions were made, they can be unipolar or bipolar, this
only depends of the parameters v_min and v_max passed to the functions.

## Analysis

The analysis made refers to the variance, standard deviation and power spectrum density of each codification line. At the moment I'm implementing the error produced by the channel in the communication system, the goal is to observe how the noise produced by the transmission can affect a message being send.
