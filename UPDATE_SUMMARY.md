# UtCS Nano-Grid Design Framework - Update Summary

## Updates Completed

### 1. **3D to 2D Conversion** ✓
- Replaced all 3D visualizations with professional 2D engineering diagrams
- Created canvas-based engineering diagrams using HTML5 Canvas API
- Added professional engineering charts using Chart.js

### 2. **Bottom Buttons Removed** ✓
- Removed all action buttons (Print, Download PDF, Email, Copy Link) from bottom of web app
- Cleaned up footer to show only contact information

### 3. **Contact Information Updated** ✓
- Updated telephone number to: **021 201 1364**
- Contact information now displayed in footer:
  - Tel: 021 201 1364
  - Email: info@utcs.co.za

### 4. **Mini-Sub Capacity Updated to 315 kVA** ✓
- Changed transformer capacity from 100 kVA to **315 kVA**
- Updated number of houses from 18 to **57 houses**
- Recalculated all network parameters with ADMD factor 0.4:
  - Total Installed Demand: **786.6 kVA** (57 × 13.8 kVA)
  - ADMD Demand: **314.6 kVA** (0.4 factor)
  - Utilization Factor: **99.9%**
  - Simultaneous Export (50%): **78.4 kW** (29 houses)
  - Peak Export (All Houses): **156.8 kW** (57 houses)
  - Transformer Reverse Flow: **49.8% of rating**

### 5. **ADMD Explanation Added** ✓
- Added comprehensive ADMD (After Diversity Maximum Demand) explanation section
- Included definition, importance, calculation example, and network planning application
- Explained how ADMD factor of 0.4 leads to 57 houses per 315 kVA mini-sub

### 6. **Professional 2D Engineering Diagrams** ✓

#### Energy Flow Diagram (Tab 1)
- Professional block diagram showing:
  - PV Array (2.75 kW, 5×550W)
  - Huawei Inverter (3 kW)
  - BESS (10.24 kWh LiFePO4)
  - House Load (15-20 kWh/day)
  - E460 Smart Meter
  - Municipal Grid
- Color-coded energy flow arrows with labels (DC, AC, Import/Export)
- System operation legend explaining daytime, night, and export modes

#### Engineering Charts
- **24-Hour Energy Generation & Consumption Profile**
  - Solar generation bell curve (0-2.75 kW)
  - House load profile showing morning and evening peaks
  
- **Battery State of Charge (SOC) Profile**
  - 24-hour SOC profile showing charge/discharge cycles
  - Range: 20% to 90% SOC

#### NRS097 Network Diagram (Tab 2)
- Professional network topology diagram showing:
  - 315 kVA Mini-Sub Transformer
  - 11kV supply connection
  - 400V/230V main feeder
  - 57 houses arranged in 6 rows
  - Each house with:
    - 60A single-phase connection
    - Solar panels on roof
    - House number labels
  - Color-coded feeders:
    - Red: 11kV supply
    - Orange: Main feeder
    - Yellow: Row feeders
    - Green: House connections
- Network specifications legend at bottom

### 7. **Complete BOQ Added to System Specifications Tab** ✓

#### CAPEX (Major Equipment): R26,850
- 5× JA Solar JAM72S30 550W Panels: R7,600
- Huawei SUN2000-3KTL-L1 3kW Inverter: R8,300
- 2× Huawei LUNA2000-5-S0 5.12kWh Battery: R8,400
- Landis+Gyr E460 Smart Meter: R2,550

#### Support Equipment & Monitoring: R7,385
- WiFi Router (Outdoor IP65): R620
- WiFi CCTV Camera 2MP: R880
- Roof Mounting Structure: R1,650
- AC/DC Protection Package: R1,650
- Cabling (DC/AC): R945
- MC4 Connectors & Terminals: R420
- Earthing Kit: R580
- PVC Conduit & Trunking: R260
- Weatherproof Enclosure IP55: R380

#### Installation & Labor: R7,020
- PV Panel Installation: R1,250
- Inverter & Battery Installation: R1,500
- Electrical Work & DB Board: R1,800
- Smart Meter Installation: R750
- CCTV Camera Installation: R520
- WiFi Router Configuration: R350
- System Commissioning & Training: R850

#### Professional Services: R2,130
- Electrical Design & SLD: R1,000
- Certificate of Compliance: R750
- Documentation & User Manuals: R380

#### Investment Summary
- **Subtotal (excl VAT):** R43,385
- **VAT (15%):** R6,508
- **GRAND TOTAL (incl VAT):** R49,893
- **Budget Variance:** +R107 (0.2% under R50,000 budget) ✓

## Website Features

### Navigation Tabs
1. **Energy Flow Diagram** - 2D engineering diagram with charts
2. **NRS097 Network** - Network topology with ADMD explanation
3. **Deployment Framework** - UtCS mass deployment framework
4. **System Specifications & BOQ** - Complete technical specs and costs

### Key Improvements
- Professional engineering diagrams (no 3D dependencies)
- Comprehensive ADMD explanation for network planning
- Complete itemized BOQ with all costs categorized
- Updated contact information
- Clean, professional layout without action buttons
- Responsive design for all screen sizes

## Deployed Website
**URL:** https://0w34gx9o.scispace.co

## Files Updated
1. `/home/sandbox/solar-solution-webapp/index.html` - Main HTML structure
2. `/home/sandbox/solar-solution-webapp/app.js` - JavaScript for diagrams and charts
3. `/home/sandbox/solar-solution-webapp/utcs-logo.png` - UtCS logo

## Technical Specifications

### System Capacity
- PV: 2.75 kW (5 × 550W JA Solar)
- Inverter: 3 kW (Huawei SUN2000-3KTL-L1)
- Battery: 10.24 kWh (2 × 5.12 kWh Huawei LUNA2000)
- Daily Capacity: 18.5 kWh/day

### Network Configuration (315 kVA Mini-Sub)
- Houses per transformer: 57
- Supply per house: 60A single-phase (13.8 kVA)
- ADMD Factor: 0.4
- Actual demand: 314.6 kVA
- Utilization: 99.9%

### NRS097 Compliance
- Max export per house: 2.75 kW (system limited)
- Export limit: 25% of supply (15A @ 230V = 3.45 kW)
- System compliance: ✓ Compliant
- Grid stability: ✓ Maintained

## Reference
- Project: UTCS-SOLAR-2026-001
- Engineer: C. Nicholls
- Company: UtCS (Pty) Ltd
- Status: CONFIDENTIAL
