# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()
print("KEY =", os.getenv("GEMINI_API_KEY"))
