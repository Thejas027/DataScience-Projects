import numpy as np

def roll_dice(num_rolls):
    rolls = np.random.randint(1,7,size=num_rolls)
    return rolls

def dice_vector(rolls):
    vector = np.zeros(6)
    
    for r in rolls:
        vector[r-1] +=1
    return vector



rolls_50 = roll_dice(50)
rolls_5000 = roll_dice(5000)

vec_50 = dice_vector(rolls_50)
vec_5000 = dice_vector(rolls_5000)

#Each index represents a dice face (0 = face 1, 1 = face 2, etc.)
# The values show how many times each face appeared

print("Dice vector (50 rolls):", vec_50)
print("Dice vector (5000 rolls):", vec_5000)

#Adding cosine similarity 
def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

ideal = np.ones(6)

cos_50 = cosine_similarity(vec_50, ideal)
cos_5000 = cosine_similarity(vec_5000, ideal)

print("Cosine similarity (50 rolls):", cos_50)
print("Cosine similarity (5000 rolls):", cos_5000)