# example of the Friedman Test with post-hoc analysis and Control method
from numpy.random import seed
from numpy.random import rand
from stac.nonparametric_tests import friedman_test
from stac.nonparametric_tests import bonferroni_dunn_test
from stac.nonparametric_tests import holm_test
from stac.nonparametric_tests import finner_test
from stac.nonparametric_tests import hochberg_test
from stac.nonparametric_tests import li_test

# seed the random number generator
seed(1342)

# generate two independent samples
data1 = 50 + (rand(10) * 10)
data2 = 51 + (rand(10) * 10)
data3 = 52 + (rand(10) * 10)

# compare samples
stat, p, rankings, pivots = friedman_test(data1, data2, data3)
print('Statistics=%.3f, p=%.3f' % (stat, p))
print('Ranking =', rankings)
print('Pivots =', pivots)

alg_list = {'a1': pivots[0], 'a2': pivots[1], 'a3': pivots[2]}

# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')

comparison, Z, p_values, adj_p_values = bonferroni_dunn_test(alg_list, control='a1')

print('Comparison', comparison)
print('BONFERRONI DUNN POST-HOC')
print('Z', Z)
print('p_values', p_values)
print('adj_p_values', adj_p_values)

comparison, Z, p_values, adj_p_values = holm_test(alg_list, control='a1')

print('HOLM POST-HOC')
print('Z', Z)
print('p_values', p_values)
print('adj_p_values', adj_p_values)

comparison, Z, p_values, adj_p_values = finner_test(alg_list, control='a1')

print('FINNER POST-HOC')
print('Z', Z)
print('p_values', p_values)
print('adj_p_values', adj_p_values)

comparison, Z, p_values, adj_p_values = hochberg_test(alg_list, control='a1')

print('HOCHBERG POST-HOC')
print('Z', Z)
print('p_values', p_values)
print('adj_p_values', adj_p_values)

comparison, Z, p_values, adj_p_values = li_test(alg_list, control='a1')

print('LI POST-HOC')
print('Z', Z)
print('p_values', p_values)
print('adj_p_values', adj_p_values)

