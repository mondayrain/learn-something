# Digital Audio 101

### Digital Audio is Math

Digital audio is math; mathematically, sound can be described as a wave.

All sound waves have at least one **push** and one **pull**, which make up a cycle. All sound waves contain at least one cycle.

Sound is **periodic**: any periodic function can be mathematically represented as a series of sine waves. So, each sound is just a large mesh of sine waves.

Any waves over 22kHz is not necessary (we can't hear them!)

To convert these sound waves into digital audio, we take snapshots called **samples**, and each has an **amplitude**.

### Basic Terminology

**Decibel**

A logarithmic unit of measurement. It expresses a quantity relative to a reference level. In most recording software, 0dB is the _loudest_ a track can get before it starts clipping.

**Sample Rate**

The number of "samples" of audio carried per second, measured in Hz or kHz.

**Bit depth**

How many bits are used to contain each sample. This determines how "precise" our digital sample of the real analog sound can be.

**Quantization Error**

The "error" we get when converting infinitismal analog values to finite digital values (e.g. 3.1002349498 to 3.1), as the precision is limited by how many bits are allocated to storing a value. When this precision is lost, the actual shape of the sound gets distorted.

The higher the bit depth, the lower the quantization error.

**Noise Floor**

The measure of signal created from the sum of all noise sources + unwanted signals.