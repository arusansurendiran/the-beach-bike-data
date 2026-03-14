# 🚲 Beach BIA Bike Share Tracker

An automated data pipeline monitoring real-time activity across 16 curated **Bike Share Toronto** stations to analyze visitor movement in the Beach neighborhood.

---

### 🚀 What It Does

* **Real-time Monitoring:** Captures bike/dock availability, capacity, and GPS coordinates for 16 specific "Beach" stations.
* **Automated Scrape:** Runs every **15 minutes** via **GitHub Actions** using the `uv` package manager for high-speed performance.
* **Historical Dataset:** Appends live snapshots to `beach_bike_data.csv` to track trends over time.
* **BIA Insight:** Provides a data-backed proxy for visitor flow between the **Waterfront** and the **Queen St. E** retail corridor.

### 📍 Tracked Stations
Focuses on **16 strategic locations** representing the core Beaches area:
> `7319, 7313, 7309, 7303, 8190, 7314, 7427, 7695, 7428, 7365, 7692, 7315, 7317, 7318, 7316, 7364`

### 📁 File Structure
* **`scraper.py`**: Python script for fetching and filtering GBFS data.
* **`pyproject.toml`**: Modern project metadata and dependencies.
* **`beach_bike_data.csv`**: The primary historical dataset.
* **`.github/workflows/scrape.yml`**: Automation schedule and logic.

---
