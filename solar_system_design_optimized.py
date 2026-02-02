#!/usr/bin/env python3
"""
Solar System Design Calculator - R50k Solution (Budget Optimized)
15-20 kWh Base Load with PV, Huawei Inverter, and BESS
Author: UtCS - C. Nicholls
Date: 2026-02-02
"""

import json
from datetime import datetime

class SolarSystemDesign:
    def __init__(self):
        self.budget = 50000  # R50,000
        self.target_daily_energy = 17.5  # kWh (midpoint of 15-20 kWh)
        self.design = {}
        self.costs = {}
        
    def calculate_system_sizing(self):
        """Calculate PV, inverter, and battery sizing - Budget optimized"""
        
        # Battery sizing: Optimized for budget
        # Using 3x 5.12 kWh modules = 15.36 kWh total
        battery_modules = 3
        total_battery_capacity = battery_modules * 5.12  # 15.36 kWh
        
        # PV sizing: 8 panels x 550W = 4.4 kW
        panel_wattage = 550  # W
        num_panels = 8
        total_pv_capacity = (num_panels * panel_wattage) / 1000  # 4.4 kW
        
        # Inverter: Huawei SUN2000-5KTL-L1
        inverter_capacity = 5  # kW
        
        self.design = {
            'pv': {
                'panel_wattage': panel_wattage,
                'num_panels': num_panels,
                'total_capacity_kw': total_pv_capacity,
                'brand': 'JA Solar JAM72S30',
                'type': 'Monocrystalline PERC',
                'efficiency': '21.3%',
                'dimensions': '2278 x 1134 x 35 mm'
            },
            'inverter': {
                'model': 'Huawei SUN2000-5KTL-L1',
                'capacity_kw': inverter_capacity,
                'type': 'Hybrid String Inverter',
                'max_efficiency': '98.4%',
                'mppt_trackers': 2,
                'phases': 'Single Phase',
                'warranty': '10 years'
            },
            'battery': {
                'model': 'Huawei LUNA2000-5-S0',
                'num_modules': battery_modules,
                'module_capacity_kwh': 5.12,
                'total_capacity_kwh': total_battery_capacity,
                'usable_capacity_kwh': total_battery_capacity * 0.9,  # 90% DoD
                'type': 'Lithium Iron Phosphate (LiFePO4)',
                'cycles': '6000 @ 90% DoD',
                'warranty': '10 years'
            },
            'performance': {
                'daily_generation_kwh': round(total_pv_capacity * 4.5 * 0.75, 2),
                'daily_load_kwh': 15.0,  # Conservative estimate
                'autonomy_days': round(total_battery_capacity * 0.9 / 15.0, 2),
                'peak_sun_hours': 4.5,
                'system_efficiency': '75%'
            }
        }
        
        return self.design
    
    def calculate_costs(self):
        """Calculate detailed cost breakdown - Budget optimized"""
        
        # CAPEX - Equipment Costs
        capex = {
            'pv_panels': {
                'description': f"{self.design['pv']['num_panels']}x {self.design['pv']['panel_wattage']}W JA Solar Panels",
                'unit_cost': 1750,  # R per panel (optimized pricing)
                'quantity': self.design['pv']['num_panels'],
                'total': 1750 * self.design['pv']['num_panels']
            },
            'inverter': {
                'description': f"{self.design['inverter']['model']} 5kW Hybrid Inverter",
                'unit_cost': 11800,  # Optimized pricing
                'quantity': 1,
                'total': 11800
            },
            'battery': {
                'description': f"{self.design['battery']['num_modules']}x Huawei LUNA2000-5kWh Battery Modules",
                'unit_cost': 4650,  # R per module (optimized)
                'quantity': self.design['battery']['num_modules'],
                'total': 4650 * self.design['battery']['num_modules']
            },
            'smart_meter': {
                'description': 'Landis+Gyr E460 4-Quadrant Bi-Directional Smart Meter',
                'unit_cost': 2950,
                'quantity': 1,
                'total': 2950
            }
        }
        
        capex_total = sum(item['total'] for item in capex.values())
        
        # Support Equipment
        support_equipment = {
            'wifi_router': {
                'description': 'Industrial WiFi Router (Outdoor Rated)',
                'unit_cost': 750,
                'quantity': 1,
                'total': 750
            },
            'cctv_camera': {
                'description': 'WiFi CCTV Camera (Inverter Monitoring)',
                'unit_cost': 1100,
                'quantity': 1,
                'total': 1100
            },
            'mounting_structure': {
                'description': 'Aluminum Mounting Rails & Clamps (8 panels)',
                'unit_cost': 420,
                'quantity': 8,
                'total': 3360
            },
            'ac_dc_protection': {
                'description': 'AC/DC Surge Protection, Isolators, Breakers',
                'unit_cost': 2400,
                'quantity': 1,
                'total': 2400
            },
            'cabling': {
                'description': 'Solar DC Cable (4mm²), AC Cable (6mm²), 40m total',
                'unit_cost': 42,  # per meter
                'quantity': 40,
                'total': 1680
            },
            'connectors': {
                'description': 'MC4 Connectors, Cable Glands, Terminals',
                'unit_cost': 580,
                'quantity': 1,
                'total': 580
            },
            'earthing': {
                'description': 'Earthing Kit (Rods, Clamps, Cable)',
                'unit_cost': 750,
                'quantity': 1,
                'total': 750
            },
            'conduit': {
                'description': 'PVC Conduit & Fittings (25mm, 15m)',
                'unit_cost': 32,  # per meter
                'quantity': 15,
                'total': 480
            }
        }
        
        support_total = sum(item['total'] for item in support_equipment.values())
        
        # Installation Costs
        installation = {
            'pv_installation': {
                'description': 'PV Panel Installation (Roof Mounting, Wiring)',
                'unit_cost': 320,  # per panel
                'quantity': self.design['pv']['num_panels'],
                'total': 320 * self.design['pv']['num_panels']
            },
            'inverter_installation': {
                'description': 'Inverter & Battery Installation (Wall Mount, Config)',
                'unit_cost': 2200,
                'quantity': 1,
                'total': 2200
            },
            'electrical_work': {
                'description': 'DB Board Modifications, AC Wiring, Testing',
                'unit_cost': 2800,
                'quantity': 1,
                'total': 2800
            },
            'smart_meter_installation': {
                'description': 'E460 Smart Meter Installation & Configuration',
                'unit_cost': 1000,
                'quantity': 1,
                'total': 1000
            },
            'cctv_installation': {
                'description': 'CCTV Camera Installation & WiFi Setup',
                'unit_cost': 700,
                'quantity': 1,
                'total': 700
            },
            'router_setup': {
                'description': 'WiFi Router Installation & Network Config',
                'unit_cost': 450,
                'quantity': 1,
                'total': 450
            },
            'commissioning': {
                'description': 'System Testing, Commissioning & Training',
                'unit_cost': 1200,
                'quantity': 1,
                'total': 1200
            }
        }
        
        installation_total = sum(item['total'] for item in installation.values())
        
        # Professional Services
        professional_services = {
            'design_engineering': {
                'description': 'Electrical Design & Engineering (COC Prep)',
                'unit_cost': 1500,
                'quantity': 1,
                'total': 1500
            },
            'coc': {
                'description': 'Certificate of Compliance (CoC)',
                'unit_cost': 950,
                'quantity': 1,
                'total': 950
            }
        }
        
        professional_total = sum(item['total'] for item in professional_services.values())
        
        # Calculate totals
        subtotal = capex_total + support_total + installation_total + professional_total
        vat = subtotal * 0.15
        grand_total = subtotal + vat
        
        self.costs = {
            'capex': capex,
            'capex_total': capex_total,
            'support_equipment': support_equipment,
            'support_total': support_total,
            'installation': installation,
            'installation_total': installation_total,
            'professional_services': professional_services,
            'professional_total': professional_total,
            'subtotal': subtotal,
            'vat': vat,
            'grand_total': grand_total,
            'budget': self.budget,
            'variance': self.budget - grand_total
        }
        
        return self.costs
    
    def generate_summary(self):
        """Generate system summary"""
        summary = {
            'project_info': {
                'title': 'R50k Solar PV + BESS Solution',
                'engineer': 'C. Nicholls',
                'company': 'UtCS (Pty) Ltd',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'classification': 'CONFIDENTIAL'
            },
            'design': self.design,
            'costs': self.costs
        }
        return summary
    
    def save_to_json(self, filename):
        """Save design to JSON file"""
        summary = self.generate_summary()
        with open(filename, 'w') as f:
            json.dump(summary, f, indent=2)
        return filename

