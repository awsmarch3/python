#!/usr/bin/env python3

import os
import sys
import datetime
import platform
import subprocess

def display_header():
    """Display a nice header for the job execution"""
    print("=" * 60)
    print("🚀 JENKINS FREESTYLE JOB EXECUTION")
    print("=" * 60)

def display_system_info():
    """Display system information"""
    print("\n📊 SYSTEM INFORMATION:")
    print(f"   Platform: {platform.system()} {platform.release()}")
    print(f"   Python Version: {sys.version}")
    print(f"   Current Directory: {os.getcwd()}")
    print(f"   User: {os.getenv('USER', 'Unknown')}")
    print(f"   Hostname: {platform.node()}")

def display_timestamp():
    """Display current timestamp"""
    now = datetime.datetime.now()
    print(f"\n⏰ EXECUTION TIME:")
    print(f"   Date: {now.strftime('%Y-%m-%d')}")
    print(f"   Time: {now.strftime('%H:%M:%S')}")
    print(f"   Timezone: {now.astimezone().tzinfo}")

def display_environment():
    """Display relevant environment variables"""
    print(f"\n🔧 ENVIRONMENT VARIABLES:")
    
    # Jenkins-specific environment variables
    jenkins_vars = [
        'BUILD_NUMBER', 'BUILD_ID', 'BUILD_URL', 'JOB_NAME', 
        'JENKINS_URL', 'WORKSPACE', 'NODE_NAME', 'BUILD_TAG'
    ]
    
    print("   Jenkins Variables:")
    for var in jenkins_vars:
        value = os.getenv(var, 'Not Set')
        print(f"     {var}: {value}")
    
    # Other useful variables
    print("   System Variables:")
    system_vars = ['PATH', 'HOME', 'PWD']
    for var in system_vars:
        value = os.getenv(var, 'Not Set')
        # Truncate long PATH variables
        if var == 'PATH' and len(value) > 100:
            value = value[:100] + "..."
        print(f"     {var}: {value}")

def perform_sample_task():
    """Perform a sample task to demonstrate job functionality"""
    print(f"\n🔄 PERFORMING SAMPLE TASKS:")
    
    # Task 1: File operations
    print("   Task 1: Creating a test file...")
    test_file = "jenkins_test_output.txt"
    with open(test_file, 'w') as f:
        f.write(f"Jenkins job executed at {datetime.datetime.now()}\n")
        f.write("This is a test file created by the Jenkins job.\n")
    print(f"   ✅ Created file: {test_file}")
    
    # Task 2: Simple calculation
    print("   Task 2: Performing calculations...")
    result = sum(range(1, 101))  # Sum of 1 to 100
    print(f"   ✅ Sum of 1 to 100: {result}")
    
    # Task 3: List directory contents
    print("   Task 3: Listing current directory...")
    files = os.listdir('.')
    print(f"   ✅ Found {len(files)} files/directories")
    for file in files[:5]:  # Show first 5 files
        print(f"      - {file}")
    if len(files) > 5:
        print(f"      ... and {len(files) - 5} more")

def check_dependencies():
    """Check if required tools/dependencies are available"""
    print(f"\n🔍 DEPENDENCY CHECK:")
    
    dependencies = ['python3', 'pip', 'git']
    
    for dep in dependencies:
        try:
            result = subprocess.run(['which', dep], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"   ✅ {dep}: {result.stdout.strip()}")
            else:
                print(f"   ❌ {dep}: Not found")
        except Exception as e:
            print(f"   ❌ {dep}: Error checking - {e}")

def display_footer():
    """Display footer with job completion status"""
    print("\n" + "=" * 60)
    print("✅ JOB COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"Job finished at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Check Jenkins console output for full logs.")
    print("=" * 60)

def main():
    """Main execution function"""
    try:
        display_header()
        display_timestamp()
        display_system_info()
        display_environment()
        check_dependencies()
        perform_sample_task()
        display_footer()
        
        # Exit with success code
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("Job failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
