import numpy as np

score = np.array([85, 90, 78, 92, 88])

score = score.astype(float)

score1 = score + 5

shape = score.shape
ndim = score.ndim
size = score.size
itemsize = score.itemsize
dtype = score.dtype
sorted_score = np.sort(score)

indices_85_plus = np.where(score >= 85)


min_score = score.min()
max_score = score.max()
std_dev = score.std()
variance = score.var()
total_sum = score.sum()
mean_score = score.mean()


print("Score [:2]:", score[:2])      
print("Score [-3:-1]:", score[-3:-1]) 
print("Score [1:4]:", score[1:4])     


print("Original score array:", score)
print("Score array with +5:", score1)
print("Shape:", shape)
print("Number of dimensions:", ndim)
print("Size:", size)
print("Item size:", itemsize)
print("Data type:", dtype)
print("Sorted score array:", sorted_score)
print("Indices with scores >= 85:", indices_85_plus)
print("Minimum score:", min_score)
print("Maximum score:", max_score)
print("Standard deviation:", std_dev)
print("Variance:", variance)
print("Sum of scores:", total_sum)
print("Mean of scores:", mean_score)