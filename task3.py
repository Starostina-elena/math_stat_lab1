import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

theta_0 = 30
sigma = 37 ** 0.5
sample_sizes = [5, 10, 50, 100, 500, 1000]

estimations = {n: [] for n in sample_sizes}

for n in sample_sizes:
    for _ in range(1000):
        sample = np.random.normal(theta_0, sigma, size=n)
        theta_hat = np.mean(sample)
        estimations[n].append(theta_hat)

df = pd.DataFrame([(n, theta) for n in sample_sizes for theta in estimations[n]],
                  columns=['Sample Size', 'Theta Hat'])
print(df.groupby("Sample Size")["Theta Hat"].describe())

plt.figure(figsize=(12, 6))
for i, n in enumerate(sample_sizes, 1):
    plt.subplot(2, 3, i)
    sns.histplot(estimations[n], bins=20, kde=True)
    plt.title(f"n = {n}")
    plt.axvline(theta_0, color='red', linestyle='dashed', label=r'$\theta_0$')
    plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x="Sample Size", y="Theta Hat", data=df)
plt.title("Box-plot оценки при разном n")

plt.subplot(1, 2, 2)
sns.violinplot(x="Sample Size", y="Theta Hat", data=df)
plt.title("Violin-plot оценки при разном n")

plt.tight_layout()
plt.show()
