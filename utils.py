import os
import json
import logging
from datetime import datetime
from typing import Dict, Optional, Any

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load and validate configuration from JSON file.
    Returns the configuration dictionary or raises an exception if invalid.
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Validate required keys
        required_keys = ["general", "file_categories", "exclude"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key: {key}")
        
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {e}")

def setup_logging(log_file: str, enable: bool = True) -> logging.Logger:
    """
    Setup logging configuration.
    """
    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    logger.handlers.clear()
    
    if not enable:
        logger.addHandler(logging.NullHandler())
        return logger
    
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def get_file_extension(file_path: str) -> str:
    """
    Extract and return the lowercase file extension.
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def should_exclude(item: str, exclude_config: Dict[str, Any]) -> bool:
    """
    Check if a file/folder should be excluded based on exclude configuration.
    """
    # Check if it's in excluded files list
    if item in exclude_config.get("files", []):
        return True
    
    # For folders, check if the folder name is in excluded folders
    if item in exclude_config.get("folders", []):
        return True
    
    return False

def resolve_duplicate(target_path: str) -> str:
    """
    Handle name collisions. If a file already exists at the destination,
    append a counter (e.g., _1, _2) to prevent overwriting.
    """
    if not os.path.exists(target_path):
        return target_path
    
    base, ext = os.path.splitext(target_path)
    counter = 1
    
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    
    return f"{base}_{counter}{ext}"

def find_category_for_extension(ext: str, file_categories: Dict[str, Any]) -> Optional[str]:
    """
    Find the category folder name for a given file extension.
    Returns None if extension is not found in any category.
    """
    for category_name, category_info in file_categories.items():
        if ext in category_info.get("extensions", []):
            return category_name
    return None

def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Get detailed information about a file.
    """
    try:
        stat_info = os.stat(file_path)
        return {
            "path": file_path,
            "name": os.path.basename(file_path),
            "size": stat_info.st_size,
            "modified": datetime.fromtimestamp(stat_info.st_mtime),
            "is_file": os.path.isfile(file_path),
            "is_dir": os.path.isdir(file_path)
        }
    except Exception as e:
        return {"error": str(e)}

def ensure_directory_exists(directory: str) -> bool:
    """
    Ensure a directory exists, creating it if necessary.
    Returns True if successful, False otherwise.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        print(f"Failed to create directory {directory}: {e}")
        return False

def format_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    """
    size_float: float = float(size_bytes)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_float < 1024.0:
            return f"{size_float:.2f} {unit}"
        size_float /= 1024.0
    return f"{size_float:.2f} TB"

def get_folder_size(folder_path: str) -> int:
    """
    Calculate total size of all files in a folder.
    """
    total_size: int = 0
    try:
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except Exception:
                    pass
    except Exception:
        pass
    return total_size

def count_files(folder_path: str) -> int:
    """
    Count total number of files in a folder (including subdirectories).
    """
    count: int = 0
    try:
        for _, _, filenames in os.walk(folder_path):
            count += len(filenames)
    except Exception:
        pass
    return count
