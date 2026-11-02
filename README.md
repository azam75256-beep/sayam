# FiberX

A modern, interactive textile fiber explorer and comparative analysis web app built with Streamlit.

## Features
- **Individual Fiber Explorer:** Interactive factsheets covering scientific classification, mechanical properties, advantages, limitations, commercial end uses, and major producing nations.
- **Side-by-Side Comparison:** Direct head-to-head comparison between any two textile fibers with responsive desktop and mobile matrices and identical selection safeguards.
- **Single Source of Truth:** Centralized Python dataset covering 7 natural and synthetic fibers.

## Included Fibers
- **Core Natural & Synthetic Fibers:** Cotton, Polyester, Wool
- **Extended Technical Fibers:** Silk, Jute, Hemp, Acrylic

## Project Structure
```text
fiber-explorer/
│
├── app.py              # Streamlit application with Explorer & Comparison tabs
├── requirements.txt    # Python package dependencies (streamlit)
└── README.md           # Project documentation and guide
```

## Running Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Community Cloud

1. Create a GitHub repository named `fiber-explorer`.
2. Commit and push `app.py`, `requirements.txt`, and `README.md` to GitHub.
3. Sign in to [share.streamlit.io](https://share.streamlit.io/) with your GitHub account.
4. Click **Create app**, select your repository, set the main file path to `app.py`, and click **Deploy!**.
