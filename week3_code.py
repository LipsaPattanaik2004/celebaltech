import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.title("Scatterplot: Sepal Length vs. Petal Length")
plt.savefig("scatterplot_sepal_vs_petal.png")  
plt.show()

plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x="species", y="sepal_width")
plt.title("Violin Plot of Sepal Width Across Species")
plt.savefig("violinplot_sepal_width.png")  
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=df, x="species", y="sepal_length", ax=axes[0])
axes[0].set_title("Boxplot of Sepal Length Across Species")
sns.heatmap(df.drop(columns=["species"]).corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1])
axes[1].set_title("Heatmap of Feature Correlations")

plt.tight_layout()
plt.savefig("boxplot_heatmap_layout.png") 
plt.show()

df.drop(columns=["species"]).hist(figsize=(10, 6), bins=20)
plt.suptitle("Feature Distribution Histograms")
plt.savefig("feature_histograms.png") 
plt.show()
