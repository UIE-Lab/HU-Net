
import numpy as np
from .GuidedFilter import GuidedFilter

def  RefinedTransmission(transmissionB,transmissionG,transmissionR,img):

    gimfiltR = 50
    eps = 10 ** -3
    
    guided_filter = GuidedFilter(img, gimfiltR, eps)
    transmissionB = guided_filter.filter(transmissionB)
    transmissionG = guided_filter.filter(transmissionG)
    transmissionR = guided_filter.filter(transmissionR)

    transmission = np.zeros(img.shape)
    transmission[:, :, 0] = transmissionB
    transmission[:, :, 1] = transmissionG
    transmission[:, :, 2] = transmissionR
    return transmission
