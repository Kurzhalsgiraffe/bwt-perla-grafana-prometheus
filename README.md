# BWT Perla Monitoring with Prometheus & Grafana

Monitor your **BWT Perla Soft Water System** using **Prometheus** and visualize metrics in **Grafana**.

<img src="grafana_screenshot.png" width="500" alt="Grafana dashboard screenshot">

---

## Overview

This project consists of **three components** running via Docker Compose:

1. **Exporter (`app.py`)**  
   - A small Python service that fetches JSON metrics from the BWT Perla API when accessed via HTTP.  
   - Example endpoint: `http://<HOST_IP>:8000/metrics`

2. **Prometheus**  
   - Acts as a **time-series database**, scraping metrics from the Exporter every **15 seconds**.  
   - Old data is automatically deleted after **180 days** (retention time).

3. **Grafana**  
   - Provides a customizable dashboard to visualize the collected metrics.  
   - You can import the provided dashboard template or create your own visualizations.

---

## Setup Instructions

### 1. Requirements

- A host system (e.g. **Raspberry Pi 3B+**, Ubuntu, or any Linux system)
- Installed:
  - [Docker](https://docs.docker.com/get-docker/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
  - [Python 3](https://www.python.org/downloads/) – required for the Exporter  
  - [Flask](https://flask.palletsprojects.com/) – lightweight web framework used by the Exporter

Example installation commands (Debian/Raspberry Pi OS):

```bash
sudo apt update
sudo apt install -y docker.io docker-compose python3 python3-pip
sudo pip3 install flask
sudo systemctl enable docker
sudo systemctl start docker
```

### 2. Setup

After installing Docker and Flask, move into the **setup** directory and edit
```bash
AUTH = ("user", "password")
```
in **app.py** to your own BWT-Perla API password.

After that, run
```bash
sudo docker-compose up -d
```

Once the setup is complete, all services will start automatically, and you can access them using your host’s IP address:

- **Exporter:** `http://<HOST_IP>:8000`  
- **Prometheus:** `http://<HOST_IP>:9090`  
- **Grafana:** `http://<HOST_IP>:3000`

> Replace `<HOST_IP>` with the actual IP address of your system (for example, `192.168.178.100`).

### 3. Grafana Setup

1. Open Grafana in your web browser: `http://<HOST_IP>:3000`
2. Log in using the default credentials:  
   **Username:** `admin`  
   **Password:** `admin`
3. You’ll be prompted to change the default password on first login.
4. Add **Prometheus** as a data source:
   - Go to **Settings → Data Sources → Add data source → Prometheus**
   - Set the URL to `http://prometheus:9090`
   - Click **Save & Test**
5. Import the provided dashboard (optional):
   - Navigate to **Dashboards → Import**
   - Upload or paste the contents of `BWT_Perla-1763031758198.json`
   - Or create your own custom dashboard.

After these steps, Grafana will begin displaying live metrics from your BWT Perla system via Prometheus.