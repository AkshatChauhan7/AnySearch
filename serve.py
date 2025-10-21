#!/usr/bin/env python3
"""
Simple HTTP server for demonstrating the AnySearch application.
This script runs a basic HTTP server and handles CORS.

Usage:
  python serve.py

Then visit: http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers"""
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

def main():
    """Start the server"""
    print(f"Starting server at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    
    handler = CORSHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()

if __name__ == "__main__":
    main()