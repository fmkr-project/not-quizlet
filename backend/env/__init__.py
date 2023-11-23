"""The env is to load environmental variables securely in case we need to host it, file access would only be from server-side"""
from dotenv import load_dotenv
load_dotenv()