# DGX Resource Monitor

A real-time monitoring dashboard for NVIDIA DGX A100 multi-user servers.

Built using **Python**, **Gradio**, **SQLite**, **Plotly**, and **NVIDIA NVML**, this dashboard provides a centralized view of GPU utilization, storage usage, running notebooks, active processes, and historical analytics for shared DGX systems.

---

## Features

- Real-time GPU monitoring
- GPU memory utilization
- GPU temperature and power usage
- Running Jupyter notebook detection
- Active process monitoring
- Storage utilization
- Historical data collection using SQLite
- Interactive web dashboard
- Responsive UI for desktop and laptop screens

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python |
| Database | SQLite |
| Dashboard | Gradio |
| Charts | Plotly |
| GPU Monitoring | NVIDIA NVML |
| Data Processing | Pandas |

---

## Project Structure

```
server_dashboard/
│
├── app.py
├── dashboard.py
├── analytics.py
├── collector.py
├── gpu.py
├── storage.py
├── processes.py
├── database.py
├── charts.py
├── components.py
├── styles.py
│
├── sections/
│
├── data/
│
├── logs/
│
└── reports/
```

---

## Dashboard Overview

Current modules include:

- System Summary
- GPU Overview
- Analytics (Work in Progress)
- Storage (Work in Progress)
- Users (Work in Progress)
- Running Processes (Work in Progress)
- Running Notebooks (Work in Progress)

---

## Architecture

```
System Metrics
        │
        ▼
collector.py
        │
        ▼
SQLite Database
        │
        ▼
analytics.py
        │
        ▼
Dashboard Sections
        │
        ▼
Gradio Dashboard
```

---

## Future Roadmap

- Interactive charts
- Auto-refresh dashboard
- GPU usage history
- User analytics
- Storage analytics
- Admin utilities
- PDF report generation
- Email alerts

---

## Installation

Clone the repository:

```bash
git clone https://github.com/srimeenakshiks/DGX-Resource-Monitor.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
python app.py
```

---

## Author

**Srimeenakshi K S**

Computer Science and Engineering  
VIT Chennai

---

## License

This project is licensed under the MIT License.