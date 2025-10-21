# Set the API key environment variable
$env:EXA_API_KEY = "961d714f-f6cc-490e-bf71-b7aebcfe4eb3"
Write-Host "API key set for this session: $env:EXA_API_KEY"

# Run the Flask app
python app.py