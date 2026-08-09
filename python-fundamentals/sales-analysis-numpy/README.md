# Monthly Sales Analysis (NumPy)

Analyzes a 12-month × 5-product sales matrix using NumPy — no pandas, just core array operations.

## Reports generated
- **Basic** — sum, mean, max, min, median, std across all sales
- **Monthly** — best/worst month, per-month totals and averages
- **Product** — best/worst product, per-product totals/mean/max/min
- **Filtering** — boolean-mask filtering (`sales > 4000`, `sales < 1000`) and threshold percentage
- **Sorting** — products and months ranked by total sales (`argsort`)
- **Broadcasting** — applies a different % increase per product across the whole matrix
- **Profit** — subtracts per-product cost (broadcast across all months) and reports monthly/product profit

## Run
```bash
pip install numpy
python main.py
```

## What it demonstrates
Vectorized operations over `axis=0`/`axis=1`, boolean masking, `argsort`/`argmax`/`argmin`, and broadcasting a 1D array against a 2D one — the NumPy patterns that show up constantly in ML preprocessing.
