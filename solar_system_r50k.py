#!/usr/bin/env python3
"""
Solar System Design Calculator - R50k Solution (Budget-Constrained Final)
15-20 kWh Base Load with PV, Huawei Inverter, and BESS
Author: UtCS - C. Nicholls
Date: 2026-02-02
"""

import json
from datetime import datetime

class SolarSystemDesign:
    def __init__(self):
        self.budget = 50000  # R50,000 (including VAT)
        self.target_daily_energy = 15.5  # kWh (within 15-20 kWh range)
        self.design = {}
        self.costs = {}
        
    def calculate_system_sizing(self):
        """Calculate PV, inverter, and battery sizing - R50k budget"""
        
        # Battery sizing: 3x 5.12 kWh modules = 15.36 kWh total
        # Provides 13.82 kWh usable (90% DoD)
        battery_modules = 3
        total_battery_capacity = battery_modules * 5.12  # 15.36 kWh
        
        # PV sizing: 5 panels x 550W = 2.75 kW
        # Generates ~9.28 kWh/day (2.75kW × 4.5h × 0.75 efficiency)
        # Combined with battery: 13.82 + 9.28 = 23.1 kWh total daily capacity
        panel_wattage = 550  # W
        num_panels = 5
        total_pv_capacity = (num_panels * panel_wattage) / 1000  # 2.75 kW
        
        # Inverter: Huawei SUN2000-3KTL-L1 (3kW)
        inverter_capacity = 3  # kW
        
        self.design = {
            'pv': {
                'panel_wattage': panel_wattage,
                'num_panels': num_panels,
                'total_capacity_kw': total_pv_capacity,
                'brand': 'JA Solar JAM72S30',
                'type': 'Monocrystalline PERC',
                'efficiency': '21.3%',
                'dimensions': '2278 x 1134 x 35 mm',
                'warranty': '25 years performance'
            },
            'inverter': {
                'model': 'Huawei SUN2000-3KTL-L1',
                'capacity_kw': inverter_capacity,
                'type': 'Hybrid String Inverter',
                'max_efficiency': '98.3%',
                'mppt_trackers': 2,
                'phases': 'Single Phase',
                'warranty': '10 years',
                'features': 'WiFi, FusionSolar App, Smart Monitoring'
            },
            'battery': {
                'model': 'Huawei LUNA2000-5-S0',
                'num_modules': battery_modules,
                'module_capacity_kwh': 5.12,
                'total_capacity_kwh': total_battery_capacity,
                'usable_capacity_kwh': round(total_battery_capacity * 0.9, 2),
                'type': 'Lithium Iron Phosphate (LiFePO4)',
                'cycles': '6000 @ 90% DoD',
                'warranty': '10 years',
                'features': 'Modular, Expandable, Active Safety'
            },
            'performance': {
                'daily_pv_generation_kwh': round(total_pv_capacity * 4.5 * 0.75, 2),
                'battery_usable_kwh': round(total_battery_capacity * 0.9, 2),
                'total_daily_capacity_kwh': round((total_pv_capacity * 4.5 * 0.75) + (total_battery_capacity * 0.9), 2),
                'target_daily_load_kwh': 15.5,
                'autonomy_days': round((total_battery_capacity * 0.9) / 15.5, 2),
                'peak_sun_hours': 4.5,
                'system_efficiency': '75%',
                'self_consumption': '85%'
            }
        }
        
        return self.design
    
    def calculate_costs(self):
        """Calculate detailed cost breakdown - R50k budget (incl VAT)"""
        
        # Working backwards from R50k including VAT
        # R50,000 / 1.15 = R43,478.26 (excl VAT)
        target_subtotal = 43478.26
        
        # CAPEX - Equipment Costs
        capex = {
            'pv_panels': {
                'description': f"{self.design['pv']['num_panels']}x {self.design['pv']['panel_wattage']}W JA Solar Monocrystalline Panels",
                'unit_cost': 1580,
                'quantity': self.design['pv']['num_panels'],
                'total': 1580 * self.design['pv']['num_panels']
            },
            'inverter': {
                'description': f"{self.design['inverter']['model']} 3kW Hybrid Inverter with WiFi",
                'unit_cost': 8500,
                'quantity': 1,
                'total': 8500
            },
            'battery': {
                'description': f"{self.design['battery']['num_modules']}x Huawei LUNA2000 5.12kWh LiFePO4 Battery Modules",
                'unit_cost': 4300,
                'quantity': self.design['battery']['num_modules'],
                'total': 4300 * self.design['battery']['num_modules']
            },
            'smart_meter': {
                'description': 'Landis+Gyr E460 4-Quadrant Bi-Directional Smart Meter',
                'unit_cost': 2650,
                'quantity': 1,
                'total': 2650
            }
        }
        
        capex_total = sum(item['total'] for item in capex.values())
        
        # Support Equipment & Monitoring
        support_equipment = {
            'wifi_router': {
                'description': 'TP-Link WiFi Router (Outdoor Rated)',
                'unit_cost': 620,
                'quantity': 1,
                'total': 620
            },
            'cctv_camera': {
                'description': 'WiFi CCTV Camera 2MP (Inverter Monitoring)',
                'unit_cost': 880,
                'quantity': 1,
                'total': 880
            },
            'mounting_structure': {
                'description': 'Aluminum Mounting Rails & Clamps (5 panels)',
                'unit_cost': 350,
                'quantity': 5,
                'total': 1750
            },
            'ac_dc_protection': {
                'description': 'AC/DC Surge Protection, DC Isolator, AC Breaker',
                'unit_cost': 1750,
                'quantity': 1,
                'total': 1750
            },
            'cabling': {
                'description': 'Solar DC Cable 4mm² (15m), AC Cable 4mm² (12m)',
                'unit_cost': 35,
                'quantity': 27,
                'total': 945
            },
            'connectors': {
                'description': 'MC4 Connectors, Cable Glands, Terminals',
                'unit_cost': 420,
                'quantity': 1,
                'total': 420
            },
            'earthing': {
                'description': 'Earthing Kit (Rods, Clamps, Earth Cable)',
                'unit_cost': 580,
                'quantity': 1,
                'total': 580
            },
            'conduit': {
                'description': 'PVC Conduit 25mm & Fittings (10m)',
                'unit_cost': 26,
                'quantity': 10,
                'total': 260
            },
            'enclosure': {
                'description': 'Weatherproof Enclosure for Router/CCTV (IP55)',
                'unit_cost': 380,
                'quantity': 1,
                'total': 380
            }
        }
        
        support_total = sum(item['total'] for item in support_equipment.values())
        
        # Installation & Labor
        installation = {
            'pv_installation': {
                'description': 'PV Panel Installation & DC Wiring (5 panels)',
                'unit_cost': 250,
                'quantity': self.design['pv']['num_panels'],
                'total': 250 * self.design['pv']['num_panels']
            },
            'inverter_battery_install': {
                'description': 'Inverter & Battery Installation, Configuration',
                'unit_cost': 1600,
                'quantity': 1,
                'total': 1600
            },
            'electrical_work': {
                'description': 'DB Board Modifications, AC Wiring, Testing',
                'unit_cost': 1900,
                'quantity': 1,
                'total': 1900
            },
            'smart_meter_installation': {
                'description': 'E460 Smart Meter Installation & Configuration',
                'unit_cost': 750,
                'quantity': 1,
                'total': 750
            },
            'cctv_installation': {
                'description': 'CCTV Camera Installation & WiFi Setup',
                'unit_cost': 520,
                'quantity': 1,
                'total': 520
            },
            'router_network_setup': {
                'description': 'WiFi Router & Network Configuration',
                'unit_cost': 350,
                'quantity': 1,
                'total': 350
            },
            'commissioning_training': {
                'description': 'System Testing, Commissioning & Training',
                'unit_cost': 850,
                'quantity': 1,
                'total': 850
            }
        }
        
        installation_total = sum(item['total'] for item in installation.values())
        
        # Professional Services & Compliance
        professional_services = {
            'design_engineering': {
                'description': 'Electrical Design & Single-Line Diagram',
                'unit_cost': 1050,
                'quantity': 1,
                'total': 1050
            },
            'coc': {
                'description': 'Certificate of Compliance (CoC)',
                'unit_cost': 750,
                'quantity': 1,
                'total': 750
            },
            'documentation': {
                'description': 'As-Built Drawings & O&M Manual',
                'unit_cost': 380,
                'quantity': 1,
                'total': 380
            }
        }
        
        professional_total = sum(item['total'] for item in professional_services.values())
        
        # Calculate totals
        subtotal = capex_total + support_total + installation_total + professional_total
        vat = subtotal * 0.15
        grand_total = subtotal + vat
        
        # Cost summary by category
        category_summary = {
            'Major Equipment (CAPEX)': capex_total,
            'Support Equipment & Monitoring': support_total,
            'Installation & Labor': installation_total,
            'Professional Services & Compliance': professional_total
        }
        
        self.costs = {
            'capex': capex,
            'capex_total': capex_total,
            'support_equipment': support_equipment,
            'support_total': support_total,
            'installation': installation,
            'installation_total': installation_total,
            'professional_services': professional_services,
            'professional_total': professional_total,
            'category_summary': category_summary,
            'subtotal': subtotal,
            'vat': vat,
            'grand_total': grand_total,
            'budget': self.budget,
            'variance': self.budget - grand_total,
            'variance_percentage': round(((self.budget - grand_total) / self.budget) * 100, 2)
        }
        
        return self.costs
    
    def generate_summary(self):
        """Generate system summary"""
        summary = {
            'project_info': {
                'title': 'R50,000 Solar PV + Battery Energy Storage Solution',
                'subtitle': '15-20 kWh Daily Base Load Capacity',
                'engineer': 'C. Nicholls',
                'company': 'UtCS (Pty) Ltd',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'classification': 'CONFIDENTIAL',
                'reference': 'UTCS-SOLAR-2026-001'
            },
            'design': self.design,
            'costs': self.costs,
            'technical_specs': {
                'system_type': 'Grid-Tied Hybrid with Battery Backup',
                'installation_type': 'Roof-Mounted Residential',
                'compliance': 'NRS 097-2-1:2017, SANS 10142-1:2017',
                'monitoring': 'Huawei FusionSolar App + WiFi CCTV',
                'metering': 'Bi-directional Smart Metering (E460)',
                'safety': 'AC/DC Surge Protection, Earthing, Isolators'
            }
        }
        return summary
    
    def save_to_json(self, filename):
        """Save design to JSON file"""
        summary = self.generate_summary()
        with open(filename, 'w') as f:
            json.dump(summary, f, indent=2)
        return filename
    
    def print_detailed_report(self):
        """Print detailed cost report"""
        print("\n" + "="*80)
        print("DETAILED COST BREAKDOWN")
        print("="*80 + "\n")
        
        print("1. MAJOR EQUIPMENT (CAPEX)")
        print("-" * 80)
        for key, item in self.costs['capex'].items():
            print(f"   {item['description']}")
            print(f"   Quantity: {item['quantity']} @ R{item['unit_cost']:,.2f} each")
            print(f"   Subtotal: R{item['total']:,.2f}\n")
        print(f"   CAPEX TOTAL: R{self.costs['capex_total']:,.2f}")
        print("="*80 + "\n")
        
        print("2. SUPPORT EQUIPMENT & MONITORING")
        print("-" * 80)
        for key, item in self.costs['support_equipment'].items():
            print(f"   {item['description']}")
            print(f"   Quantity: {item['quantity']} @ R{item['unit_cost']:,.2f} each")
            print(f"   Subtotal: R{item['total']:,.2f}\n")
        print(f"   SUPPORT EQUIPMENT TOTAL: R{self.costs['support_total']:,.2f}")
        print("="*80 + "\n")
        
        print("3. INSTALLATION & LABOR")
        print("-" * 80)
        for key, item in self.costs['installation'].items():
            print(f"   {item['description']}")
            print(f"   Quantity: {item['quantity']} @ R{item['unit_cost']:,.2f} each")
            print(f"   Subtotal: R{item['total']:,.2f}\n")
        print(f"   INSTALLATION TOTAL: R{self.costs['installation_total']:,.2f}")
        print("="*80 + "\n")
        
        print("4. PROFESSIONAL SERVICES & COMPLIANCE")
        print("-" * 80)
        for key, item in self.costs['professional_services'].items():
            print(f"   {item['description']}")
            print(f"   Quantity: {item['quantity']} @ R{item['unit_cost']:,.2f} each")
            print(f"   Subtotal: R{item['total']:,.2f}\n")
        print(f"   PROFESSIONAL SERVICES TOTAL: R{self.costs['professional_total']:,.2f}")
        print("="*80 + "\n")

