# Currency Converter

## Overview

Currency Converter is a simple Python program with a graphical user interface (GUI) built using the Tkinter library. It takes advantage of the `forex-python` library to fetch exchange rates and convert between different foreign currencies. 

## Features

- **User-Friendly GUI:** The program provides a user-friendly interface with dropdowns to select the source and target currencies, input fields for the amount, and a button to perform the conversion.

- **Real Exchange Rates:** Upon installation of the 'forex-python' package, the program will retrieve the actual exchange rates at that time. However, note that the exchange rates will not update in real time. See below for how to update the package to get the most updated exchange rates. 

## Getting Started

### Prerequisites

- Python 3
- Install required packages: `pip install forex-python`

### Usage

1. Clone the repository: `git clone https://github.com/your-username/currency-converter.git`
2. Navigate to the project directory: `cd currency-converter`
3. Run the program: `python currency_converter.py`

### Updating Exchange Rates

Please be aware that the exchange rates fetched by the program might not be up-to-date in real-time. To manually update the library and potentially get the latest rates:

```bash
pip install --upgrade forex-python
