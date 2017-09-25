import numpy as np
from scipy.stats import ttest_ind, ttest_ind_from_stats
from scipy.special import stdtr

'''
    Null hypothesis :  The means of both groups are the same.
    Alternative hypothesis : Both means are significantly different.
'''

def solution(array1, array2, s_level=0.05):
    '''
        True, if set1 and set2 are significantly different.
        False, if they are significantly not different.
    '''
    # Convert into np array
    array1 = np.array(array1)
    array2 = np.array(array2)

    # Compute the descriptive statistics of a and b.
    array1_bar = array1.mean()
    array1_var = array1.var(ddof=1)
    array1_N = array1.size  	# number of elements
    array1_dof = array1_N - 1   # Degrees of freedom

    array2_bar = array2.mean()
    array2_var = array2.var(ddof=1)
    array2_N = array2.size
    array2_dof = array2_N - 1

    # Method 1
    # Use scipy.stats.ttest_ind.
    result = ttest_ind(a=array1, b=array2)
    t_statistics = result[0]
    p_value = result[1]
    print("Using scipy.stats.ttest_ind.: t = %g  p = %g" % (t_statistics, p_value))

    # Method 2
    # Use scipy.stats.ttest_ind_from_stats.
    t_statistics, p_value = ttest_ind_from_stats(array1_bar, np.sqrt(array1_var), array1_N,
    	array2_bar, np.sqrt(array2_var), array2_N, equal_var=False )
    print("Using ttest_ind_from_stats: t = %g  p = %g" % (t_statistics, p_value))

    # Method 3
    # Use the formulas directly.
    t_statistics = (array1_bar - array2_bar) / np.sqrt(array1_var/array1_N + array2_var/array2_N )
    dof = (array1_var/array1_N + array2_var/array2_N)**2 / (array1_var**2/(array1_N**2*array1_dof) + array2_var**2/(array2_N**2*array2_dof) )
    p_value = 2 * stdtr(dof, -np.abs(t_statistics))
    print("Using formulas : t = %g  p = %g" % (t_statistics, p_value))

    if p_value > (s_level/2):
        # Failed to reject null. Both means are not significantly different.
        return False
    else:
        # Reject Null. Both means are significantly different.
        return True
