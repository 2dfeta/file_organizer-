# 🗂️ File Organizer - Project Overview

Welcome to File Organizer! This is a complete, professional-grade file organization system.

## 📂 Project Structure

```
file_organizer/
├── 📄 MAIN APPLICATION FILES
│   ├── main.py              ⭐ Main application (run this!)
│   ├── utils.py             Utility functions
│   └── config.json          Configuration file (EDIT THIS!)
│
├── 📚 DOCUMENTATION
│   ├── README.md            Complete documentation
│   ├── QUICKSTART.md        5-minute setup guide
│   ├── MANUAL.md            Complete user manual
│   ├── CONFIG_EXAMPLES.md   Configuration examples
│   └── INDEX.md             This file
│
├── 🛠️ SETUP & UTILITIES
│   ├── setup.py             Verify installation
│   ├── demo.py              Create demo files
│   ├── requirements.txt     Python dependencies
│   ├── run.bat              Windows launcher
│   └── run.sh               Linux/Mac launcher
│
├── 📁 RUNTIME DIRECTORIES
│   ├── demo_files/          Demo folder with sample files
│   ├── logs/                Application logs
│   └── .venv/               Python virtual environment
│
└── 🌳 VENV (Development)
    └── .venv/               Virtual environment (optional)
```

## 🚀 Quick Start (Choose One)

### Option 1: Windows (Easiest)
```bash
# Double-click:
run.bat

# OR run in Command Prompt:
python main.py
```

### Option 2: Linux/Mac
```bash
chmod +x run.sh
./run.sh

# OR directly:
python3 main.py
```

### Option 3: First Time Setup
```bash
python setup.py    # Verify installation
python demo.py     # Create test files
python main.py     # Run application
```

## 📖 Documentation Guide

Choose based on your need:

| Document | Best For | Time |
|----------|----------|------|
| **QUICKSTART.md** | Getting started quickly | 5 min |
| **README.md** | Understanding all features | 15 min |
| **MANUAL.md** | Complete reference guide | 30 min |
| **CONFIG_EXAMPLES.md** | Configuration templates | 10 min |

## 🎯 What This Does

Automatically organizes files into categories:

**Before:**
```
📂 Downloads/
 ├── document.pdf
 ├── photo.jpg
 ├── song.mp3
 └── archive.zip
```

**After:**
```
📂 Downloads/
 ├── 📂 Documents/ ← document.pdf
 ├── 📂 Images/    ← photo.jpg
 ├── 📂 Media/     ← song.mp3
 └── 📂 Archives/  ← archive.zip
```

## ⚙️ Key Features

✅ **Smart Organization** - Automatic file categorization
✅ **Customizable** - Define your own categories in config.json
✅ **Scheduled** - Run automatically daily at any time (e.g., 8 PM)
✅ **Safe** - Preview mode, duplicate handling, error recovery
✅ **Logged** - Complete audit trail of all operations
✅ **User-Friendly** - Interactive menu interface
✅ **Fast** - Organize hundreds of files in seconds
✅ **Reliable** - Comprehensive error handling

## 🔧 Configuration

Edit `config.json` to customize:

```json
{
  "general": {
    "target_directory": "./Downloads",   // Your folder here!
    "schedule_time": "20:00",            // Run at 8 PM
    "enable_scheduling": true            // Auto-organize
  },
  
  "file_categories": {
    "MyCategory": {
      "extensions": [".ext1", ".ext2"]
    }
  }
}
```

## 📋 Common Tasks

### 1. First Time Use
```bash
python demo.py      # Create sample files
python main.py      # Run app
# Choose option 6: Preview changes
# Review output
# Choose option 1: Organize
```

### 2. Organize Real Folder
```
1. Edit config.json, change target_directory
2. Run python main.py
3. Choose option 6: Preview
4. Choose option 1: Organize
```

### 3. Schedule Daily Run at 8 PM
```
1. python main.py
2. Choose option 2: Enable scheduling
3. Answer 'y'
4. Keep window open or use Task Scheduler
```

