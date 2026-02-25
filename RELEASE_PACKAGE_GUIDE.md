# Creating Release Package for GitHub

## Quick Release Package Creation

### Step 1: Build the Executable

```bash
python build_exe.py
```

Wait for the build to complete (2-5 minutes).

---

### Step 2: Create Release Folder Structure

```bash
mkdir release
mkdir release\FusionStressTesterPRO_v1.0.0_Windows
```

---

### Step 3: Copy Files to Release Folder

Copy these files from your project to `release\FusionStressTesterPRO_v1.0.0_Windows\`:

**Required Files:**
- `dist\FusionStressTesterPRO.exe` → Main executable
- `README.md` → Project overview
- `LICENSE` → MIT License
- `CHANGELOG.md` → Version history

**Documentation:**
- `docs\USER_GUIDE.md` → Comprehensive user guide
- `RELEASE_NOTES_v1.0.0.md` → Release information
- `BUILD_INSTRUCTIONS.md` → How to build from source

**Optional:**
- `CONTRIBUTING.md` → For contributors
- `requirements.txt` → For Python users

---

### Step 4: Create README for Release Package

Create `release\FusionStressTesterPRO_v1.0.0_Windows\README_RELEASE.txt`:

```
================================================================================
         FUSION STRESS TESTER PRO v1.0.0 - Windows Release
================================================================================

Thank you for downloading Fusion Stress Tester PRO!

QUICK START:
1. Extract all files to a folder
2. Double-click FusionStressTesterPRO.exe
3. Read USER_GUIDE.md for detailed instructions

SYSTEM REQUIREMENTS:
- Windows 10/11 (64-bit)
- 4GB RAM minimum (8GB recommended)
- 200MB free disk space
- Optional: NVIDIA GPU for GPU stress testing

FIRST TIME USERS:
- The first launch may take 10-15 seconds
- Windows may show a security warning (click "More info" → "Run anyway")
- Read the USER_GUIDE.md for safety information

IMPORTANT SAFETY:
- Monitor temperatures during stress testing
- Start with lower intensity levels
- Enable automatic safety shutoff
- Read safety warnings in USER_GUIDE.md

FILES INCLUDED:
- FusionStressTesterPRO.exe - Main application
- README.md - Project information
- USER_GUIDE.md - Comprehensive guide
- LICENSE - MIT License
- CHANGELOG.md - Version history
- RELEASE_NOTES_v1.0.0.md - What's new

SUPPORT:
- Documentation: See USER_GUIDE.md
- Issues: https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/issues
- Email: itszeeshanrajput@gmail.com

AUTHOR:
Zeeshan Rajput (@404innovator)
https://github.com/Itszeeshanrajput

LICENSE:
MIT License - See LICENSE file

VERSION: 1.0.0
RELEASE DATE: February 25, 2026

================================================================================
```

---

### Step 5: Create ZIP Archive

**Option A: Using PowerShell**
```powershell
cd release
Compress-Archive -Path FusionStressTesterPRO_v1.0.0_Windows -DestinationPath FusionStressTesterPRO_v1.0.0_Windows.zip
```

**Option B: Using Windows Explorer**
1. Right-click the `FusionStressTesterPRO_v1.0.0_Windows` folder
2. Select "Send to" → "Compressed (zipped) folder"
3. Rename to `FusionStressTesterPRO_v1.0.0_Windows.zip`

---

### Step 6: Upload to GitHub Releases

1. **Go to Releases Page:**
   https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/releases/new

2. **Fill in Release Information:**
   - **Tag:** `v1.0.0`
   - **Release title:** `Fusion Stress Tester PRO v1.0.0 - Major Release`
   - **Description:** Copy from `RELEASE_NOTES_v1.0.0.md`

3. **Upload Files:**
   - Drag and drop `FusionStressTesterPRO_v1.0.0_Windows.zip`
   - Optionally add standalone `FusionStressTesterPRO.exe`

4. **Publish:**
   - Check "Set as the latest release"
   - Click "Publish release"

---

## Release Checklist

Before creating the release, verify:

- [ ] Executable builds without errors
- [ ] Executable runs and all features work
- [ ] All documentation files are included
- [ ] README_RELEASE.txt is created
- [ ] ZIP file is created and tested
- [ ] Version numbers are correct (v1.0.0)
- [ ] CHANGELOG is up to date
- [ ] Release notes are complete

---

## Testing the Release Package

1. **Extract ZIP to a test folder**
2. **Run the executable**
3. **Test all features:**
   - CPU stress test
   - RAM stress test
   - Disk I/O test
   - GPU test (if available)
   - Network test
   - Monitoring graphs
   - Data export
   - Profile save/load

4. **Verify documentation:**
   - README.md opens correctly
   - USER_GUIDE.md is readable
   - All links work

---

## Release Package Contents

```
FusionStressTesterPRO_v1.0.0_Windows.zip
└── FusionStressTesterPRO_v1.0.0_Windows/
    ├── FusionStressTesterPRO.exe          # Main executable (100-200MB)
    ├── README.md                           # Project overview
    ├── README_RELEASE.txt                  # Quick start for users
    ├── USER_GUIDE.md                       # Comprehensive guide
    ├── LICENSE                             # MIT License
    ├── CHANGELOG.md                        # Version history
    ├── RELEASE_NOTES_v1.0.0.md            # What's new
    ├── BUILD_INSTRUCTIONS.md               # Build from source
    └── CONTRIBUTING.md                     # For contributors
```

---

## Download Links (After Release)

Once published, users can download from:
- **Latest Release:** https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/releases/latest
- **All Releases:** https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/releases

---

## Updating README with Download Link

Add this section to your main README.md:

```markdown
## 📥 Download

### Windows Executable (Recommended)
Download the latest release:
[**Download FusionStressTesterPRO_v1.0.0_Windows.zip**](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/releases/latest)

**No Python installation required!**

### Run from Source
```bash
git clone https://github.com/Itszeeshanrajput/fusion-stress-tester-pro.git
cd fusion-stress-tester-pro
pip install -r requirements.txt
python fusion_stress_tester_pro_v0.0.9.py
```
```

---

## Troubleshooting Release Creation

### Issue: Build takes too long

**Normal:** PyInstaller can take 2-10 minutes depending on your system.

### Issue: Executable is very large

**Normal:** Size is 100-200MB due to included libraries. This is expected.

### Issue: Windows Defender blocks executable

**Solution:** This is a false positive. Users can:
1. Click "More info"
2. Click "Run anyway"
3. Or add exception in Windows Defender

### Issue: Missing files in release

**Solution:** Double-check the file list and copy all required files.

---

## Version Numbering

For future releases:
- **Major (1.x.x):** Breaking changes
- **Minor (x.1.x):** New features
- **Patch (x.x.1):** Bug fixes

Example:
- v1.0.0 → Initial release
- v1.0.1 → Bug fix
- v1.1.0 → New features
- v2.0.0 → Major overhaul

---

**Created:** February 25, 2026  
**Author:** Zeeshan Rajput (@404innovator)  
**Version:** 1.0.0
