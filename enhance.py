import numpy as np


def enhance(im, stdval=3.0, just_alpha=False):
    """
    Enhance an image by normalizing color channels by
    their mean and standard deviation.
    """
    if just_alpha:
        nim = im[:,:,:3]
        nz = nim[nim>0.0]
        nim = nim/(nz.mean()+stdval*np.std(nz))
        nim[nim>1.0]=1.0
        nim[nim<0.0]=0.0
        del nz
    else:
        nim = np.zeros_like(im[:,:,:3])
        for c in range(3):
            nz = im[:,:,c][im[:,:,c]>0.0]
            nim[:,:,c] = im[:,:,c]/(nz.mean()+stdval*np.std(nz))
            del nz
        nim[:,:][nim>1.0]=1.0
        nim[:,:][nim<0.0]=0.0
    return nim