# Main execution
if __name__ == "__main__":
    print("=" * 80)
    print("SOLAR SYSTEM DESIGN CALCULATOR - R50k SOLUTION (OPTIMIZED)")
    print("Engineer: C. Nicholls | Company: UtCS (Pty) Ltd")
    print("=" * 80)
    print()
    
    designer = SolarSystemDesign()
    
    print("Step 1: Calculating system sizing...")
    design = designer.calculate_system_sizing()
    print(f"✓ PV System: {design['pv']['total_capacity_kw']} kW ({design['pv']['num_panels']} panels)")
    print(f"✓ Inverter: {design['inverter']['model']} - {design['inverter']['capacity_kw']} kW")
    print(f"✓ Battery: {design['battery']['total_capacity_kwh']} kWh ({design['battery']['num_modules']} modules)")
    print(f"✓ Daily Generation: {design['performance']['daily_generation_kwh']} kWh")
    print()
    
    print("Step 2: Calculating detailed costs...")
    costs = designer.calculate_costs()
    print(f"✓ CAPEX (Equipment): R {costs['capex_total']:,.2f}")
    print(f"✓ Support Equipment: R {costs['support_total']:,.2f}")
    print(f"✓ Installation: R {costs['installation_total']:,.2f}")
    print(f"✓ Professional Services: R {costs['professional_total']:,.2f}")
    print(f"✓ Subtotal: R {costs['subtotal']:,.2f}")
    print(f"✓ VAT (15%): R {costs['vat']:,.2f}")
    print(f"✓ GRAND TOTAL: R {costs['grand_total']:,.2f}")
    print(f"✓ Budget Variance: R {costs['variance']:,.2f}")
    print()
    
    print("Step 3: Saving design data...")
    json_file = designer.save_to_json('/home/sandbox/solar_design_data.json')
    print(f"✓ Design saved to: {json_file}")
    print()
    
    print("=" * 80)
    print("DESIGN COMPLETE")
    print("=" * 80)
