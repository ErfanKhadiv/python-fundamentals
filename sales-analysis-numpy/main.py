import numpy as np

# ==========================================================
# Sample Dataset
# Rows    -> Months
# Columns -> Products
# ==========================================================

MONTHLY_SALES = np.array([
    [3200, 4100, 1800, 2600, 950],
    [3400, 3900, 2100, 2700, 1100],
    [3600, 4500, 2500, 2800, 1200],
    [3100, 4300, 2200, 3000, 1300],
    [4000, 4700, 2700, 3100, 1500],
    [4200, 4900, 2900, 3300, 1700],
    [4500, 5100, 3100, 3500, 1800],
    [4700, 5300, 3300, 3700, 2000],
    [4400, 5000, 3000, 3400, 1900],
    [4300, 4800, 2800, 3200, 1750],
    [3900, 4600, 2600, 3000, 1600],
    [4100, 5200, 3200, 3600, 2100]
])

MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

PRODUCTS = [
    "Laptop",
    "Phone",
    "Tablet",
    "Monitor",
    "Keyboard"
]


def basic_report(sales):
    """Display overall statistics."""

    print("========== BASIC REPORT ==========")

    print(f"Annual Sales : {sales.sum():,}")
    print(f"Average Sale : {sales.mean():,.2f}")
    print(f"Maximum Sale : {sales.max():,}")
    print(f"Minimum Sale : {sales.min():,}")
    print(f"Median       : {np.median(sales):,}")
    print(f"Std          : {sales.std():,.2f}")


def monthly_report(sales):
    """Display statistics for each month."""

    monthly_total = sales.sum(axis=1)

    print("\n========== MONTHLY REPORT ==========")

    print(
        f"Best Month : "
        f"{MONTHS[monthly_total.argmax()]} ({monthly_total.max():,})"
    )

    print(
        f"Worst Month: "
        f"{MONTHS[monthly_total.argmin()]} ({monthly_total.min():,})\n"
    )

    for i, month in enumerate(MONTHS):
        print(f"--- {month} ---")
        print(f"Total Sales : {monthly_total[i]:,}")
        print(f"Average     : {sales[i].mean():,.2f}\n")


def product_report(sales):
    """Display statistics for each product."""

    product_total = sales.sum(axis=0)
    product_mean = sales.mean(axis=0)
    product_max = sales.max(axis=0)
    product_min = sales.min(axis=0)

    print("========== PRODUCT REPORT ==========")

    print(
        f"Best Product : "
        f"{PRODUCTS[product_total.argmax()]} ({product_total.max():,})"
    )

    print(
        f"Worst Product: "
        f"{PRODUCTS[product_total.argmin()]} ({product_total.min():,})\n"
    )

    for i, product in enumerate(PRODUCTS):
        print(f"--- {product} ---")
        print(f"Annual Sales : {product_total[i]:,}")
        print(f"Average      : {product_mean[i]:,.2f}")
        print(f"Maximum      : {product_max[i]:,}")
        print(f"Minimum      : {product_min[i]:,}\n")


def filtering_report(sales):
    """Filtering examples."""

    print("========== FILTERING REPORT ==========")

    print("Sales > 4000")
    print(sales[sales > 4000])

    print("\nSales < 1000")
    print(sales[sales < 1000])

    percentage = (sales > 3000).sum() / sales.size * 100

    print(f"\nSales > 3000 : {percentage:.2f}%")


def sorting_report(sales):
    """Sorting examples."""

    print("\n========== SORTING REPORT ==========")

    print("Products (Highest → Lowest)")

    product_total = sales.sum(axis=0)

    for index in product_total.argsort()[::-1]:
        print(PRODUCTS[index])

    print("\nMonths (Highest → Lowest)")

    monthly_total = sales.sum(axis=1)

    for index in monthly_total.argsort()[::-1]:
        print(MONTHS[index])


def broadcasting_report(sales):
    """Broadcasting example."""

    print("\n========== BROADCASTING REPORT ==========")

    increase_percent = np.array([5, 8, 12, 3, 20])

    new_sales = sales * (1 + increase_percent / 100)

    print(new_sales)


def profit_report(sales):
    """Calculate monthly and product profit."""

    print("\n========== PROFIT REPORT ==========")

    cost = np.array([2500, 1800, 1200, 1000, 250])

    profit = sales - cost

    monthly_profit = profit.sum(axis=1)
    product_profit = profit.sum(axis=0)

    print(f"Annual Profit : {profit.sum():,}\n")

    print("Monthly Profit")

    for month, value in zip(MONTHS, monthly_profit):
        print(f"{month:<10} {value:>8,}")

    print(
        f"\nHighest Monthly Profit : "
        f"{MONTHS[monthly_profit.argmax()]} "
        f"({monthly_profit.max():,})"
    )

    print("\nProduct Profit")

    for product, value in zip(PRODUCTS, product_profit):
        print(f"{product:<10} {value:>8,}")

    print(
        f"\nHighest Product Profit : "
        f"{PRODUCTS[product_profit.argmax()]} "
        f"({product_profit.max():,})"
    )


def main():
    basic_report(MONTHLY_SALES)
    monthly_report(MONTHLY_SALES)
    product_report(MONTHLY_SALES)
    filtering_report(MONTHLY_SALES)
    sorting_report(MONTHLY_SALES)
    broadcasting_report(MONTHLY_SALES)
    profit_report(MONTHLY_SALES)


if __name__ == "__main__":
    main()
