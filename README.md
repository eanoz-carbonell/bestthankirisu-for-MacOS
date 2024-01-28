# bestthankirisu
Bestthankirisu transforms and normalizes time-dependent spectral data obtained with the ProData-SX software (Applied Photophysics Ltd.)
The advantage over the original kirisu (developped by José Ramon Peregrina and Jorge Estrada, University of Zaragoza) is that the code can be runned over multiple files at the same time. Additionally, it implements several tools for spectral smoothing.

The programm allows to truncate (and smooth) all the .glt files on a directory "glb" and save the processed files .glb_t into a new directory "glb_t". Therefore, the programm: (1) loads the data, (2) smooths the absorbance with respect the wavelenth for each time (optional step), (3) modifies the spectra to make all times zero at a specific wavelenght, (4) trims the spectrea to onlyu include up to a minimun and a maximun time and wavelenth, and (5) generates the converted files in a new folder.

