#!/usr/bin/env python3
"""
Demo script for File Organizer
Creates a test folder with sample files for demonstration
"""

import os
import json

def create_demo_folder():
    """Create a demo folder with sample files."""
    demo_dir = "./demo_files"
    
    if not os.path.exists(demo_dir):
        os.makedirs(demo_dir)
        print(f"✓ Created demo folder: {demo_dir}")
    
    # Create sample files
    sample_files = {
        "document1.pdf": "Sample PDF document",
        "report.docx": "Sample Word document",
        "budget.xlsx": "Sample Excel spreadsheet",
        "notes.txt": "Sample text file",
        "photo.jpg": "Sample JPEG image",
        "screenshot.png": "Sample PNG image",
        "wallpaper.gif": "Sample GIF image",
        "song.mp3": "Sample audio file",
        "video.mp4": "Sample video file",
        "archive.zip": "Sample archive",
        "setup.exe": "Sample installer",
        "script.py": "Sample Python script",
        "style.css": "Sample CSS file",
        "index.html": "Sample HTML file",
    }
    
    files_created = 0
    for filename, content in sample_files.items():
        filepath = os.path.join(demo_dir, filename)
        if not os.path.exists(filepath):
            try:
                with open(filepath, 'w') as f:
                    f.write(content)
                files_created += 1
                print(f"  ✓ Created: {filename}")
            except Exception as e:
                print(f"  ❌ Failed to create {filename}: {e}")
    
    print(f"\n✓ Created {files_created} sample files in {demo_dir}/")
    return demo_dir

def update_config_for_demo(demo_dir: str) -> bool:
    """Update config.json to use the demo folder."""
    config_file = "config.json"
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Update target directory
        original_dir = config["general"]["target_directory"]
        config["general"]["target_directory"] = demo_dir
        config["general"]["dry_run"] = False  # Enable actual moves for demo
        
        # Write back
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Updated config.json:")
        print(f"  Target directory: {original_dir} → {demo_dir}")
        print(f"  Dry-run: enabled (no files actually moved)")
        return True
    except Exception as e:
        print(f"❌ Failed to update config: {e}")
        return False

def main():
    """Main demo setup."""
    print("\n" + "="*60)
    print("🎬 FILE ORGANIZER - DEMO SETUP")
    print("="*60 + "\n")
    
    # Create demo folder
    demo_dir = create_demo_folder()
    
    print("\n" + "-"*60)
    print("📋 DEMO FOLDER CONTENTS:")
    print("-"*60)
    try:
        files = sorted(os.listdir(demo_dir))
        for filename in files:
            print(f"  • {filename}")
    except Exception as e:
        print(f"Error listing files: {e}")
    
    # Update config
    print("\n" + "-"*60)
    update_config_for_demo(demo_dir)
    
    print("\n" + "="*60)
    print("🎯 NEXT STEPS:")
    print("="*60)
    print(f"\n1. Run the organizer with demo folder:")
    print(f"   python main.py")
    print(f"\n2. From the menu, choose:")
    print(f"   Option 6 - Preview changes (to see what will happen)")
    print(f"   Option 1 - Organize files now")
    print(f"\n3. Check the results in: {demo_dir}/")
    print(f"\nFiles will be organized into:")
    print(f"  • {demo_dir}/Documents/")
    print(f"  • {demo_dir}/Images/")
    print(f"  • {demo_dir}/Media/")
    print(f"  • {demo_dir}/Archives/")
    print(f"  • {demo_dir}/Applications/")
    print(f"  • {demo_dir}/Code/")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
