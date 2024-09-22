import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/covid-geography/mmsa-icu-beds.csv"
)
df = df.filter(pl.col("icu_beds") != "NA").with_columns(
    pl.col("icu_beds").cast(pl.Int64)
)


# summary statistics (mean, median, standard deviation)
def statistics(p=False):
    icu_beds = df["icu_beds"]
    bed_mean = icu_beds.mean()
    bed_median = icu_beds.median()
    bed_std = icu_beds.std()
    if p:
        summary_stats = (
            f"Mean = {bed_mean}, Median = {bed_median}, Standard Deviation = {bed_std}"
        )
        print(summary_stats)
    return bed_mean, bed_median, bed_std


# count columns and rows for test
def count_col():
    num_col = len(df.columns)
    return num_col


def count_row():
    num_row = len(df)
    return num_row


# visualization
def create_hist():
    plt.figure(figsize=(10, 6))
    plt.hist(df["icu_beds"].to_list(), bins=25, color="orange", edgecolor="black")
    plt.title("ICU Beds Histogram", fontsize=16)
    plt.xlabel("Number of ICU Beds in the Area", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.savefig("bed_hist.png")


# summary report
def save_report(output_file="summary_report.md", image_file="bed_hist.png"):
    bed_mean, bed_median, bed_std = statistics()
    summary_stats = (
        f"Mean = {bed_mean}, Median = {bed_median}, Standard Deviation = {bed_std}"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Summary Report\n\n")
        f.write("## Summary Statistics\n\n")
        f.write(f"{summary_stats}\n\n")
        f.write("## Visualization: Histogram\n\n")
        f.write(f"![Histogram](./{image_file})\n\n")

    print(f"Summary report (histogram included) saved to {output_file}")


if __name__ == "__main__":
    statistics(True)
    create_hist()
    save_report()
