#****paste this in the terminal"python deployment/run_app_with_ngrok.py****


import os
import time
import threading
from pyngrok import ngrok

# CONFIG
STREAMLIT_FILE = "ui/app.py"  # path to your Streamlit file
PORT = 8501

def start_streamlit():
    """Start the Streamlit app."""
    os.system(f"streamlit run {STREAMLIT_FILE} --server.port {PORT}")

def start_ngrok():
    """Start ngrok tunnel and print the public URL."""
    public_url = ngrok.connect(PORT).public_url
    print(f"\n🚀 Public URL: {public_url}\n")
    print("Share this link — it will stay live while this script is running.")

if __name__ == "__main__":
    # Start ngrok in a separate thread
    threading.Thread(target=start_ngrok, daemon=True).start()
    
    # Wait a moment so ngrok starts before Streamlit
    time.sleep(2)
    
    # Start Streamlit (blocking)
    start_streamlit()
