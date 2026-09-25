# INJECTOR DIAGNOSTIC GUI

A professional Python GUI for automotive diagnostics, built with PySide6.

## Overview

This project provides a modular and extensible desktop GUI for an injector diagnostic system. It is designed for:
- Modern automotive diagnostics user interface
- Simulation-first development approach
- Future OBD-II / CAN / hardware integration
- Professional workshop-oriented workflows

## Features

- Dashboard with ECU status, battery voltage, RPM, temperature, fault count
- Live Data monitoring panel
- ECU scan with DTC search, favorites, and filtering
- Injector test workflow for resistance, pulse, flow, and leak tests
- Diagnosis workflow with possible causes and next actions
- Settings for vehicle, ECU, communication, and theme selection
- Simulation mode for isolated development without hardware
- Data logging to CSV export
- DTC history tracking
- Work session notes and report export
- Batch injector testing
- Real-time alerts and notifications
- Modern dark UI with light mode option
- Modular architecture ready for future C++ integration

## Tech Stack

- Python 3.11+
- PySide6 (Qt for Python)
- pytest
- Clean architecture with separation of concerns

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## GUI Architecture

```text
app/
├── ui/
├── core/
├── services/
├── communication/
└── main.py
```

## Simulation Mode

All data is simulated and clearly marked as such.

## Testing

```bash
pytest
```

## Roadmap

- [x] Dashboard
- [x] Live Data
- [x] ECU Scan with search and filtering
- [x] Injector Test
- [x] Diagnosis
- [x] Settings and theme support
- [x] Simulation backend
- [x] Unit tests
- [x] CSV export and logging
- [x] Session tracking
- [x] Alerts system
- [ ] Real OBD-II connection layer
- [ ] CAN protocol support
- [ ] C++ core integration
