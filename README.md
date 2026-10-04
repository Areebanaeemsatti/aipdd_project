# AI Project Design & Development (AI-316)
**Course:** AI Project Design and Development (AI-316)  
**Institution:** Air University Islamabad | Department of Creative Technologies  
**Student Name:** Areeba  
**Lab Instructor:** Farhan Zafar Kayani  

---

## 📋 Overview

This repository contains the coursework, development environments, system design specifications, and source code modules for the **AI-316** laboratory series.

---

## 🛠️ Completed Lab Deliverables

### 🚀 Lab 01: Environment Configuration & Version Control Setup
**Focus:** Project workspace setup, Python virtual environment configuration, and version control initialization.

* **Repository Initialization:** Created a standardized Python project structure separating source code (`src/`), notebooks (`notebooks/`), and documentation.
* **Virtual Environment Setup:** Configured local environment dependencies and generated `requirements.txt` tracking core libraries (OpenCV, PyTorch, Ultralytics, NumPy, Matplotlib).
* **Git Version Control:** Initialized Git repository and authored `.gitignore` to exclude temporary runtime assets, virtual environment binaries (`.venv/`), and model weights.

---

### 🏗️ Lab 02: System Requirements & Software Architecture Design
**Focus:** System design specification for the **Smart Automated Attendance & Vision Analytics System**.

* **Requirements Breakdown (`ARCHITECTURE.md`):**
  * **Functional Requirements (FR-01 to FR-05):** Real-time face detection, facial recognition matching, automated attendance logging, database synchronization, and alert triggers.
  * **Non-Functional Requirements (NFR-01 to NFR-05):** Target processing frame rates (25–30 FPS), model accuracy thresholds (≥98.5%), processing latency (<200 ms), power constraints (≤25W), and AES-256 data privacy encryption.
* **Operational Boundary & Input/Output Mapping:** Defined camera RTSP stream specs, location metadata, visual overlays `[x1, y1, x2, y2]`, and database schemas alongside system memory and bandwidth caps.
* **Data-Flow Diagrams (DFDs):** Modeled Context Level 0 and Detailed Level 1 DFDs using Mermaid.js syntax.
* **Modular Software Blueprint (`src/`):** Defined component interfaces and created core modular class stubs:
  * `src/data_ingestion.py`: Multi-threaded frame acquisition.
  * `src/preprocessor.py`: Image normalization and color space transformation.
  * `src/inference_engine.py`: Neural network model execution engine.
  * `src/alert_logger.py`: Attendance persistence and notification dispatcher.

---

## 📁 Repository Directory Structure

```text
aipdd_project/
├── README.md                  # Main repository overview
├── ARCHITECTURE.md           # Lab 02: System Design Specification Document
├── .gitignore                # Lab 01: Git exclusion rules
├── requirements.txt          # Lab 01: Python dependencies
│
├── notebooks/
│   └── lab01_setup.ipynb     # Lab 01: Environment verification notebook
│
└── src/                      # Lab 02: Modular Python class components
    ├── __init__.py
    ├── data_ingestion.py     # Data Ingestion module
    ├── preprocessor.py       # Image Preprocessor module
    ├── inference_engine.py   # Model Inference Engine
    └── alert_logger.py       # Attendance & Alert Logger
