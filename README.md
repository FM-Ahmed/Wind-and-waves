# Wind
### getSamplingPara.py
Gathers sampling parameters f and t. Originally written by Etienne Cheynet in MATLAB: https://se.mathworks.com/matlabcentral/profile/authors/4608373

### KaimalModel.py
Kaimal spectral model.

### Davenport.py
Calculate the coherence using the Davenport coherence model.

### Example.py
Example of how getSamplingPara.py and KaimalModel.py can be used in unison to plot the Kaimal spectral model.

## Low-level-jet
### generate_LLJ.py
Generates random low-level jets based on input parameters. Can keep either the LLJ core-speed or LLJ core-height equal.

### single_LLJ.py
Creates a low-level jet based on some input parameters.

# Waves
### jonswap.py
Takes Hs, Tp, df and fcutoff_high to return the JONSWAP spectrum. It is based on the JONSWAP implementation in the HydroDyn module in OpenFAST. Returns the JONSWAP spectrum as a function of both frequency and angular frequency.  

### Example_JONSWAP.py
This file shows an example of the usage of the function jonswap.py. First, an arbitrary spectrum was made with randomly chosen inputs. Then, the spectrum was converted to a wave elevation time series. 

### seastate_anim.py
An animation of the sea and waves.
![anim](https://github.com/FM-Ahmed/Wave-modelling/assets/128718838/bb9fdc31-d98f-48e8-9c0b-08b5d07952ed)