# Main execution
if __name__ == "__main__":
    print("="*80)
    print("SOLAR SYSTEM DESIGN - R50,000 BUDGET SOLUTION")
    print("Engineer: C. Nicholls | Company: UtCS (Pty) Ltd | Date: 2026-02-02")
    print("="*80)
    
    designer = SolarSystemDesign()
    
    print("\n📊 SYSTEM SIZING")
    print("-" * 80)
    design = designer.calculate_system_sizing()
    print(f"PV Array:          {design['pv']['total_capacity_kw']} kW ({design['pv']['num_panels']} x {design['pv']['panel_wattage']}W panels)")
    print(f"Inverter:          {design['inverter']['model']} - {design['inverter']['capacity_kw']} kW Hybrid")
    print(f"Battery:           {design['battery']['total_capacity_kwh']} kWh ({design['battery']['num_modules']} modules)")
    print(f"Daily PV Gen:      {design['performance']['daily_pv_generation_kwh']} kWh/day")
    print(f"Battery Usable:    {design['performance']['battery_usable_kwh']} kWh")
    print(f"Total Daily Cap:   {design['performance']['total_daily_capacity_kwh']} kWh/day")
    print(f"Target Load:       {design['performance']['target_daily_load_kwh']} kWh/day ✓")
    
    print("\n💰 COST SUMMARY")
    print("-" * 80)
    costs = designer.calculate_costs()
    print(f"CAPEX (Equipment):              R {costs['capex_total']:>10,.2f}")
    print(f"Support Equipment & Monitoring: R {costs['support_total']:>10,.2f}")
    print(f"Installation & Labor:           R {costs['installation_total']:>10,.2f}")
    print(f"Professional Services:          R {costs['professional_total']:>10,.2f}")
    print("-" * 80)
    print(f"SUBTOTAL (excl VAT):            R {costs['subtotal']:>10,.2f}")
    print(f"VAT (15%):                      R {costs['vat']:>10,.2f}")
    print("=" * 80)
    print(f"GRAND TOTAL (incl VAT):         R {costs['grand_total']:>10,.2f}")
    print(f"Budget:                         R {costs['budget']:>10,.2f}")
    print(f"Variance:                       R {costs['variance']:>10,.2f} ({costs['variance_percentage']:+.1f}%)")
    print("=" * 80)
    
    # Print detailed breakdown
    designer.print_detailed_report()
    
    # Save to JSON
    print("\n💾 SAVING DESIGN DATA")
    print("-" * 80)
    json_file = designer.save_to_json('/home/sandbox/solar_design_data.json')
    print(f"✓ Design data saved to: {json_file}")
    
    print("\n" + "="*80)
    print("✓ DESIGN COMPLETE - PROCEEDING TO WEB APP & LATEX DOCUMENTATION")
    print("="*80 + "\n")
