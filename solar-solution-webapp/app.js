// Tab switching
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName + '-tab').classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// Initialize all diagrams on page load
window.addEventListener('load', () => {
    drawEnergyFlowDiagram();
    drawEnergyProfileChart();
    drawBatterySOCChart();
    drawNetworkDiagram();
});

// Draw Energy Flow Diagram
function drawEnergyFlowDiagram() {
    const canvas = document.getElementById('energyFlowDiagram');
    const ctx = canvas.getContext('2d');
    
    // Set canvas size
    canvas.width = 1200;
    canvas.height = 600;
    
    // Background
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Title
    ctx.fillStyle = '#1f2937';
    ctx.font = 'bold 24px Inter';
    ctx.textAlign = 'center';
    ctx.fillText('Energy Flow Diagram - Nano-Grid System', canvas.width / 2, 40);
    
    // Component positions
    const components = {
        pv: { x: 200, y: 150, w: 120, h: 80, label: 'PV Array\n2.75 kW\n5×550W', color: '#fbbf24' },
        inverter: { x: 450, y: 250, w: 120, h: 100, label: 'Huawei\nInverter\n3 kW', color: '#60a5fa' },
        battery: { x: 200, y: 350, w: 120, h: 80, label: 'BESS\n10.24 kWh\nLiFePO4', color: '#f97316' },
        house: { x: 700, y: 250, w: 140, h: 100, label: 'House Load\n15-20 kWh/day', color: '#10b981' },
        meter: { x: 900, y: 250, w: 100, h: 80, label: 'E460\nSmart\nMeter', color: '#8b5cf6' },
        grid: { x: 1050, y: 250, w: 100, h: 80, label: 'Municipal\nGrid', color: '#3b82f6' }
    };
    
    // Draw components
    Object.entries(components).forEach(([key, comp]) => {
        // Component box
        ctx.fillStyle = comp.color;
        ctx.fillRect(comp.x, comp.y, comp.w, comp.h);
        ctx.strokeStyle = '#1f2937';
        ctx.lineWidth = 2;
        ctx.strokeRect(comp.x, comp.y, comp.w, comp.h);
        
        // Label
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 14px Inter';
        ctx.textAlign = 'center';
        const lines = comp.label.split('\n');
        lines.forEach((line, i) => {
            ctx.fillText(line, comp.x + comp.w / 2, comp.y + 25 + i * 18);
        });
    });
    
    // Draw energy flow arrows
    const arrows = [
        { from: 'pv', to: 'inverter', label: 'DC', color: '#fbbf24' },
        { from: 'battery', to: 'inverter', label: 'DC Charge/Discharge', color: '#f97316' },
        { from: 'inverter', to: 'house', label: 'AC 230V', color: '#10b981' },
        { from: 'house', to: 'meter', label: 'Monitoring', color: '#8b5cf6' },
        { from: 'meter', to: 'grid', label: 'Import/Export', color: '#3b82f6' }
    ];
    
    arrows.forEach(arrow => {
        const from = components[arrow.from];
        const to = components[arrow.to];
        
        // Arrow line
        ctx.strokeStyle = arrow.color;
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        let startX, startY, endX, endY;
        
        if (arrow.from === 'pv' && arrow.to === 'inverter') {
            startX = from.x + from.w / 2;
            startY = from.y + from.h;
            endX = to.x + to.w / 2;
            endY = to.y;
        } else if (arrow.from === 'battery' && arrow.to === 'inverter') {
            startX = from.x + from.w;
            startY = from.y + from.h / 2;
            endX = to.x;
            endY = to.y + to.h / 2;
        } else {
            startX = from.x + from.w;
            startY = from.y + from.h / 2;
            endX = to.x;
            endY = to.y + to.h / 2;
        }
        
        ctx.moveTo(startX, startY);
        ctx.lineTo(endX, endY);
        ctx.stroke();
        
        // Arrow head
        const angle = Math.atan2(endY - startY, endX - startX);
        ctx.beginPath();
        ctx.moveTo(endX, endY);
        ctx.lineTo(endX - 15 * Math.cos(angle - Math.PI / 6), endY - 15 * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(endX - 15 * Math.cos(angle + Math.PI / 6), endY - 15 * Math.sin(angle + Math.PI / 6));
        ctx.closePath();
        ctx.fillStyle = arrow.color;
        ctx.fill();
        
        // Arrow label
        ctx.fillStyle = '#1f2937';
        ctx.font = '12px Inter';
        ctx.textAlign = 'center';
        ctx.fillText(arrow.label, (startX + endX) / 2, (startY + endY) / 2 - 10);
    });
    
    // Legend
    ctx.fillStyle = '#f3f4f6';
    ctx.fillRect(50, 480, 1100, 100);
    ctx.strokeStyle = '#d1d5db';
    ctx.lineWidth = 1;
    ctx.strokeRect(50, 480, 1100, 100);
    
    ctx.fillStyle = '#1f2937';
    ctx.font = 'bold 14px Inter';
    ctx.textAlign = 'left';
    ctx.fillText('System Operation:', 70, 510);
    
    ctx.font = '12px Inter';
    ctx.fillText('• Daytime: PV generates power → Supplies house load → Excess charges battery', 70, 535);
    ctx.fillText('• Night: Battery discharges → Supplies house load → Grid imports if needed', 70, 555);
    ctx.fillText('• Export: Excess solar energy can be exported to grid (max 2.75kW)', 70, 575);
}

// Draw 24-Hour Energy Profile Chart
function drawEnergyProfileChart() {
    const ctx = document.getElementById('energyProfileChart').getContext('2d');
    
    const hours = Array.from({ length: 24 }, (_, i) => i + ':00');
    
    // Solar generation profile (bell curve)
    const solarData = hours.map((_, i) => {
        if (i < 6 || i > 18) return 0;
        const normalized = (i - 6) / 12;
        return Math.exp(-Math.pow((normalized - 0.5) * 4, 2)) * 2.75;
    });
    
    // Load profile
    const loadData = [0.5, 0.5, 0.5, 0.5, 0.5, 0.8, 2.0, 2.0, 1.5, 1.0, 1.0, 1.0, 
                      1.2, 1.0, 1.0, 1.2, 1.5, 2.5, 2.5, 2.5, 2.0, 1.5, 1.0, 0.8];
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: hours,
            datasets: [
                {
                    label: 'Solar Generation (kW)',
                    data: solarData,
                    borderColor: '#fbbf24',
                    backgroundColor: 'rgba(251, 191, 36, 0.1)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'House Load (kW)',
                    data: loadData,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Power (kW)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time of Day'
                    }
                }
            }
        }
    });
}

