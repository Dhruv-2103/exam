import matplotlib.pyplot as plt
import numpy as np
Country = ('USA', 'China', 'India')
Gender_counts = {'Male': np.array([73, 34, 61]),'Female': np.array([27, 66, 48]),}
width = 0.6
fig, ax = plt.subplots()
bottom = np.zeros(3)
for Gender, gender_count in Gender_counts.items():
    p = ax.bar(Country, gender_count, width, label=Gender, bottom=bottom)
    bottom += gender_count

ax.bar_label(p, label_type='center')
ax.set_title('Number of People by Gender')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
ax.legend()
plt.show()