### 4. Add New File Category
```
1. Edit config.json
2. Add new category with extensions
3. Run application
4. Organize files
```

## ⏰ Scheduling

**Run automatically at 8 PM daily:**

1. python main.py
2. Choose option 2
3. Type 'y'
4. Application runs in background

**Change time:**
Edit config.json `"schedule_time": "21:00"` (9 PM)

## 🎯 Menu Overview

```
1️⃣  Organize files now          - Move files immediately
2️⃣  Enable/Disable scheduling    - Daily auto-organization
3️⃣  View organization stats      - Statistics & breakdown
4️⃣  View current configuration   - Review all settings
5️⃣  Edit target directory        - Change folder
6️⃣  Preview changes (dry-run)    - See what would happen
7️⃣  View recent logs             - Check operation history
8️⃣  Exit                         - Close application
```

## 💡 Pro Tips

- **Always preview first** - Use option 6 before option 1
- **Test with demo** - Run `python demo.py` first
- **Check logs** - Option 7 shows what was moved
- **Backup important files** - Before using on real folders
- **Keep config.json** - It's your configuration

## ✅ Before You Start

- [ ] Python installed
- [ ] Read QUICKSTART.md (5 min)
- [ ] Run setup.py (verify installation)
- [ ] Run demo.py (create test files)
- [ ] Review config.json (update target directory)

## 📚 Documentation Files

### README.md
Complete feature documentation, installation guide, usage examples.

### QUICKSTART.md
5-minute setup guide with common configurations.

### MANUAL.md
Comprehensive user manual with all features and troubleshooting.

### CONFIG_EXAMPLES.md
Ready-to-use configuration templates for different scenarios.

### INDEX.md
This file - project overview and quick reference.

## 🔍 Logging & Debugging

**View logs from menu:**
```
Choose option 7: View recent logs
```

**Or read directly:**
```
logs/file_organizer.log
```

**Run setup verification:**
```
python setup.py
```

## 🌍 Supported Platforms

- ✅ **Windows** - Run: `python main.py` or `run.bat`
- ✅ **Linux** - Run: `python3 main.py` or `./run.sh`
- ✅ **macOS** - Run: `python3 main.py` or `./run.sh`

## 🐛 Troubleshooting Quick Guide

| Problem | Solution |
|---------|----------|
| Files not moving | Use option 6 (preview) to debug |
| "Directory not found" | Update `target_directory` in config.json |
| "Permission denied" | Run as Administrator (Windows) |
| Schedule not working | Keep application window open |
| No files organized | Check file extensions in config |

**More help:** See MANUAL.md Troubleshooting section

## 📞 Getting Help

1. **For setup issues:** Run `python setup.py`
2. **For usage questions:** See README.md or MANUAL.md
3. **For configuration help:** Check CONFIG_EXAMPLES.md
4. **For errors:** Review logs (option 7 in menu)

## 🎓 Learning Path

**Beginner:**
1. Read QUICKSTART.md
2. Run demo.py
3. Try menu options 1-3

**Intermediate:**
1. Read README.md
2. Edit config.json
3. Set up scheduling (option 2)

**Advanced:**
1. Read MANUAL.md
2. Create custom categories
3. Set up Task Scheduler (Windows)

## 🎉 Ready to Go!

You're all set! Choose how to start:

```bash
# Easiest - Just run:
python main.py

# Setup - Verify first:
python setup.py

# Demo - Test with samples:
python demo.py

# Windows - Double-click:
run.bat

# Linux/Mac - Run:
./run.sh
```

## 📝 Version Info

- **Version:** 2.0
- **Updated:** May 2024
- **Status:** Production Ready ✅
- **Python:** 3.7+
- **Dependencies:** schedule library

## 📄 License & Attribution

Open source and free to use for personal and commercial purposes.

---

**Enjoy organizing your files!** 🗂️✨

*For detailed information, see the relevant documentation file above.*
