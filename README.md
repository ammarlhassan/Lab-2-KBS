# Lab 2: Hardware Configuration Expert System

## Overview
This project implements a **rule‑based expert system** using the **Experta** library in Python. The system helps users choose a compatible set of computer hardware components (**CPU**, **Motherboard**, **GPU**) tailored to their specified use case:

- **Gaming**: High‑performance CPU/GPU combinations.
- **Office Work**: Mid‑range CPU with basic graphics.
- **Video Editing**: Multi‑core CPU and high‑performance GPU with ample RAM support.

It validates compatibility (socket matching, expansion slot requirements) and handles invalid inputs gracefully.

## Repository Structure
```
lab‑2‑KBS/
├── data.py           # Predefined component pool (CPU, Motherboard, GPU)
├── facts.py          # Custom Fact classes with attribute validation
├── rules.py          # Experta engine: recommendation & compatibility rules
├── engine.py         # CLI entry point: gathers input, runs engine, displays results
├── demo.py           # Sample runs for gaming, office, and video_editing
└── README.md         # Project overview and instructions
```

## Requirements
- **Python** 3.6 or higher
- **Experta** library

Install Experta via pip:

```

bash
pip install experta
```

## Installation and Setup
1. Clone the repository:
   ```bash
git clone https://github.com/YourUsername/lab-2-KBS.git
cd lab-2-KBS
```
2. (Optional) Create and activate a virtual environment:
   ``` bash
python3 -m venv env
source env/bin/activate
   ```
3. Install dependencies:
   ```bash
pip install experta
```

## Usage
- **Interactive mode**: prompts for a use case and outputs a recommended configuration.
  ```bash
python engine.py
```  
  _Enter one of: gaming, office, video_editing_  

- **Automated demos**: runs all three scenarios in sequence.
  ```bash
python demo.py
```

## Sample Output
```
$ python engine.py
Enter your use-case (gaming, office, video_editing): gaming

Recommended Configuration:
 CPU: Intel i9-10900K
 Motherboard: ASUS ROG Strix
 GPU: NVIDIA RTX 3080
Compatibility confirmed!
```
