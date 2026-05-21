# Quick Start Guide - File Organizer

## 🎯 5-Minute Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Target Directory
Edit `config.json` and change the `target_directory`:

From:
```json
"target_directory": "./Downloads"
```

To your actual folder (Windows example):
```json
"target_directory": "C:/Users/YourName/Downloads"
```

Or Linux/Mac:
```json
"target_directory": "/home/username/Downloads"
```

### Step 3: Run the Application
```bash
python main.py
```

### Step 4: Choose an Option
```
1. Organize files now - Sort files immediately
6. Preview changes - See what would happen first (RECOMMENDED)
2. Enable/Disable scheduled organization - Auto-run daily
```

## 📋 Default Configuration

The application comes with pre-configured categories:

| Category | File Types | Examples |
|----------|-----------|----------|
| **Documents** | .pdf, .docx, .txt, .xlsx, .pptx | Reports, Spreadsheets, Presentations |
| **Images** | .jpg, .png, .gif, .svg | Photos, Graphics |
| **Media** | .mp3, .mp4, .mkv, .wav | Music, Videos |
| **Archives** | .zip, .rar, .tar.gz | Compressed files |
| **Applications** | .exe, .msi, .app | Installers |
| **Code** | .py, .js, .java, .cpp | Source code |
| **Others** | (anything else) | Uncategorized |

## 🔧 Common Customizations

### Add a New Category
Edit `config.json`, in `file_categories`:

```json
"Games": {
  "extensions": [".exe", ".iso", ".msi"],
  "description": "Game installers and files"
}
```

### Change Schedule Time
Edit `schedule_time` in `config.json` (24-hour format):

- 08:00 = 8 AM
- 14:00 = 2 PM
- 20:00 = 8 PM
- 23:00 = 11 PM

### Exclude Files/Folders
Edit `exclude` in `config.json`:

```json
"exclude": {
  "folders": [".venv", "important_folder"],
  "files": ["keep_this.txt", ".DS_Store"]
}
```

### Enable Dry-run Mode
Edit `config.json`:
```json
"dry_run": true
```

## ⏰ Schedule Setup

To run automatically every day at 8 PM:

1. Run `python main.py`
2. Select option 2: "Enable/Disable scheduled organization"
3. Type `y` to enable
4. Application will run in background and trigger at 8 PM each day
5. Press Ctrl+C to stop scheduling

## 📊 View Statistics

From the menu, choose option 3 to see:
- Total files organized
- Total folder size
- Breakdown by category
- Files in each category

## 👁️ Preview Mode (Recommended First Step!)

**Always preview before running on important folders:**

1. From menu, choose option 6: "Preview changes"
2. See what files would be moved (no actual changes)
3. Review the summary
4. If satisfied, disable `dry_run` in config.json and run again

## 🚨 Safety Tips

✅ **DO:**
- Use preview mode first (option 6)
- Backup important folders before first run
- Start with a test folder
- Check logs regularly (option 7)
- Review config.json carefully

❌ **DON'T:**
- Run on system folders without testing
- Disable logging
- Exclude too many files
- Delete the config.json file

## 📞 Getting Help

Inside the application:
- Option 4: View current configuration
- Option 7: View recent logs
- Option 3: View statistics

Outside the application:
- Check `logs/file_organizer.log` file
- Review `README.md` for detailed guide
- Edit `config.json` to adjust settings

## 🎓 Examples

### Example 1: Organize Downloads Folder

**config.json:**
```json
"target_directory": "C:/Users/YourName/Downloads"
```

**Run:**
```
python main.py → Option 6 (Preview) → Option 1 (Organize)
```

### Example 2: Daily Auto-Organization at 8 PM

**config.json:**
```json
"enable_scheduling": true,
"schedule_time": "20:00"
```

**Run:**
```
python main.py → Option 2 (Enable scheduling) → Y
```

Leave the application running, and it will automatically organize at 8 PM every day.

### Example 3: Custom Categories for Work Projects

**config.json - Add new category:**
```json
"Projects": {
  "extensions": [".project", ".psd", ".sketch"],
  "description": "Design project files"
}
```

## 🎉 You're Ready!

1. ✅ Dependencies installed
2. ✅ Configuration updated
3. ✅ Ready to organize!

**Next Step:** Run `python main.py` and choose option 6 to preview!

---

**Need more help?** See README.md for the full documentation.
