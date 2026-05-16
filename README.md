# 🌤️ Advanced Weather Station (GCP Native CI/CD Project)

An ultra-modern, production-ready Weather Dashboard application built with **Flask (Python)** and fully automated using **Google Cloud Platform (GCP)**. This project demonstrates a complete **GitOps / CI/CD pipeline** where pushing code to GitHub automatically triggers a build and deploys the app to a serverless environment.

🚀 **Live Demo:** [https://weather-app-41719782460.us-central1.run.app](https://weather-app-41719782460.us-central1.run.app)

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/949c4562-9b28-4264-8e75-0d3a6493460a" />
---

## ✨ Features

- **Dynamic City-Specific Timezone:** Automatically calculates and displays the exact local date and time of the searched city (not the user's local machine time).
- **Comprehensive Environmental Specs:** Displays 6 core weather metrics:
  - Temperature & "Feels Like" index
  - Humidity percentage
  - Wind Speed (m/s)
  - Atmospheric Pressure (hPa)
  - Visibility (km)
  - Cloudiness percentage
- **Premium UI/UX:** A glassmorphic theme featuring dark cinematic radial gradients, smooth CSS animations, and contextual responsive iconography.
- **Production-Grade Security:** 100% compliant with zero-hardcoded secrets. API keys are injected safely via GCP Environment Variables.

---

## 🛠️ Tech Stack & Architecture

- **Backend:** Python 3.9, Flask, Gunicorn (WSGI HTTP Server)
- **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid, Animations), JavaScript (Vanilla)
- **API Integration:** OpenWeatherMap API
- **Cloud Infrastructure (GCP):**
  - **Cloud Build:** Handles automated Docker image compilation.
  - **Artifact Registry:** Secure storage for versioned Docker container images.
  - **Cloud Run:** Fully managed serverless hosting (scales to zero when inactive).

---

## 🔄 Automated CI/CD Pipeline Flow

1. **Code Commit:** Developer pushes code changes to the `main` branch on GitHub.
2. **Webhook Trigger:** GCP Cloud Build detects the push event via a secure trigger.
3. **Containerization:** Cloud Build reads the `Dockerfile`, compiles the app, and pushes it to **Artifact Registry**.
4. **Serverless Deployment:** Cloud Build instructs **Cloud Run** to deploy a new revision of the container seamlessly with zero downtime.