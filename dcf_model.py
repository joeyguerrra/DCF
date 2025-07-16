# dcf_model.py
from config import DCF_CONFIG

def project_fcf(config):
    revenue = config["revenue"]
    fcf_list = []

    for year in range(1, config["projection_years"] + 1):
        revenue *= (1 + config["revenue_growth_rate"])
        ebit = revenue * config["ebit_margin"]
        nopat = ebit * (1 - config["tax_rate"])
        depreciation = revenue * config["depreciation_pct"]
        capex = revenue * config["capex_pct"]
        change_in_nwc = revenue * config["change_in_nwc_pct"]
        fcf = nopat + depreciation - capex - change_in_nwc
        fcf_list.append(fcf)

    return fcf_list, revenue

def calculate_dcf(fcf_list, revenue, config):
    wacc = config["wacc"]
    terminal_value = (fcf_list[-1] * (1 + config["terminal_growth_rate"])) / (wacc - config["terminal_growth_rate"])
    discount_factors = [(1 / (1 + wacc) ** year) for year in range(1, len(fcf_list) + 1)]
    discounted_fcfs = [fcf * df for fcf, df in zip(fcf_list, discount_factors)]
    pv_terminal_value = terminal_value / ((1 + wacc) ** len(fcf_list))

    enterprise_value = sum(discounted_fcfs) + pv_terminal_value
    equity_value = enterprise_value - config["net_debt"]

    return {
        "Enterprise Value": enterprise_value,
        "Equity Value": equity_value,
        "Per Year FCF": fcf_list
    }

if __name__ == "__main__":
    fcf_list, final_revenue = project_fcf(DCF_CONFIG)
    results = calculate_dcf(fcf_list, final_revenue, DCF_CONFIG)

    print("----- DCF Results -----")
    for k, v in results.items():
        if isinstance(v, list):
            for i, cash_flow in enumerate(v):
                print(f"Year {i+1} FCF: ${cash_flow:,.2f}")
        else:
            print(f"{k}: ${v:,.2f}")
