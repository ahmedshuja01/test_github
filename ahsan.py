import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Set style for beautiful plots
plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# ===================================================================
#  CHAPTER 1: Setting the Stage - "Two Tribes in a Digital World"
# ===================================================================

print(" CHAPTER 1: Creating Our Digital World")
print("=" * 50)

#  The Random Seed: Ensuring our story is reproducible
np.random.seed(42)
print(" Random seed set to 42 - our story will be consistent every time!")

#  Creating the Blue Tribe (Class 0)
print("\n Creating the Blue Tribe:")
X0 = np.random.randn(50, 2) * 1.0 + [0, 0]  # Centered at origin, tighter spread
print(f"   - Population: 50 members")
print(f"   - Territory: Centered around (0, 0)")
print(f"   - Lifestyle: Conservative (smaller variance = 1.0)")

#  Creating the Red Tribe (Class 1) 
print("\n Creating the Red Tribe:")
X1 = np.random.randn(50, 2) * 1.5 + [1.5, 1.5]  # Northeast location, wider spread
print(f"   - Population: 50 members") 
print(f"   - Territory: Centered around (1.5, 1.5)")
print(f"   - Lifestyle: Adventurous (larger variance = 1.5)")
