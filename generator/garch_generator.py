import numpy as np

def garch_generator(n,a0,a1,a2,b1,b2,seed=53,sigsq_=False):
    '''Generates epsilon values for GARCH model up to 2nd order(GARCH(2,2))
    Set a2=0 and b2=0 to simulate a GARCH(1,1) model
    ---------------------------
    Returns:
    sigsq : square of time dependent error standard deviation
    eps :
    ---------------------------
    Parameters:
    n: sample size
    a0: alpha_0
    a1: alpha_1
    a2: alpha_2
    b1: beta_1
    b2: beta_2
    seed: set seed for Gaussian white noise generator
    ----------------------------
    Formula:
    sigma^2_t = a_0 + a_1*epsilon^2_t-1 + a_2*epsilon^2_t-2 + b_1*sigma^2_t-1
    + b_2*sigma^2_t-2'''
    np.random.seed(seed)
    w = np.random.normal(size=n)
    eps = np.zeros_like(w)          #ERROR terms
    sigsq = np.zeros_like(w)        #VARIANCE terms

    for i in range(2, n):
        sigsq[i] = a0 + a1*(eps[i-1]**2) + a2*(eps[i-2]**2) + b1*sigsq[i-1] + b2*sigsq[i-2]
        eps[i] = w[i] * np.sqrt(sigsq[i])
    if sigsq_:
        return(eps,sigsq)
    else:
        return(eps)
