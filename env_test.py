# ============ ENVIRONMENT VARIABLES TEST ============
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variables
print("=== Environment Variables ===")

github_token = os.getenv("GITHUB_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")
app_env = os.getenv("APP_ENV")
log_level = os.getenv("LOG_LEVEL")

print(f"GITHUB_TOKEN:    {github_token}")
print(f"OPENAI_API_KEY:  {openai_key}")
print(f"APP_ENV:         {app_env}")
print(f"LOG_LEVEL:       {log_level}")

# Read with default value
print("\n=== With Defaults ===")
missing_var = os.getenv("MISSING_VAR", "default_value")
print(f"MISSING_VAR:     {missing_var}")

# Check if a secret is set
print("\n=== Secret Check ===")
if github_token and github_token != "your_github_token_here":
    print("✅ GITHUB_TOKEN is set with a real value")
else:
    print("⚠️  GITHUB_TOKEN is not set (or still placeholder)")

# Safe way to display secrets (never print full key)
print("\n=== Safe Display ===")
if openai_key:
    masked = openai_key[:8] + "..." + openai_key[-4:] if len(openai_key) > 12 else "***"
    print(f"OPENAI_API_KEY (masked): {masked}")
