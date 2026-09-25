# INJECTOR DIAGNOSTIC GUI

A professional Python GUI for automotive diagnostics, built with PySide6.

## Overview

This project provides a modular and extensible desktop GUI for an injector diagnostic system. It is designed for:
- Modern automotive diagnostics user interface
- Simulation-first development approach
- Future OBD-II / CAN / hardware integration
- Professional workshop-oriented workflows

## Features

- **Dashboard** - ECU status, battery voltage, RPM, temperature, fault count at a glance
- **Live Data** - Real-time display of RPM, coolant temperature, TPS, MAP, MAF, O2 sensor, battery voltage
- **ECU Scan** - Read, decode, and clear simulated DTCs with detailed information
- **Injector Test** - Workflow for resistance, pulse, flow, and leak tests
- **Diagnosis** - Step-by-step diagnosis workflow with possible causes and remediation actions
- **Settings** - Configure vehicle, ECU, and communication parameters
- **Simulation Mode** - Complete simulation backend for isolated development without hardware
- **Clean Modular Architecture** - Ready for future C++ diagnostic core integration

## Tech Stack

- Python 3.11+
- PySide6 (Qt for Python)
- pytest for unit testing
- Clean architecture with separation of concerns

## Installation

### Prerequisites
- Python 3.11 or higher
- pip or conda

### Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate   # Linux/macOS
# or
.venv\\Scripts\\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

or

```bash
python -m app.main
```

## GUI Architecture

The project follows a clean, modular architecture:

```
app/
├── ui/                   # PySide6 UI components
│   ├── main_window.py   # Main application window
│   ├── dashboard.py     # Dashboard widget
│   ├── live_data.py     # Live data display
│   ├── ecu_scan.py      # ECU scan interface
│   ├── injector_test.py # Injector testing interface
│   ├── diagnosis.py     # Diagnosis workflow
│   └── settings.py      # Settings interface
│
├── core/                 # Business logic & models
│   ├── models.py        # Data models and enums
│   ├── simulator.py     # Simulation backend
│   └── diagnostics.py   # Diagnosis engine
│
├── services/            # Service layer
│   ├── ecu_service.py       # ECU operations
│   ├── injector_service.py  # Injector testing
│   └── diagnosis_service.py # Diagnosis operations
│
└── communication/       # Communication interfaces (future hardware)
    ├── interface.py     # Abstract communication interface
    ├── simulation.py    # Simulation communication
    ├── obd.py          # OBD-II communication (placeholder)
    └── can.py          # CAN communication (placeholder)
```

## Simulation Mode

The application runs in **Simulation Mode by default**. All data is clearly marked as simulated:
- Live data values are generated programmatically
- DTCs are predefined sample records
- Injector tests return simulated results
- No real ECU or hardware is accessed

The UI clearly indicates when running in simulation mode, preventing confusion with real diagnostic data.

## C++ Integration Roadmap

This GUI is architected to connect to the C++ diagnostic core (`Injector-Diagnostic`) in the future through:

- **subprocess** - Direct process communication
- **C API binding** - ctypes/cffi integration
- **Shared library** - DLL/SO dynamic loading
- **IPC** - Inter-process communication (socket, named pipe)
- **gRPC** - Remote procedure calls for distributed systems

The current simulation layer can be swapped with real backend calls without changing the UI.

## Testing

Run unit tests with pytest:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Test coverage:
- Simulator data generation
- DTC record management
- Injector test workflows
- Service layer operations
- Diagnosis engine workflows

## Project Structure

```
Injector-Diagnostic-GUI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ui/
│   ├── core/
│   ├── communication/
│   └── services/
├── tests/
│   ├── test_simulator.py
│   ├── test_diagnostics.py
│   └── test_services.py
├── requirements.txt
├── README.md
├── .gitignore
└── app.py              # Entry point
```

## Roadmap

- [x] Dashboard with status cards
- [x] Live data visualization
- [x] ECU scan with DTC details
- [x] Injector test simulation
- [x] Diagnosis workflow engine
- [x] Settings interface
- [x] Simulation backend
- [x] Unit tests
- [ ] Real OBD-II connection layer
- [ ] CAN protocol support
- [ ] C++ core integration via IPC
- [ ] Hardware adapter abstraction
- [ ] Advanced charting and graphs
- [ ] Data logging and export
- [ ] Real-time performance monitoring
- [ ] Multi-language support
- [ ] Dark/Light theme toggle

## Important Notes

### Simulation Mode
This application operates in **Simulation Mode only**. It does not connect to real vehicle ECUs or injector test benches. All data is simulated and clearly marked as such.

### Safety & Liability
This is a development foundation and diagnostic framework, not a certified automotive diagnostic tool. For professional vehicle diagnostics, use certified OEM diagnostic equipment with proper training and safety procedures.

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- New features include unit tests
- Modular architecture is maintained
- Comments explain complex logic

## License

MIT License - See LICENSE file for details

## Author

Developed as a professional automotive diagnostic framework.

## Support

For issues, questions, or feature requests, please create an issue in the repository.
