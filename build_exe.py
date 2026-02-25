"""
Build script for creating Fusion Stress Tester PRO executable
"""
import PyInstaller.__main__
import os
import shutil

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# PyInstaller arguments
PyInstaller.__main__.run([
    'fusion_stress_tester_pro_v0.0.9.py',
    '--name=FusionStressTesterPRO',
    '--onefile',
    '--windowed',
    '--icon=NONE',
    '--add-data=LICENSE;.',
    '--add-data=README.md;.',
    '--hidden-import=customtkinter',
    '--hidden-import=tkinter',
    '--hidden-import=psutil',
    '--hidden-import=matplotlib',
    '--hidden-import=matplotlib.backends.backend_tkagg',
    '--hidden-import=pynvml',
    '--hidden-import=torch',
    '--collect-all=customtkinter',
    '--collect-all=matplotlib',
    '--noconfirm',
])

print("\n" + "="*60)
print("BUILD COMPLETE!")
print("="*60)
print(f"\nExecutable created at: {os.path.join(current_dir, 'dist', 'FusionStressTesterPRO.exe')}")
print("\nYou can now:")
print("1. Test the executable by running it from the 'dist' folder")
print("2. Create a release package with the executable and documentation")
print("3. Upload to GitHub releases")
print("="*60)
