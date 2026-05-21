# 🗂️ File Organizer - Automatic File Management System

A powerful, user-friendly Python application to automatically organize files into categories based on their extensions. Supports scheduled automation, customizable configuration, and detailed logging.

## ✨ Features

- **📁 Smart File Organization**: Automatically sorts files into categories (Documents, Images, Media, Archives, Applications, Code, Others)
- **⚙️ Customizable Configuration**: Edit `config.json` to define your own file categories and extensions
- **⏰ Scheduled Automation**: Run organization at a specific time daily (default: 8 PM)
- **👁️ Preview Mode**: Use dry-run feature to see what would be moved without making changes
- **📊 Statistics & Monitoring**: View folder statistics and organization history
- **📝 Detailed Logging**: All operations are logged to a file for audit trail
- **🛡️ Safe Operations**: Automatic duplicate handling, permission checking, error recovery
- **🎯 Smart Exclusions**: Skip system files, temporary files, and specified folders

## 📋 Requirements

- Python 3.7+
- schedule library (install via pip)

## 🚀 Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or install schedule directly:
   ```bash
   pip install schedule
   ```

## 📖 Usage

### Run the Application

```bash
python main.py
```

This will start the interactive menu where you can:

1. **Organize files now** - Manually trigger file organization
2. **Enable/Disable scheduling** - Set up automatic organization at a specific time
3. **View stats** - See folder statistics and file breakdown
4. **View configuration** - Check current settings and file categories
5. **Edit target directory** - Change the folder to organize
6. **Preview changes** - Dry-run mode to see what would be moved
7. **View logs** - Check recent operations and history

### Configuration (config.json)

The `config.json` file controls all aspects of the organizer:

```json
{
  "general": {
    "target_directory": "./Downloads",     // Directory to organize
    "enable_scheduling": true,             // Auto-run at schedule_time
    "schedule_time": "20:00",              // Time format: HH:MM (24-hour)
    "dry_run": false,                      // Preview without moving files
    "enable_logging": true,                // Log all operations
    "log_file": "./logs/file_organizer.log"
  },
  "exclude": {
    "folders": [".venv", "node_modules"],  // Folders to skip
    "files": ["Thumbs.db", ".DS_Store"]    // Files to skip
  },
  "file_categories": {
    "Documents": {
      "extensions": [".pdf", ".docx", ...],
      "description": "Word documents, PDFs, ..."
    },
    // ... more categories
  }
}
```

### Example Configurations

#### Quick Setup
Change `target_directory` to your Downloads folder:
```json
"target_directory": "C:/Users/YourName/Downloads"
```

#### Change Schedule Time
To run at 9 PM instead:
```json
"schedule_time": "21:00"
```

#### Disable Scheduling
```json
"enable_scheduling": false
```

#### Preview Mode
To test without moving files:
```json
"dry_run": true
```

#### Add Custom Categories
Edit `file_categories` in config.json:
```json
"Videos": {
  "extensions": [".mp4", ".mkv", ".avi"],
  "description": "Video files"
}
```

## 📁 Project Structure

```
file_organizer/
├── main.py              # Main application with interactive menu
├── utils.py             # Helper functions and utilities
├── config.json          # Configuration file (customize here!)
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── logs/                # Log files (created automatically)
    └── file_organizer.log
```

## 🔧 How It Works

1. **Reads Configuration**: Loads settings from `config.json`
2. **Scans Directory**: Lists all files in target directory
3. **Categorizes Files**: Matches file extensions to categories
4. **Creates Folders**: Makes category folders if they don't exist
5. **Moves Files**: Moves files to appropriate folders
6. **Handles Conflicts**: Appends counters to duplicate filenames
7. **Logs Operations**: Records all actions to log file
8. **Shows Summary**: Displays how many files were organized

## 📊 File Organization Example

**Before:**
```
📂 Downloads/
 ├── thesis.pdf
 ├── photo.jpg
 ├── song.mp3
 ├── archive.zip
 └── installer.exe
```

**After:**
```
📂 Downloads/
 ├── 📂 Documents/
 │   └── thesis.pdf
 ├── 📂 Images/
 │   └── photo.jpg
 ├── 📂 Media/
 │   └── song.mp3
 ├── 📂 Archives/
 │   └── archive.zip
 └── 📂 Applications/
     └── installer.exe
```

## 🎯 Common Tasks

### Organize Downloads Folder
1. Update `config.json` target_directory to your Downloads path
2. Choose option 1 from menu or enable scheduling for automatic runs

### Test Before Applying
1. Choose option 6 (Preview/Dry-run)
2. Review what would be moved
3. If satisfied, disable dry_run in config and run again

### View Organization History
1. Choose option 7 from menu
2. View recent log entries showing all moved files

### Add New File Category
1. Edit `config.json`
2. Add new category with extensions:
   ```json
   "Spreadsheets": {
     "extensions": [".xlsx", ".csv", ".ods"],
     "description": "Spreadsheet files"
   }
   ```
3. Restart application

### Exclude Certain Files
1. Edit `exclude.files` in `config.json`
2. Add filename or extension patterns
3. These files will be skipped during organization

## ⏰ Scheduling Guide

The scheduler runs at the specified time daily:
- Default: **20:00** (8 PM)
- Format: 24-hour time (HH:MM)
- Examples:
  - 09:00 = 9 AM
  - 14:30 = 2:30 PM
  - 23:59 = 11:59 PM

To enable scheduling:
1. Run application: `python main.py`
2. Choose option 2 (Enable/Disable scheduling)
3. Answer 'y' to enable
4. Scheduler will run in background at specified time

## 📝 Logging

All operations are logged to `logs/file_organizer.log`:
- File movements
- Folder creations
- Errors and warnings
- Scheduling events

Check logs via menu option 7 or directly open the log file.

## ⚠️ Important Notes

- **Backup**: Always backup important files before running on new directories
- **Permissions**: Script needs read/write permissions on target directory
- **Dry-run**: Use preview mode first on new directories
- **Extensions**: Configure extensions in config.json to match your needs
- **Special Characters**: Vietnamese and Unicode filenames are supported

## 🐛 Troubleshooting

### "Directory not found" Error
- Check `target_directory` in config.json
- Ensure path exists and is accessible
- Use forward slashes (/) in paths

### Schedule Not Running
- Ensure `enable_scheduling` is `true` in config.json
- Check that application is still running
- Verify `schedule_time` format is correct (HH:MM)

### Files Not Moving
- Check if files are in `exclude.files` list
- Verify file extensions are in your categories
- Check file permissions
- View logs for specific error messages

### Permission Denied
- Run script with appropriate permissions
- On Windows: Run as Administrator if needed
- Check folder permissions

## 📞 Support

For issues or questions:
1. Check the logs: option 7 in menu
2. Review your config.json for errors
3. Use dry-run mode (option 6) to test

## 📄 License

This project is open source and available for personal and commercial use.

## 🎉 Tips & Tricks

- Use dry-run mode frequently to preview changes
- Customize categories in config.json for your needs
- Set up scheduling to run during off-peak hours
- Regularly check logs to monitor operations
- Exclude system folders to avoid accidentally organizing them
- Create test folders to verify behavior before using on important directories

## 🚀 Future Enhancements

Potential features for future versions:
- GUI interface
- Multiple directory support
- File pattern matching (regex)
- Smart categorization based on content
- Backup/Restore functionality
- Performance optimization
- Cross-platform GUI

---

**Made with ❤️ for organizing your digital life**
