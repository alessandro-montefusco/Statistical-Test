# example of the mann-whitney u test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import mannwhitneyu

# seed the random number generator
seed(1342)

# generate two independent samples
data1 = 50 + (rand(100) * 100)
data2 = 51 + (rand(100) * 100)

print(data1)

# compare samples
stat, p = mannwhitneyu(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')