# 🗂️ File Organizer - Complete User Manual

A sophisticated, production-ready Python application for automatic file organization with scheduling support, detailed logging, and extensive customization options.

---

## 📚 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Core Features](#core-features)
4. [Configuration](#configuration)
5. [Usage Guide](#usage-guide)
6. [Scheduling](#scheduling)
7. [Advanced Features](#advanced-features)
8. [Troubleshooting](#troubleshooting)
9. [Command Reference](#command-reference)

---

## ⚡ Quick Start

### Windows
```bash
# Double-click run.bat
# OR run in Command Prompt:
python main.py
```

### Linux/Mac
```bash
# Make script executable
chmod +x run.sh

# Run it
./run.sh

# OR directly
python3 main.py
```

### First Time Setup
1. Run `python setup.py` to verify installation
2. Run `python demo.py` to create test files
3. Run `python main.py` and choose option 6 (Preview)
4. Review changes, then run option 1 (Organize)

---

## 💾 Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)
- 50 MB free disk space

### Step 1: Install Python
- **Windows**: Download from https://www.python.org
- **Ubuntu**: `sudo apt-get install python3 python3-pip`
- **macOS**: `brew install python3`

### Step 2: Install Dependencies
```bash
# Option A: Using requirements file
pip install -r requirements.txt

# Option B: Manual installation
pip install schedule

# On macOS, you might need:
pip3 install schedule
```

### Step 3: Verify Installation
```bash
python setup.py
```

Expected output:
```
✓ Python Version
✓ Dependencies
✓ Config File
✓ File Permissions
✓ Logs Directory
```

---

## ✨ Core Features

### 1. Smart File Organization
- Automatically categorizes files by extension
- Creates organized folder structure
- Prevents file overwrites with automatic renaming

### 2. Customizable Configuration
- JSON-based configuration
- Define your own categories and extensions
- Exclude specific files/folders

### 3. Scheduled Automation
- Run at specific times daily (default: 8 PM)
- Background scheduling with minute-level precision
- Automatic logging of scheduled operations

### 4. Preview Mode (Dry-run)
- See exactly what would be moved
- No actual changes made
- Perfect for testing new configurations

### 5. Comprehensive Logging
- All operations logged to file
- View logs from menu or directly
- Audit trail for compliance

### 6. User-Friendly Interface
- Interactive menu system
- Real-time feedback during operations
- Detailed statistics and reports

### 7. Error Handling
- Graceful error recovery
- Permission checking
- Detailed error messages in logs

### 8. Exclusion System
- Skip system folders (.venv, node_modules, etc.)
- Exclude specific files (Thumbs.db, .DS_Store)
- Configurable via config.json

---

## ⚙️ Configuration

### Config File Location
`config.json` in the application directory

### Main Sections

#### general
```json
{
  "general": {
    "target_directory": "./Downloads",      // Folder to organize
    "enable_scheduling": true,              // Auto-run feature
    "schedule_time": "20:00",               // 24-hour format (HH:MM)
    "dry_run": false,                       // Preview mode
    "enable_logging": true,                 // Save logs
    "log_file": "./logs/file_organizer.log" // Log location
  }
}
```

#### exclude
```json
{
  "exclude": {
    "folders": [".venv", "node_modules"],   // Skip these folders
    "files": ["Thumbs.db", ".DS_Store"]     // Skip these files
  }
}
```

#### file_categories
```json
{
  "file_categories": {
    "CategoryName": {
      "extensions": [".ext1", ".ext2"],     // File types
      "description": "Human-readable name"  // Description
    }
  }
}
```

### Quick Configuration Changes

**Change target directory:**
```json
"target_directory": "C:/Users/YourName/Downloads"
```

**Change schedule time to 9 AM:**
```json
"schedule_time": "09:00"
```

**Add new category:**
```json
"Videos": {
  "extensions": [".mp4", ".mkv", ".avi"],
  "description": "Video files"
}
```

**Disable scheduling:**
```json
"enable_scheduling": false
```

**Enable preview mode:**
```json
"dry_run": true
```

---

## 🎯 Usage Guide

### Starting the Application

**Windows:**
```batch
python main.py
```

**Linux/Mac:**
```bash
python3 main.py
```

### Menu Options

```
1. Organize files now (one-time)
   └─ Immediately organize target directory

2. Enable/Disable scheduled organization
   └─ Set up automatic daily organization

3. View organization stats
   └─ See breakdown by category and size

4. View current configuration
   └─ Review all settings and categories

5. Edit target directory
   └─ Change folder to organize

6. Preview changes (dry-run)
   └─ See what would be moved (no actual changes)

7. View recent logs
   └─ Check operation history

8. Exit
   └─ Close the application
```

### Typical Workflow

1. **First Time:**
   - Option 5: Set target directory
   - Option 6: Preview changes
   - Option 1: Organize files

2. **Daily Use:**
   - Option 2: Enable scheduling
   - App runs automatically at scheduled time
   - Option 7: Check logs occasionally

3. **Maintenance:**
   - Option 4: Review configuration
   - Option 3: Check statistics
   - Option 7: Monitor logs

---

## ⏰ Scheduling

### Enable Scheduling

1. Run `python main.py`
2. Choose option 2: "Enable/Disable scheduled organization"
3. Type `y` when prompted
4. Application will run in background

### Schedule Times

Format: 24-hour time (HH:MM)

| Time | Format | Usage |
|------|--------|-------|
| 8:00 AM | 08:00 | Morning cleanup |
| 12:00 PM | 12:00 | Midday organization |
| 5:00 PM | 17:00 | End of work day |
| 8:00 PM | 20:00 | Evening cleanup (default) |
| 11:00 PM | 23:00 | Late night |

### Change Schedule Time

Edit `config.json`:
```json
"schedule_time": "21:00"  // Changes to 9 PM
```

### Background Operation

- Scheduler runs in application foreground
- Monitor processes to see it running
- Press Ctrl+C to stop

### Windows Task Scheduler

To run automatically on system startup:

1. Open Task Scheduler (search "Task Scheduler")
2. Create Basic Task
3. Set trigger: "At startup"
4. Set action: Start program
   - Program: `python.exe`
   - Arguments: `C:\path\to\main.py`
5. Click OK

---

## 🔧 Advanced Features

### Dry-run Mode

Test before actual execution:
```json
"dry_run": true
```

Output shows what would happen without making changes.

### Custom Categories

Add to `file_categories`:
```json
"Research": {
  "extensions": [".pdf", ".doc", ".bib", ".csv"],
  "description": "Research documents"
}
```

### Exclude Patterns

Skip important files:
```json
"exclude": {
  "folders": ["Archive", "Keep", "Important"],
  "files": ["do_not_move.txt", "keep_this.pdf"]
}
```

### Logging Options

```json
"enable_logging": true,              // Turn logging on/off
"log_file": "./logs/custom_log.log"  // Custom log location
```

### Multiple Categories for Same Extension

Extensions are searched in order, first match wins.

---

## 🐛 Troubleshooting

### Issue: "Target directory not found"
**Solution:**
1. Verify path in config.json
2. Check path exists on your system
3. Use absolute path instead of relative

### Issue: "Permission denied"
**Solution:**
1. Run with appropriate permissions
2. On Windows: Run as Administrator
3. On Linux/Mac: Check folder permissions

### Issue: "schedule library not found"
**Solution:**
```bash
pip install schedule
```

### Issue: No files being moved
**Solution:**
1. Check file extensions in config
2. Verify target directory path
3. Review logs for errors
4. Test with dry-run mode first

### Issue: Application crashes
**Solution:**
1. Check log file for errors
2. Verify config.json is valid JSON
3. Run setup.py to verify installation
4. Check file permissions

### Viewing Logs

**From menu:**
- Choose option 7: "View recent logs"

**Directly:**
- Open `logs/file_organizer.log`
- On Windows: Notepad
- On Linux/Mac: `cat logs/file_organizer.log`

---

## 🔍 Command Reference

### Running Application

```bash
python main.py              # Run main application
python demo.py              # Create demo files
python setup.py             # Verify installation
python run.bat              # Windows launcher
./run.sh                    # Linux/Mac launcher
```

### Installation

```bash
pip install -r requirements.txt  # Install dependencies
pip install schedule              # Install schedule package
pip install --upgrade schedule    # Upgrade to latest
```

### File Locations

```
File Organizer/
├── main.py                  # Main application
├── utils.py                 # Helper functions
├── config.json              # Configuration
├── requirements.txt         # Dependencies
├── setup.py                 # Setup verification
├── demo.py                  # Demo file creator
├── run.bat                  # Windows launcher
├── run.sh                   # Linux/Mac launcher
├── README.md                # Full documentation
├── QUICKSTART.md            # Quick start guide
├── CONFIG_EXAMPLES.md       # Configuration examples
├── MANUAL.md                # This file
└── logs/                    # Log directory
    └── file_organizer.log   # Application logs
```

### Log Format

```
2024-05-21 20:00:15 - INFO - File Organizer started
2024-05-21 20:00:16 - INFO - Starting organization for directory: ./Downloads
2024-05-21 20:00:16 - INFO - Created folder: Documents
2024-05-21 20:00:16 - INFO - Moved file: thesis.pdf -> Documents/thesis.pdf
2024-05-21 20:00:17 - INFO - Organization complete. Moved: 5, Skipped: 0, Errors: 0
```

---

## 💡 Best Practices

### Do's ✅
- Use dry-run mode first on new directories
- Back up important folders before first run
- Review logs regularly
- Keep config.json organized
- Test with demo folder first
- Set appropriate schedule times
- Exclude system folders

### Don'ts ❌
- Don't run on critical system directories
- Don't disable logging on important tasks
- Don't modify files while organizing
- Don't delete config.json without backup
- Don't run multiple instances simultaneously
- Don't exclude everything
- Don't ignore errors in logs

---

## 🎓 Examples

### Example 1: Organize Downloads at 8 PM Daily

1. Edit `config.json`:
```json
{
  "target_directory": "C:/Users/YourName/Downloads",
  "schedule_time": "20:00",
  "enable_scheduling": true
}
```

2. Run: `python main.py`
3. Choose: Option 2, type `y`
4. Keep application running

### Example 2: Test First, Then Deploy

1. Choose option 6: Preview changes
2. Review output
3. If satisfied, set `"dry_run": false` in config
4. Run option 1: Organize files

### Example 3: Add Custom Category for Projects

1. Edit `config.json`
2. Add:
```json
"Projects": {
  "extensions": [".project", ".psd", ".figma"],
  "description": "Design projects"
}
```

3. Run application
4. Option 1: Organize files

---

## 📞 Support & Help

### Getting Help
1. Review README.md for full documentation
2. Check QUICKSTART.md for common tasks
3. See CONFIG_EXAMPLES.md for configuration ideas
4. View application logs for detailed errors
5. Run setup.py to verify installation

### Common Questions

**Q: How often does the scheduler run?**
A: Once daily at the specified time

**Q: Can I organize multiple directories?**
A: Configure target_directory for each
Multiple runs needed

**Q: How do I change the schedule time?**
A: Edit `schedule_time` in config.json (24-hour format)

**Q: Will it overwrite existing files?**
A: No, it appends _1, _2, etc. to duplicates

**Q: Can I undo organization?**
A: Check logs to see where files moved
Manually restore from backups

---

## ✅ Verification Checklist

Before using on important folders:

- [ ] Python installed (check: `python --version`)
- [ ] Dependencies installed (check: `pip list | grep schedule`)
- [ ] config.json updated with correct path
- [ ] setup.py passes all checks
- [ ] Demo folder created and tested
- [ ] Dry-run preview verified
- [ ] Logs directory exists
- [ ] Excluded folders configured
- [ ] Backup of important files created
- [ ] Scheduler time set correctly (if using)

---

## 🎉 Summary

File Organizer is a complete, production-ready solution for automatic file organization. Start with the Quick Start section, use the menu interface, and refer to this manual for advanced features.

**Happy organizing!** 🗂️

---

*Version 2.0 - May 2024*
*Last updated: 2024-05-21*
