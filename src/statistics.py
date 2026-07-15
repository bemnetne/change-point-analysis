from statsmodels.tsa.stattools import adfuller


def adf_test(series):

    result = adfuller(series)

    print("=" * 50)
    print("Augmented Dickey-Fuller Test")
    print("=" * 50)

    print(f"ADF Statistic : {result[0]:.4f}")
    print(f"p-value       : {result[1]:.4f}")

    print("\nCritical Values")

    for key, value in result[4].items():
        print(f"{key}: {value:.4f}")

    if result[1] < 0.05:
        print("\nSeries is stationary.")
    else:
        print("\nSeries is NOT stationary.")

    return result