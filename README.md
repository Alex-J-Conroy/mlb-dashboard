# ⚾ MLB Stats Dashboard — Interactive Baseball Performance Explorer

## 📌 Overview

This project delivers a fully interactive **MLB performance dashboard** built using **Plotly Dash**. It enables users to explore team and player statistics from the **Retrosheet dataset (2000–2019)** with custom filters, visualisations, and comparisons.

The dashboard empowers users — especially team managers, analysts, and fans — to:
- Track player performance across seasons
- Compare batting vs pitching metrics
- View positional breakdowns and time-series stats
- Make informed decisions on roster and strategy

---

## 👤 Author

**Alex Conroy**  
Individual project submitted as part of **IFN703 — Interactive Visualisation & Analytics**

---

## 🛠 Tech Stack

- **Python**  
- **Dash / Plotly** for UI and charts  
- **Pandas** / **NumPy** for data manipulation  
- **Retrosheet MLB** CSVs as data source  

---

## 🔍 Features

✅ **Filter by player, team, or position**  
✅ **Dynamic radar plots** to compare player skill areas  
✅ **Bar charts** for team-level performance  
✅ **Time series visualisations** for performance trends  
✅ **Built with modular components** for clean code

---

## 📁 Project Structure
mlb-dashboard/ ├── data/ # Contains MLB stats (see below) │ ├── Battings.csv │ ├── Pitchings.csv │ ├── 2019combinedroster.txt │ └── TEAM2019.txt ├── notebooks/ │ └── Dashboard.ipynb # Original notebook prototype ├── src/ │ ├── app.py # Dash layout & callbacks │ └── visualisations.py # Reusable Plotly chart functions ├── utils/ │ └── data_processing.py # Merging and cleanup utilities ├── report/ │ └── IFN703_Assignment3_Report.pdf ├── requirements.txt └── README.md

## 🧾 Data Notes

- Source: **Retrosheet.org** (historical MLB data)
- Manual preprocessing done to extract:
  - `Battings.csv`, `Pitchings.csv`  
  - Team/player mappings (`2019combinedroster.txt`, `TEAM2019.txt`)

> These files must be manually placed in the `data/` folder.  
> They are not included in the repo due to size.

---

## 📊 Sample Visualisations
- ![radar](https://github.com/user-attachments/assets/60910d61-6e47-4fc4-9697-a11768d39de3)
- ![dashboard with layout](https://github.com/user-attachments/assets/970f8d8a-cc92-44e4-85ff-79e37c476dc7)
- ![pitching IP bar](https://github.com/user-attachments/assets/530b963c-4aa8-4e2a-bc2a-138bab03dfd0)


## 🔮 Future Improvements
- Integrate live data feeds via API
- Add player prediction metrics (e.g. WAR forecast)
- Support mobile layout and responsive resizing
- Add download/export options for filtered stats
