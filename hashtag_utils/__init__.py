import dotenv
import os
import sys
from .hashtag_utils import HashtagUtils

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path
sys.path.append(parent_directory)

env_path = os.path.join(os.getcwd(), ".env")


dotenv.load_dotenv(env_path)
