import os

def check_env_var():
    """Check if the EXA_API_KEY environment variable is set and print its value."""
    api_key = os.environ.get('EXA_API_KEY')
    
    if api_key:
        print(f"✅ EXA_API_KEY is set: {api_key[:5]}...{api_key[-4:]}")
        print("The API key is correctly configured in the environment.")
        print("You can now run the application with: python app.py")
    else:
        print("❌ EXA_API_KEY is NOT set")
        print("Please set the API key using one of these methods:")
        print("\n1. Windows PowerShell:")
        print("   $env:EXA_API_KEY = 'your-api-key'")
        print("\n2. Windows CMD:")
        print("   set EXA_API_KEY=your-api-key")
        print("\n3. Use the run_app.ps1 script:")
        print("   ./run_app.ps1")
        print("\n4. Use the run_app.bat batch file:")
        print("   run_app.bat")
        print("\nNote: For PowerShell, environment variables set with $env:VAR = 'value'")
        print("only persist for the current PowerShell session.")

if __name__ == "__main__":
    check_env_var()