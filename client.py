import os
from dotenv import load_dotenv

load_dotenv()

def main():
    run_localhost = os.getenv("RUN_LOCALHOST", "false").lower() == "true"
    if run_localhost:
        print("Running on localhost")
    else:
        print("Running on remote server")

if __name__ == "__main__":
    main()
print('test frontend')