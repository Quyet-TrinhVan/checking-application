

# Face Checking Application

A modular, multi-platform solution for secure, real-time face recognition, anti-spoofing, and background analysis. This project supports backend, dashboard, and mobile components for comprehensive identity verification in various environments.

## Features
- **Face Recognition:** Detect and identify faces from images or video streams.
- **Anti-Spoofing:** Prevents fraudulent attempts using photos, videos, or masks.
- **Background Analysis:** Improves recognition accuracy by analyzing scene context.
- **RESTful API:** Integrate easily with other systems via HTTP endpoints.
- **Dashboard:** Web-based interface for monitoring and management.
- **Mobile:** Android and iOS clients for on-the-go verification.
- **Modular Design:** Easily extend or replace components for custom use cases.

## Project Structure
```
face_checking_application/
├── backend/         # Python backend (API, logic, models)
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── config/      # Configuration files
│   │   ├── modules/     # Core modules
│   │   ├── schemas/     # Data schemas
│   │   ├── services/    # Service layer
│   │   └── __init__.py
│   ├── data/            # ...
│   ├── model/           # Pretrained models
│   ├── requirements.txt
│   ├── run.py           # Backend entry point
│   └── test/            # Backend tests
├── dashboard/       # Web dashboard
│   ├── app.py
│   ├── requirements.txt
│   ├── static/
│   └── templates/
├── mobile/          # Mobile clients
│   ├── android/
│   ├── ios/
│   └── lib/
├── .env             # Environment (not tracked by git)
├── docs/            # Documentation and diagrams
├── workflow/        # System workflow diagrams
├── LICENSE
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites
- Python 3.10+ (for backend)
- pip
- Node.js & npm (if dashboard uses JS frameworks)
- Android Studio / Xcode (for mobile development)

### Installation

#### Backend
```sh
cd backend
pip install -r requirements.txt
python run.py
```

#### Dashboard
```sh
cd dashboard
pip install -r requirements.txt
python app.py
```

#### Mobile
- Open `mobile/android` in Android Studio or `mobile/ios` in Xcode.

## API Usage
- API endpoints are defined in `backend/app/api/`.
- See `docs/` for endpoint documentation and usage examples.

## Testing
- Backend tests: `pytest` in `backend/test/`
- Dashboard tests: (add instructions if available)
- Mobile tests: (add instructions if available)


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact **quyettv1302@gmail.com** or open an issue on GitHub.
