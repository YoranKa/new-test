# Sample Dashboard

A simple interactive web dashboard built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/python/). It displays a sample bar chart from a small dataset.

## Features

- Web-based dashboard served locally
- Bar chart visualizing sample category/value data
- Built with Dash, Plotly Express, and Pandas

## Prerequisites

- Python 3.8 or newer
- pip

## Installation

1. Clone or download this repository.

2. Install the required packages:

```bash
pip install dash plotly pandas
```

## Usage

Run the dashboard:

```bash
python test.py
```

Open your browser and go to [http://127.0.0.1:8050](http://127.0.0.1:8050) to view the dashboard.

The app runs in debug mode by default, so code changes will reload automatically.

## Project Structure

```
.
├── test.py      # Main Dash application
└── README.md    # Project documentation
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `dash` | Web framework for building the dashboard |
| `plotly` | Interactive charting (via Plotly Express) |
| `pandas` | Data handling for the sample dataset |

## License

This project is provided as-is for demonstration purposes.
