import os
import shutil
import schedule  # type: ignore
import time
import json
from datetime import datetime
from typing import Dict, Any

from utils import (
    load_config,
    setup_logging,
    get_file_extension,
    should_exclude,
    resolve_duplicate,
    find_category_for_extension,
    format_size,
    get_folder_size,
    count_files
)

# Global variables
logger = None
config = None

def print_banner():
    """Print a nice banner at startup."""
    print("\n" + "="*60)
    print("🗂️  FILE ORGANIZER - Automatic File Management System")
    print("="*60 + "\n")

def print_menu():
    """Display the main menu."""
    print("\n" + "-"*60)
    print("📋 MAIN MENU")
    print("-"*60)
    print("1. Organize files now (one-time)")
    print("2. Enable/Disable scheduled organization")
    print("3. View organization stats")
    print("4. View current configuration")
    print("5. Edit target directory")
    print("6. Preview changes (dry-run)")
    print("7. View recent logs")
    print("8. Exit")
    print("-"*60)

def organize_folder(target_dir: str, dry_run: bool = False) -> Dict[str, Any]:
    """
    Scan the target directory and organize files into categories.
    
    Args:
        target_dir: Directory to organize
        dry_run: If True, only preview changes without moving files
    
    Returns:
        Dictionary with organization statistics
    """
    if not os.path.exists(target_dir):
        if logger:
            logger.error(f"Target directory does not exist: {target_dir}")
        print(f"❌ Error: Directory not found - {target_dir}")
        return {"error": "Directory not found", "moved": 0}
    
    if logger:
        logger.info(f"Starting organization for directory: {target_dir}")
        logger.info(f"Dry-run mode: {dry_run}")
    print(f"\n{'📋 PREVIEW MODE' if dry_run else '🚀 ORGANIZING FILES'}")
    print("="*60)
    print(f"Target directory: {target_dir}")
    print(f"Mode: {'Preview (No changes)' if dry_run else 'Live'}")
    print("="*60 + "\n")
    
    if not config:
        print("\u274c Config not loaded")
        return {"error": "Config not loaded", "moved": 0}
    
    file_categories: Dict[str, Any] = config["file_categories"]
    exclude_config: Dict[str, Any] = config.get("exclude", {})
    
    moved_count: int = 0
    skipped_count: int = 0
    error_count: int = 0
    moved_files: list[Dict[str, str]] = []
    skipped_files: list[str] = []
    
    try:
        items = os.listdir(target_dir)
    except PermissionError:
        if logger:
            logger.error(f"Permission denied: {target_dir}")
        print("❌ Permission denied accessing the directory")
        return {"error": "Permission denied", "moved": 0}
    
    # Sort items for consistent output
    items.sort()
    
    for item in items:
        item_path = os.path.join(target_dir, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            # But still log them
            if not should_exclude(item, exclude_config):
                if logger:
                    logger.debug(f"Skipped directory: {item}")
            continue
        
        # Skip excluded items
        if should_exclude(item, exclude_config):
            if logger:
                logger.debug(f"Excluded file: {item}")
            skipped_files.append(item)
            skipped_count += 1
            continue
        
        file_ext = get_file_extension(item)
        destination_folder = find_category_for_extension(file_ext, file_categories)
        
        if not destination_folder:
            destination_folder = "Others"
        
        dest_dir_path = os.path.join(target_dir, destination_folder)
        final_dest_path = os.path.join(dest_dir_path, item)
        final_dest_path = resolve_duplicate(final_dest_path)
        
        try:
            # Create destination folder
            if not dry_run:
                if not os.path.exists(dest_dir_path):
                    os.makedirs(dest_dir_path)
                    if logger:
                        logger.info(f"Created folder: {destination_folder}")
                    print(f"📁 Created folder: {destination_folder}/")
                
                # Move the file
                shutil.move(item_path, final_dest_path)
                if logger:
                    logger.info(f"Moved file: {item} -> {destination_folder}/{os.path.basename(final_dest_path)}")
            else:
                if logger:
                    logger.debug(f"[DRY-RUN] Would move: {item} -> {destination_folder}/{os.path.basename(final_dest_path)}")
            
            # Display message
            final_file_name = os.path.basename(final_dest_path)
            status = "✓" if not dry_run else "→"
            print(f"{status} {item:<40} → {destination_folder}/{final_file_name}")
            
            moved_files.append({
                "file": item,
                "destination": destination_folder,
                "final_name": final_file_name
            })
            moved_count += 1
            
        except Exception as e:
            error_msg = str(e)
            if logger:
                logger.error(f"Error moving file {item}: {error_msg}")
            print(f"❌ Error: {item} - {error_msg}")
            error_count += 1
    
    # Print summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"✓ Organized: {moved_count} files")
    print(f"⊘ Skipped: {skipped_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("="*60 + "\n")
    
    if logger:
        logger.info(f"Organization complete. Moved: {moved_count}, Skipped: {skipped_count}, Errors: {error_count}")
    
    return {
        "moved": moved_count,
        "skipped": skipped_count,
        "errors": error_count,
        "moved_files": moved_files,
        "skipped_files": skipped_files
    }

def scheduled_task() -> None:
    """Task to run at scheduled time."""
    if logger:
        logger.info(f"Scheduled task triggered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\n⏰ Running scheduled organization at {datetime.now().strftime('%H:%M:%S')}")
    if config:
        target_dir = config["general"]["target_directory"]
        organize_folder(target_dir)

def start_scheduler() -> None:
    """Start the background scheduler."""
    if not config:
        print("❌ Config not loaded")
        return
    schedule_time = config["general"]["schedule_time"]
    
    # Clear existing jobs
    schedule.clear()  # type: ignore
    
    # Schedule the task
    schedule.every().day.at(schedule_time).do(scheduled_task)  # type: ignore
    
    if logger:
        logger.info(f"Scheduler started. Will run at {schedule_time} daily")
    print(f"✓ Scheduler enabled - Will run daily at {schedule_time}")
    
    # Keep scheduler running in a loop
    try:
        while True:
            schedule.run_pending()  # type: ignore
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        if logger:
            logger.info("Scheduler stopped by user")
        print("\n⏸️  Scheduler stopped")

def view_stats(target_dir: str) -> None:
    """Display organization statistics."""
    print("\n" + "="*60)
    print("📊 FOLDER STATISTICS")
    print("="*60)
    
    if not os.path.exists(target_dir):
        print(f"❌ Directory not found: {target_dir}")
        return
    
    total_size = get_folder_size(target_dir)
    total_files = count_files(target_dir)
    
    print(f"Location: {target_dir}")
    print(f"Total files: {total_files}")
    print(f"Total size: {format_size(total_size)}")
    print("\nBreakdown by category:")
    print("-"*60)
    
    try:
        for category in os.listdir(target_dir):
            category_path = os.path.join(target_dir, category)
            if os.path.isdir(category_path):
                size = get_folder_size(category_path)
                files = count_files(category_path)
                print(f"  📁 {category:<25} - {files:>3} files ({format_size(size):>10})")
    except Exception as e:
        if logger:
            logger.error(f"Error reading folder stats: {e}")
        print(f"❌ Error reading folder statistics")
    
    print("="*60 + "\n")

def view_configuration() -> None:
    """Display current configuration."""
    print("\n" + "="*60)
    print("⚙️  CURRENT CONFIGURATION")
    print("="*60)
    
    if not config:
        print("❌ Config not loaded")
        return
    general = config["general"]
    print(f"Target Directory: {general['target_directory']}")
    print(f"Scheduling Enabled: {general['enable_scheduling']}")
    print(f"Schedule Time: {general['schedule_time']}")
    print(f"Dry-run Mode: {general['dry_run']}")
    print(f"Logging Enabled: {general['enable_logging']}")
    print(f"Log File: {general['log_file']}")
    
    print("\nFile Categories:")
    print("-"*60)
    for category, info in config["file_categories"].items():
        exts = ", ".join(info["extensions"][:5])
        more = f" +{len(info['extensions'])-5} more" if len(info["extensions"]) > 5 else ""
        print(f"  📂 {category:<15} - {info['description']}")
        print(f"     Extensions: {exts}{more}")
    
    print("\nExcluded Items:")
    print("-"*60)
    exclude = config.get("exclude", {})
    folders = exclude.get("folders", [])
    files = exclude.get("files", [])
    print(f"  Excluded folders: {', '.join(folders[:5])}{'...' if len(folders) > 5 else ''}")
    print(f"  Excluded files: {', '.join(files[:5])}{'...' if len(files) > 5 else ''}")
    
    print("="*60 + "\n")

def edit_target_directory() -> None:
    """Allow user to change the target directory."""
    if not config:
        print("❌ Config not loaded")
        return
    current = config["general"]["target_directory"]
    print(f"\nCurrent target directory: {current}")
    print("Enter new target directory (or press Enter to cancel):")
    new_dir = input("> ").strip()
    
    if not new_dir:
        print("Cancelled.")
        return
    
    if not os.path.exists(new_dir):
        print(f"❌ Directory does not exist: {new_dir}")
        return
    
    config["general"]["target_directory"] = new_dir
    
    # Save to config file
    try:
        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        if logger:
            logger.info(f"Target directory changed to: {new_dir}")
        print(f"✓ Target directory updated to: {new_dir}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to save config: {e}")
        print(f"❌ Failed to save configuration: {e}")

def view_logs(lines: int = 20) -> None:
    """Display recent log entries."""
    if not config:
        print("❌ Config not loaded")
        return
    log_file = config["general"]["log_file"]
    
    if not os.path.exists(log_file):
        print(f"Log file not found: {log_file}")
        return
    
    print("\n" + "="*60)
    print(f"📋 RECENT LOGS (last {lines} lines)")
    print("="*60)
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            all_lines: list[str] = f.readlines()
            recent_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
            for line in recent_lines:
                print(line.rstrip())
    except Exception as e:
        print(f"❌ Error reading logs: {e}")
    
    print("="*60 + "\n")

def main():
    """Main entry point."""
    global logger, config
    
    print_banner()
    
    # Load configuration
    try:
        config = load_config("config.json")
    except Exception as e:
        print(f"❌ Failed to load configuration: {e}")
        print("Please check your config.json file.")
        return
    
    # Setup logging
    log_enabled = config["general"]["enable_logging"]
    log_file = config["general"]["log_file"]
    logger = setup_logging(log_file, enable=log_enabled)
    
    if logger:
        logger.info("="*60)
        logger.info("File Organizer started")
        logger.info("="*60)
    
    target_dir = config["general"]["target_directory"]
    
    # Interactive menu
    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == "1":
            organize_folder(target_dir, dry_run=config["general"]["dry_run"])
        
        elif choice == "2":
            enable = input("Enable scheduling? (y/n): ").strip().lower() == 'y'
            if enable:
                start_scheduler()
            else:
                schedule.clear()  # type: ignore
                print("✓ Scheduler disabled")
        
        elif choice == "3":
            view_stats(target_dir)
        
        elif choice == "4":
            view_configuration()
        
        elif choice == "5":
            edit_target_directory()
            target_dir = config["general"]["target_directory"]
        
        elif choice == "6":
            organize_folder(target_dir, dry_run=True)
        
        elif choice == "7":
            view_logs()
        
        elif choice == "8":
            print("\n👋 Goodbye!\n")
            logger.info("File Organizer closed")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()