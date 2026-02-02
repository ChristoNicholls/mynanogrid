#!/usr/bin/env python3
import json

# Load the current design
with open('/home/sandbox/solar_design_data.json', 'r') as f:
    data = json.load(f)

# Target: R50,000 including VAT
# That means: R50,000 / 1.15 = R43,478.26 excluding VAT

# Adjust costs to meet R50k target
# Reduce battery from 3 modules to 2 modules (10.24 kWh)
# This still provides 15+ kWh daily capacity with PV generation

# Update design
data['design']['battery']['num_modules'] = 2
data['design']['battery']['total_capacity_kwh'] = 10.24
data['design']['battery']['usable_capacity_kwh'] = 9.22

# Update performance
data['design']['performance']['battery_usable_kwh'] = 9.22
data['design']['performance']['total_daily_capacity_kwh'] = 18.5
data['design']['performance']['target_daily_load_kwh'] = 15.0

# Recalculate costs
# Battery: 2 x R4,300 = R8,600 (was R12,900) - saves R4,300
data['costs']['capex']['battery']['quantity'] = 2
data['costs']['capex']['battery']['total'] = 8600
data['costs']['capex']['battery']['description'] = "2x Huawei LUNA2000 5.12kWh LiFePO4 Battery Modules"

# Recalculate totals
capex_total = sum(item['total'] for item in data['costs']['capex'].values())
support_total = data['costs']['support_total']
installation_total = data['costs']['installation_total']
professional_total = data['costs']['professional_total']

subtotal = capex_total + support_total + installation_total + professional_total
vat = subtotal * 0.15
grand_total = subtotal + vat

data['costs']['capex_total'] = capex_total
data['costs']['subtotal'] = subtotal
data['costs']['vat'] = vat
data['costs']['grand_total'] = grand_total
data['costs']['variance'] = 50000 - grand_total
data['costs']['variance_percentage'] = round(((50000 - grand_total) / 50000) * 100, 2)

# Update category summary
data['costs']['category_summary']['Major Equipment (CAPEX)'] = capex_total

# Save updated design
with open('/home/sandbox/solar_design_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated Design:")
print(f"Battery: {data['design']['battery']['total_capacity_kwh']} kWh ({data['design']['battery']['num_modules']} modules)")
print(f"Total Daily Capacity: {data['design']['performance']['total_daily_capacity_kwh']} kWh/day")
print(f"\nUpdated Costs:")
print(f"CAPEX: R{capex_total:,.2f}")
print(f"Subtotal: R{subtotal:,.2f}")
print(f"VAT: R{vat:,.2f}")
print(f"Grand Total: R{grand_total:,.2f}")
print(f"Budget Variance: R{data['costs']['variance']:,.2f} ({data['costs']['variance_percentage']:+.1f}%)")
