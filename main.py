from dotenv import load_dotenv
import os

load_dotenv()






def main():
    print("Hello from langsmith-first-project!")
    print(os.getenv("GOOGLE_API_KEY"))
    


if __name__ == "__main__":
    main()
