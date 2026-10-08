import pandas as pd
import matplotlib.pyplot as plt

data = input("Please provide the .csv file name for gene expression analysis: (with extension): ")
df = pd.read_csv(data)

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

df = df.set_index("Gene")

df["Mean_Expression"] = df.mean(axis=1)

top10 = df.sort_values(
    by="Mean_Expression",
    ascending=False
).head(10)

print("\nTop 10 Highly Expressed Genes:")
print(top10[["Mean_Expression"]])

top10[["Mean_Expression"]].to_csv("top_10_expressed_genes.csv")

plt.figure(figsize=(10, 6))

plt.bar(
    top10.index,
    top10["Mean_Expression"]
)

plt.xlabel("Gene")
plt.ylabel("Mean Expression")
plt.title("Top 10 Most Highly Expressed Genes")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_genes.png", dpi=300)
plt.show()