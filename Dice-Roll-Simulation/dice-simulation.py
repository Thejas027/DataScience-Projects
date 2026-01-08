import numpy as np
import matplotlib.pyplot as plt

num_rolls = 1000000

dice_rolls = np.random.randint(1,7,size=num_rolls)

print("First 10 dice rolls:")
print(dice_rolls[:10])

mean_value = np.mean(dice_rolls)
variance = np.var(dice_rolls)
std_dev = np.std(dice_rolls)

print("Mean : ", mean_value)
print("Variance : " , variance)
print("Standard Deviation : ",std_dev)


# Probablity of each outcome
values,counts = np.unique(dice_rolls , return_counts=True)
probablities = counts / num_rolls

for v,p in zip(values,probablities):
    print(f"Probablity of {v} : {p:.3f}")
    
# Visualization of data 
plt.hist(dice_rolls,bins=6)
plt.title("Dice Roll Distributation")
plt.xlabel("Dice value")
plt.ylabel("Frequency")
plt.show()

print("\nINSIGHTS:")
print("1. Mean approaches 3.5 as number of rolls increases.")
print("2. Dice values are uniformly distributed.")
print("3. Variance shows spread around the mean.")