// Draw Battery SOC Chart
function drawBatterySOCChart() {
    const ctx = document.getElementById('batterySOCChart').getContext('2d');
    
    const hours = Array.from({ length: 24 }, (_, i) => i + ':00');
    
    // Battery SOC profile
    const socData = hours.map((_, i) => {
        if (i >= 6 && i <= 16) {
            // Charging during day
            return Math.min(90, 50 + (i - 6) * 4);
        } else if (i > 16 && i <= 23) {
            // Discharging evening
            return Math.max(20, 90 - (i - 16) * 10);
        } else {
            // Night discharge
            return Math.max(20, 50 - i * 2);
        }
    });
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: hours,
            datasets: [
                {
                    label: 'Battery SOC (%)',
                    data: socData,
                    borderColor: '#f97316',
                    backgroundColor: 'rgba(249, 115, 22, 0.1)',
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: false
                }
            },
            scales: {
                y: {
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'State of Charge (%)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time of Day'
                    }
                }
            }
        }
    });
}

// Draw Network Diagram
function drawNetworkDiagram() {
    const canvas = document.getElementById('networkDiagram');
    const ctx = canvas.getContext('2d');
    
    // Set canvas size
    canvas.width = 1200;
    canvas.height = 700;
    
    // Background
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Title
    ctx.fillStyle = '#1f2937';
    ctx.font = 'bold 24px Inter';
    ctx.textAlign = 'center';
    ctx.fillText('NRS097 Network Topology - 315kVA Mini-Sub with 57 Houses', canvas.width / 2, 40);
    
    // Draw transformer
    ctx.fillStyle = '#10b981';
    ctx.fillRect(550, 100, 100, 80);
    ctx.strokeStyle = '#1f2937';
    ctx.lineWidth = 2;
    ctx.strokeRect(550, 100, 100, 80);
    
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 16px Inter';
    ctx.textAlign = 'center';
    ctx.fillText('315 kVA', 600, 130);
    ctx.font = '14px Inter';
    ctx.fillText('Mini-Sub', 600, 150);
    ctx.fillText('Transformer', 600, 168);
    
    // Draw 11kV connection
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(600, 50);
    ctx.lineTo(600, 100);
    ctx.stroke();
    
    ctx.fillStyle = '#1f2937';
    ctx.font = '12px Inter';
    ctx.fillText('11kV Supply', 600, 75);
    
    // Draw main feeder
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(600, 180);
    ctx.lineTo(600, 250);
    ctx.stroke();
    
    ctx.fillStyle = '#1f2937';
    ctx.fillText('400V/230V', 650, 220);
    ctx.fillText('Main Feeder', 650, 235);
    
    // Draw houses in 6 rows of 9-10 houses each (57 total)
    const houseSize = 50;
    const houseSpacing = 80;
    const startX = 100;
    const rows = 6;
    const housesPerRow = [10, 10, 10, 9, 9, 9]; // Total = 57
    
    let houseCounter = 0;
    for (let row = 0; row < rows; row++) {
        const rowY = 280 + row * 100;
        const housesInThisRow = housesPerRow[row];
        
        // Draw horizontal feeder for this row
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(50, rowY);
        ctx.lineTo(1150, rowY);
        ctx.stroke();
        
        // Draw connection from main to row feeder
        if (row === 0) {
            ctx.strokeStyle = '#f97316';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(600, 250);
            ctx.lineTo(600, rowY);
            ctx.stroke();
        } else {
            ctx.strokeStyle = '#fbbf24';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(600, 280);
            ctx.lineTo(600, rowY);
            ctx.stroke();
        }
        
        for (let col = 0; col < housesInThisRow; col++) {
            const houseX = startX + col * houseSpacing * 1.1;
            houseCounter++;
            const houseNumber = houseCounter;
            
            // Draw connection line
            ctx.strokeStyle = '#10b981';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(houseX + houseSize / 2, rowY);
            ctx.lineTo(houseX + houseSize / 2, rowY + 30);
            ctx.stroke();
            
            // Draw house
            ctx.fillStyle = '#3b82f6';
            ctx.fillRect(houseX, rowY + 30, houseSize, houseSize * 0.8);
            ctx.strokeStyle = '#1f2937';
            ctx.lineWidth = 1;
            ctx.strokeRect(houseX, rowY + 30, houseSize, houseSize * 0.8);
            
            // Draw roof
            ctx.fillStyle = '#1e40af';
            ctx.beginPath();
            ctx.moveTo(houseX - 5, rowY + 30);
            ctx.lineTo(houseX + houseSize / 2, rowY + 15);
            ctx.lineTo(houseX + houseSize + 5, rowY + 30);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Draw solar panels on roof
            ctx.fillStyle = '#1f2937';
            for (let p = 0; p < 3; p++) {
                ctx.fillRect(houseX + 10 + p * 15, rowY + 20, 12, 8);
            }
            
            // House number
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 14px Inter';
            ctx.textAlign = 'center';
            ctx.fillText('#' + houseNumber, houseX + houseSize / 2, rowY + 60);
            
            // House specs
            ctx.font = '9px Inter';
            ctx.fillText('60A', houseX + houseSize / 2, rowY + 75);
        }
    }
    
    // Legend
    ctx.fillStyle = '#f3f4f6';
    ctx.fillRect(50, 620, 1100, 70);
    ctx.strokeStyle = '#d1d5db';
    ctx.lineWidth = 1;
    ctx.strokeRect(50, 620, 1100, 70);
    
    ctx.fillStyle = '#1f2937';
    ctx.font = 'bold 14px Inter';
    ctx.textAlign = 'left';
    ctx.fillText('Network Specifications:', 70, 645);
    
    ctx.font = '11px Inter';
    ctx.fillText('• 57 Houses @ 60A each (13.8 kVA max demand) = 786.6 kVA total installed', 70, 665);
    ctx.fillText('• ADMD Factor: 0.4 → Actual demand: 314.6 kVA (99.9% utilization)', 70, 680);
    
    ctx.fillText('• Each house: 2.75kW PV + 10.24kWh BESS', 550, 665);
    ctx.fillText('• Max export per house: 2.75kW (NRS097 compliant)', 550, 680);
}

// Handle window resize for charts
window.addEventListener('resize', () => {
    // Charts will auto-resize due to responsive: true
});
