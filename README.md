# ExaSearch - Modern Web Search UI

A professional search application built with Flask that demonstrates integration with the Exa search API. This project showcases modern web development techniques, clean UI/UX design, and proper API integration.

![ExaSearch Screenshot](https://via.placeholder.com/800x400?text=ExaSearch+Screenshot)

## Features

- Modern, responsive design with smooth animations
- Powerful search interface with domain filtering
- Works on desktop, tablet, and mobile devices
- Built with Flask, Bootstrap, and the Exa API
- Secure API key handling via environment variables

## Prerequisites

- Python 3.10+ (3.11+ recommended)
- Exa API key (get one from [exa.ai](https://exa.ai))

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/exasearch.git
   cd exasearch
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   
   **Option A: Create a .env file (Recommended)**
   ```bash
   # Create .env file in the project root
   echo "EXA_API_KEY=your-api-key-here" > .env
   ```
   
   **Option B: Set environment variable**
   ```powershell
   # Windows PowerShell
   $env:EXA_API_KEY = "your-api-key-here"
   
   # Linux/Mac
   export EXA_API_KEY="your-api-key-here"
   ```

## Running the Application

**Option 1: Using the launcher (Recommended)**
```bash
python launch.py
```

**Option 2: Direct Flask app**
```bash
python app.py
```

**Option 3: Using the quick run scripts**
```bash
# Windows
run_app.bat
# or
./run_app.ps1
```

Then open http://127.0.0.1:5000 in your browser.

## API Key Security

This application requires an Exa API key to function. For security:

- **Never commit your API key** to source control
- Set it as an environment variable as shown above
- For production deployment, use a proper secrets management solution
- The `.gitignore` file is configured to help prevent accidental exposure

## Making It Permanent

To make your API key persistent:

**Windows:**
```powershell
setx EXA_API_KEY "your-api-key-here"
# Close and reopen your terminal for this to take effect
```

**Linux/Mac (add to ~/.bashrc or ~/.zshrc):**
```bash
echo 'export EXA_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Deployment Options

This application can be deployed to various platforms:

- **Heroku:** Set `EXA_API_KEY` in Config Vars
- **Vercel:** Add environment variable in project settings
- **AWS/Azure:** Use their respective secrets management services

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5, custom CSS
- **Icons:** Bootstrap Icons
- **Fonts:** Inter (Google Fonts)
- **API:** Exa Search API

## Author

AKSHAT CHAUHAN