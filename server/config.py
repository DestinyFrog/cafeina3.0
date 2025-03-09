from dotenv import load_dotenv
import os

load_dotenv()

API_PREFIX = os.getenv("API_PREFIX")
PORT = os.getenv("PORT")
MODE = os.getenv("MODE")