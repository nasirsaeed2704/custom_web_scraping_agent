from dotenv import load_dotenv
import os

load_dotenv()

configs = {
    "TEST": os.getenv("TEST")
}