#!/usr/bin/env python3
"""
Usage: python launch.py
"""
import os
import sys

def main():
    try:
        from dotenv import load_dotenv
        if os.path.exists('.env'):
            load_dotenv()
            print("Loaded configuration from .env file")
        else:
            print("No .env file found, using system environment variables")
    except ImportError:
        print("python-dotenv not installed, using system environment variables")
        print("   Run: pip install python-dotenv")
    
    api_key = os.environ.get('EXA_API_KEY')
    if not api_key:
        print("\nEXA_API_KEY not found!")
        print("\nTo fix this:")
        print("1. Create a .env file in this directory with:")
        print("   EXA_API_KEY=your-actual-api-key")
        print("\n2. Or set the environment variable:")
        print("   Windows: $env:EXA_API_KEY = 'your-key'")
        print("   Linux/Mac: export EXA_API_KEY='your-key'")
        sys.exit(1)
    
    print(f"API key loaded:")

    try:
        from app import app
        print("Starting AnySearch at http://127.0.0.1:5000")
        print("   Press Ctrl+C to stop the server")
        app.run(debug=True, host='127.0.0.1', port=5000)
    except ImportError as e:
        print(f"Error importing Flask app: {e}")
        print("   Make sure Flask and exa-py are installed: pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAnySearch stopped")

if __name__ == '__main__':
    main()