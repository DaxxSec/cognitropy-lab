# Tools & Techniques Reference

## Statistical Analysis Tools

### Python (Primary Data Analysis)
```python
# Benford's Law analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def benfords_test(amounts):
    """Compute Benford's Law first-digit distribution."""
    first_digits = amounts[amounts > 0].apply(lambda x: int(str(x)[0]))
    actual = first_digits.value_counts(normalize=True).sort_index()
    expected = {d: np.log10(1 + 1/d) for d in range(1, 10)}
    
    results = pd.DataFrame({
        'digit': range(1, 10),
        'actual_%': [actual.get(d, 0) * 100 for d in range(1, 10)],
        'expected_%': [expected[d] * 100 for d in range(1, 10)]
    })
    
    # Z-statistic for each digit
    n = len(first_digits)
    results['z_stat'] = abs(results['actual_%']/100 - results['expected_%']/100) / \
                        np.sqrt(results['expected_%']/100 * (1 - results['expected_%']/100) / n)
    results['flag'] = results['z_stat'] > 1.96
    return results

# Duplicate payment detection
def find_duplicates(df, vendor_col, amount_col, date_col, days_window=3):
    """Find potential duplicate payments within a date window."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df_sorted = df.sort_values([vendor_col, amount_col, date_col])
    
    duplicates = []
    for (vendor, amount), group in df_sorted.groupby([vendor_col, amount_col]):
        dates = group[date_col].tolist()
        for i, d1 in enumerate(dates):
            for d2 in dates[i+1:]:
                if (d2 - d1).days <= days_window:
                    duplicates.append((vendor, amount, d1, d2))
    return pd.DataFrame(duplicates, columns=['vendor', 'amount', 'date1', 'date2'])
```

### Excel / Google Sheets
- COUNTIFS for duplicate detection
- VLOOKUP/XLOOKUP for vendor cross-referencing
- Pivot tables for summarizing by vendor, GL account, time period
- Conditional formatting for threshold highlighting

### ACL / Galvanize (IDEA)
Industry-standard audit data analytics software. Commands available in CLAUDE.md workflow guidance:
- `BENFORD` — built-in Benford's analysis
- `DUPLICATES` — configurable duplicate detection
- `GAPS` — sequence gap detection
- `STRATIFY` — amount stratification with statistics
- `JOIN` — cross-file matching (e.g., payroll vs. HR)

---

## Open-Source Intelligence (OSINT) Tools for Entity Research

| Tool | Use Case | URL |
|---|---|---|
| OpenCorporates | Corporate registry search, 140+ jurisdictions | opencorporates.com |
| SEC EDGAR Full-Text Search | 10-K/Q filings, insider transactions | efts.sec.gov |
| OFAC Search | SDN/consolidated sanctions list | sanctionssearch.ofac.treas.gov |
| FinCEN BOI Search | Beneficial ownership (law enforcement) | fincen.gov/boi |
| PACER | Federal court records | pacer.gov |
| ProPublica Nonprofit Explorer | 990 filings for nonprofits | projects.propublica.org/nonprofits |
| Sqoop | SEC filing search and alerts | sqoop.com |

---

## Blockchain Analysis Tools

| Tool | Type | Strengths |
|---|---|---|
| Etherscan / blockchain.info | Free explorer | Transaction history, address labels |
| Breadcrumbs | Free (limited) | Visual flow mapping |
| Chainalysis Reactor | Commercial | Advanced clustering, sanctions screening |
| Elliptic | Commercial | Risk scoring, VASP identification |
| CipherTrace | Commercial | DeFi exposure analysis |
| Crystal | Commercial | Exchange attribution |

---

## Document Analysis

### PDF Extraction
```bash
# Extract text from financial report PDF
pdftotext -layout annual_report.pdf output.txt
# Or via Python:
# pip install pdfplumber
import pdfplumber
with pdfplumber.open("filing.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
        tables = page.extract_tables()
```

### OCR for scanned documents
```bash
tesseract invoice_scan.jpg output -l eng pdf
```

---

## Visualization

### Transaction Flow Diagrams
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge("Entity A", "Entity B", amount=50000)
G.add_edge("Entity B", "Entity C", amount=49500)
G.add_edge("Entity C", "Bank Account X", amount=49000)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        arrows=True, edge_color='gray')
plt.savefig("flow_diagram.png")
```

### Benford's Law Chart
```python
import matplotlib.pyplot as plt

digits = range(1, 10)
expected = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
actual = [...]  # from analysis

x = range(len(digits))
plt.bar([i - 0.2 for i in x], expected, width=0.4, label='Expected (Benford)', alpha=0.7)
plt.bar([i + 0.2 for i in x], actual, width=0.4, label='Actual', alpha=0.7)
plt.xticks(x, digits)
plt.xlabel('First Digit')
plt.ylabel('Frequency (%)')
plt.title("Benford's Law Analysis")
plt.legend()
plt.savefig("benfords_chart.png")
```

---

## Data Formats Expected

| Source | Typical Format | Key Fields |
|---|---|---|
| General Ledger export | CSV/XLSX | date, journal_entry_id, account, debit, credit, preparer, description |
| AP transaction file | CSV/XLSX | invoice_date, vendor_id, invoice_number, amount, payment_date, check_number |
| Payroll export | CSV/XLSX | employee_id, name, ssn_last4, department, amount, bank_account, pay_period |
| Vendor master | CSV/XLSX | vendor_id, name, address, phone, ein, bank_routing, bank_account, added_date |
| Bank statement | OFX/CSV/PDF | date, description, amount, balance |
| Corporate filing | PDF/XBRL | Varies by regulator |
