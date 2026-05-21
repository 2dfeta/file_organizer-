# Configuration Examples for File Organizer

This file contains example configurations for different use cases.

## Example 1: Default Configuration (Balanced)

Best for: General users organizing Downloads folder

```json
{
  "general": {
    "target_directory": "./Downloads",
    "enable_scheduling": true,
    "schedule_time": "20:00",
    "dry_run": false,
    "enable_logging": true,
    "log_file": "./logs/file_organizer.log"
  },
  "exclude": {
    "folders": [".venv", "node_modules", "__pycache__", ".git"],
    "files": ["Thumbs.db", ".DS_Store", "desktop.ini"]
  },
  "file_categories": {
    "Documents": {
      "extensions": [".pdf", ".docx", ".txt", ".xlsx"],
      "description": "Documents"
    },
    "Images": {
      "extensions": [".jpg", ".png", ".gif"],
      "description": "Images"
    },
    "Media": {
      "extensions": [".mp3", ".mp4"],
      "description": "Media files"
    }
  }
}
```

## Example 2: Developer Workspace

Best for: Developers with many code and project files

```json
{
  "general": {
    "target_directory": "./Downloads",
    "enable_scheduling": true,
    "schedule_time": "22:00",
    "dry_run": false,
    "enable_logging": true,
    "log_file": "./logs/file_organizer.log"
  },
  "exclude": {
    "folders": [".venv", "node_modules", ".git", "venv", "env", ".env", "build", "dist"],
    "files": [".DS_Store", "Thumbs.db", ".gitignore"]
  },
  "file_categories": {
    "Code": {
      "extensions": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".html", ".css"],
      "description": "Source code"
    },
    "Projects": {
      "extensions": [".project", ".sln", ".xcodeproj"],
      "description": "Project files"
    },
    "Documentation": {
      "extensions": [".md", ".rst", ".txt", ".pdf"],
      "description": "Docs"
    },
    "Archives": {
      "extensions": [".zip", ".tar.gz", ".7z"],
      "description": "Archives"
    }
  }
}
```

## Example 3: Media Professional

Best for: Photographers, designers, video editors

```json
{
  "general": {
    "target_directory": "D:/Creative/Inbox",
    "enable_scheduling": false,
    "schedule_time": "19:00",
    "dry_run": true,
    "enable_logging": true,
    "log_file": "D:/Creative/Logs/organizer.log"
  },
  "exclude": {
    "folders": [".backup", "archive", ".versions"],
    "files": ["temp.psd", ".DS_Store", "Thumbs.db"]
  },
  "file_categories": {
    "Photos": {
      "extensions": [".jpg", ".jpeg", ".raw", ".dng", ".tiff", ".png"],
      "description": "Photography"
    },
    "Design": {
      "extensions": [".psd", ".ai", ".svg", ".sketch", ".xd"],
      "description": "Design files"
    },
    "Video": {
      "extensions": [".mp4", ".mov", ".mkv", ".avi", ".prproj"],
      "description": "Video files"
    },
    "Audio": {
      "extensions": [".mp3", ".wav", ".flac", ".aac"],
      "description": "Audio files"
    }
  }
}
```

## Example 4: Business User

Best for: Business, accounting, HR, project management

```json
{
  "general": {
    "target_directory": "C:/Users/BusinessUser/Downloads",
    "enable_scheduling": true,
    "schedule_time": "17:30",
    "dry_run": false,
    "enable_logging": true,
    "log_file": "C:/Users/BusinessUser/AppData/file_organizer.log"
  },
  "exclude": {
    "folders": ["archive", "backup", "old"],
    "files": ["temp.xls", "~temp.docx", ".DS_Store"]
  },
  "file_categories": {
    "Reports": {
      "extensions": [".pdf", ".xlsx", ".pptx"],
      "description": "Business reports"
    },
    "Contracts": {
      "extensions": [".docx", ".pdf", ".txt"],
      "description": "Legal documents"
    },
    "Invoices": {
      "extensions": [".xlsx", ".pdf", ".csv"],
      "description": "Invoices"
    },
    "Communications": {
      "extensions": [".eml", ".msg", ".pdf"],
      "description": "Emails and communications"
    }
  }
}
```

## Example 5: Content Creator

Best for: YouTubers, streamers, podcasters

```json
{
  "general": {
    "target_directory": "E:/RawContent",
    "enable_scheduling": true,
    "schedule_time": "09:00",
    "dry_run": false,
    "enable_logging": true,
    "log_file": "E:/RawContent/logs/organizer.log"
  },
  "exclude": {
    "folders": [".cache", "temp", "working"],
    "files": [".DS_Store", "Thumbs.db"]
  },
  "file_categories": {
    "Raw_Video": {
      "extensions": [".mov", ".mp4", ".mkv", ".avi", ".mxf"],
      "description": "Raw video files"
    },
    "Raw_Audio": {
      "extensions": [".wav", ".aac", ".mp3", ".flac"],
      "description": "Audio files"
    },
    "Graphics": {
      "extensions": [".psd", ".jpg", ".png", ".svg", ".gif"],
      "description": "Thumbnails and graphics"
    },
    "Subtitles": {
      "extensions": [".srt", ".vtt", ".ass"],
      "description": "Subtitle files"
    }
  }
}
```

## Example 6: Minimal Configuration (Dry-run)

Best for: Testing before actual use

```json
{
  "general": {
    "target_directory": "./test_folder",
    "enable_scheduling": false,
    "schedule_time": "20:00",
    "dry_run": true,
    "enable_logging": true,
    "log_file": "./logs/test.log"
  },
  "exclude": {
    "folders": [],
    "files": []
  },
  "file_categories": {
    "Documents": {
      "extensions": [".pdf", ".docx", ".txt"],
      "description": "Documents"
    },
    "Images": {
      "extensions": [".jpg", ".png", ".gif"],
      "description": "Images"
    },
    "Media": {
      "extensions": [".mp3", ".mp4"],
      "description": "Media"
    }
  }
}
```

## How to Use These Examples

1. **Copy the JSON** from the example you want
2. **Paste it** into your `config.json` file
3. **Modify the paths** to match your system:
   - Windows: `C:/Users/YourName/Downloads`
   - Linux/Mac: `/home/username/Downloads`
4. **Adjust extensions** if needed
5. **Run setup.py** to verify: `python setup.py`
6. **Use dry-run first**: Set `"dry_run": true` and run `python main.py`
7. **Review changes** before disabling dry-run

## Tips for Creating Custom Configurations

- **test_first**: Always use `"dry_run": true` initially
- **exclude_carefully**: Add system folders to exclude list
- **schedule_wisely**: Choose times when computer is usually on
- **keep_backups**: Back up config.json before major changes
- **add_extensions**: Include all variations of file types
- **meaningful_names**: Use clear category names

## Platform-Specific Paths

### Windows
```
C:/Users/Username/Downloads
C:/Users/Username/Documents
D:/Creative/Projects
```

### Linux
```
/home/username/Downloads
/home/username/Documents
/media/storage/Projects
```

### macOS
```
/Users/username/Downloads
/Users/username/Documents
/Volumes/External/Projects
```

---

**Need help?** See README.md or QUICKSTART.md
