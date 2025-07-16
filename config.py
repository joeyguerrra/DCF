# config.py
DCF_CONFIG = {
    "revenue": 100000000,        # Year 0 revenue
    "revenue_growth_rate": 0.08, # Annual revenue growth
    "ebit_margin": 0.15,         # EBIT as % of revenue
    "tax_rate": 0.21,            # Corporate tax rate
    "depreciation_pct": 0.04,    # Depreciation as % of revenue
    "capex_pct": 0.05,           # CapEx as % of revenue
    "change_in_nwc_pct": 0.02,   # ΔNWC as % of revenue
    "wacc": 0.10,                # Discount rate
    "terminal_growth_rate": 0.03,# Long-term growth
    "projection_years": 5,       # Number of forecast years
    "net_debt": 20000000         # Net debt (debt - cash)
}
