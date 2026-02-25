# Fusion Stress Tester PRO - User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Features Overview](#features-overview)
6. [Stress Testing Components](#stress-testing-components)
7. [Safety Features](#safety-features)
8. [Data Export & Analysis](#data-export--analysis)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)

---

## Introduction

Fusion Stress Tester PRO is a comprehensive system stability and performance testing tool designed for:
- **System Builders** - Validate new PC builds
- **Overclockers** - Test stability after overclocking
- **IT Professionals** - Diagnose hardware issues
- **Enthusiasts** - Benchmark and monitor system performance

### What's New in v1.0.0
- Modern Python 3.14+ syntax
- Enhanced error handling
- Professional logging system
- Better performance monitoring
- Improved safety features

---

## System Requirements

### Minimum Requirements
- **OS:** Windows 10/11, Linux (Ubuntu 20.04+), macOS 11+
- **Python:** 3.10 or higher (3.14 recommended)
- **RAM:** 4GB (8GB recommended)
- **Storage:** 500MB free space
- **Display:** 1280x720 resolution

### Optional Requirements
- **GPU Testing:** NVIDIA GPU with CUDA support
- **Advanced Monitoring:** NVIDIA drivers with NVML support

---

## Installation

### Step 1: Install Python

Download Python 3.14 from [python.org](https://www.python.org/downloads/)

**Important:** Check "Add Python to PATH" during installation

### Step 2: Install Dependencies

```bash
cd fusion-stress-tester-pro
pip install -r requirements.txt
```

### Step 3: GPU Support (Optional)

For NVIDIA GPU stress testing:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install pynvml
```

---

## Quick Start

### Launch the Application

```bash
python fusion_stress_tester_pro_v1.0.0.py
```

### Your First Stress Test

1. **Select Components**
   - Check boxes for components you want to test
   - Start with CPU and RAM for beginners

2. **Configure Intensity**
   - Use sliders to set stress level
   - Start with 50% intensity for safety

3. **Set Safety Limits**
   - Go to "Safety & Monitoring" tab
   - Enable automatic shutoff
   - Set temperature limit (e.g., 85°C)

4. **Start Testing**
   - Click "Start All Stress Tests"
   - Monitor real-time graphs
   - Watch for warnings

5. **Stop and Review**
   - Click "Stop All" when done
   - Export data for analysis
   - Check logs for any issues

---

## Features Overview

### 1. Stress Control Panel
- **Component Selection** - Choose which hardware to stress
- **Intensity Sliders** - Fine-tune stress levels
- **Quick Profiles** - Pre-configured test scenarios
- **Start/Stop Controls** - Individual or all components

### 2. Real-Time Monitoring
- **Live Metrics** - CPU, RAM, Disk, GPU, Network usage
- **Temperature Tracking** - CPU and GPU temperatures
- **Performance Graphs** - Visual representation over time
- **Historical Data** - Track trends and patterns

### 3. Safety Features
- **Temperature Limits** - Automatic shutoff at threshold
- **Resource Protection** - Prevent system damage
- **Warning System** - Visual and audio alerts
- **Emergency Stop** - Immediate halt of all tests

### 4. Data Management
- **CSV Export** - Detailed performance data
- **JSON Export** - Structured data for analysis
- **Test Profiles** - Save and load configurations
- **Logging** - Comprehensive event logging

---

## Stress Testing Components

### CPU Stress Testing

**Purpose:** Test processor stability and thermal performance

**How it Works:**
- Spawns worker processes for each CPU core
- Performs intensive mathematical calculations
- Monitors temperature and usage

**Settings:**
- **Number of Cores:** 1 to all available cores
- **Intensity:** Light (30%), Medium (60%), Heavy (100%)

**Best Practices:**
- Start with 50% of cores
- Monitor temperatures closely
- Run for 15-30 minutes minimum
- Ensure adequate cooling

**Warning Signs:**
- Temperature above 90°C
- System freezing or stuttering
- Unexpected shutdowns

---

### RAM Stress Testing

**Purpose:** Validate memory stability and capacity

**How it Works:**
- Allocates memory in chunks
- Performs read/write operations
- Tests memory integrity

**Settings:**
- **Allocation Size:** MB to allocate
- **Test Pattern:** Sequential or random

**Best Practices:**
- Don't allocate all available RAM
- Leave 2-4GB for system
- Monitor for memory errors
- Run for 1-2 hours for thorough test

**Warning Signs:**
- System slowdown
- Application crashes
- Blue screen errors (BSOD)

---

### Disk I/O Stress Testing

**Purpose:** Test storage device performance and endurance

**How it Works:**
- Creates temporary test file
- Performs continuous read/write operations
- Measures throughput and latency

**Settings:**
- **File Size:** Size of test file (MB)
- **Endurance Mode:** Continuous writes (SSD warning!)
- **Test Duration:** Time to run test

**Best Practices:**
- **HDD:** Safe for extended testing
- **SSD:** Use endurance mode sparingly
- Monitor disk health after testing
- Ensure sufficient free space

**⚠️ SSD Warning:**
Endurance mode performs continuous writes which reduce SSD lifespan. Use only when necessary!

---

### GPU Stress Testing

**Purpose:** Test graphics card stability and thermal performance

**Requirements:**
- NVIDIA GPU with CUDA support
- PyTorch installed
- Latest NVIDIA drivers

**How it Works:**
- Performs matrix multiplications on GPU
- Scales intensity with matrix size
- Monitors GPU temperature and usage

**Settings:**
- **Intensity:** Easy, Medium, Hard, Extreme
- **Duration:** Test length

**Best Practices:**
- Ensure good GPU cooling
- Monitor GPU temperature (max 85°C)
- Start with Medium intensity
- Watch for artifacts or crashes

**Warning Signs:**
- Temperature above 90°C
- Screen artifacts or glitches
- Driver crashes
- System instability

---

### Network Stress Testing

**Purpose:** Test network throughput and stability

**How it Works:**
- Sends UDP packets to target
- Measures network bandwidth
- Tests network stability

**Settings:**
- **Target IP:** Destination address
- **Target Port:** Destination port
- **Packet Size:** Size of each packet

**⚠️ Important Warnings:**
- **Only use on private networks**
- **Get permission before testing**
- **May be flagged as malicious**
- **Can cause network congestion**

**Best Practices:**
- Test on local network only
- Use dedicated test machine as target
- Monitor network equipment
- Keep tests short (5-10 minutes)

---

## Safety Features

### Automatic Shutoff

**Temperature Protection:**
- Set maximum CPU temperature
- Set maximum GPU temperature
- Automatic test stop when exceeded

**Resource Protection:**
- Minimum free RAM threshold
- Minimum free disk space
- Prevents system crashes

**How to Configure:**
1. Go to "Safety & Monitoring" tab
2. Enable "Auto-Stop on Limits"
3. Set temperature thresholds
4. Set resource minimums
5. Click "Apply Settings"

---

### Emergency Stop

**When to Use:**
- System becoming unstable
- Temperatures too high
- Unexpected behavior
- Need immediate halt

**How to Use:**
- Click "STOP ALL" button (red)
- Or press ESC key
- Or close application window

**What Happens:**
- All stress tests stop immediately
- Resources are released
- Temporary files cleaned up
- System returns to normal

---

## Data Export & Analysis

### CSV Export

**What's Included:**
- Timestamp for each data point
- CPU usage (overall and per-core)
- RAM usage percentage
- Disk usage
- CPU temperature
- GPU metrics (if available)
- Network statistics

**How to Export:**
1. Run stress tests
2. Click "Export Data" button
3. Choose "CSV Format"
4. Select save location
5. Open in Excel or analysis tool

**Analysis Tips:**
- Look for temperature spikes
- Check for usage patterns
- Identify bottlenecks
- Compare before/after overclocking

---

### JSON Export

**What's Included:**
- Structured performance data
- Test configuration
- System information
- Timestamps and metadata

**How to Export:**
1. Click "Export Data" button
2. Choose "JSON Format"
3. Select save location

**Use Cases:**
- Programmatic analysis
- Database import
- Custom reporting
- API integration

---

### Test Profiles

**Save Profile:**
1. Configure your test settings
2. Click "Save Profile"
3. Enter profile name
4. Click "Save"

**Load Profile:**
1. Click "Load Profile"
2. Select saved profile
3. Settings automatically applied

**Profile Contents:**
- Component selection
- Intensity levels
- Safety thresholds
- Test duration
- Custom parameters

---

## Troubleshooting

### Application Won't Start

**Symptoms:** Error on launch or immediate crash

**Solutions:**
1. Check Python version: `python --version` (need 3.10+)
2. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
3. Check for conflicting packages
4. Run as administrator (Windows)
5. Check logs in `logs/` directory

---

### GPU Stress Not Available

**Symptoms:** GPU option grayed out or error message

**Solutions:**
1. Verify NVIDIA GPU: Check Device Manager
2. Install CUDA Toolkit from NVIDIA
3. Install PyTorch with CUDA:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
4. Update NVIDIA drivers
5. Restart application

---

### High Temperatures

**Symptoms:** Temperature warnings or automatic shutoff

**Solutions:**
1. Check cooling system (fans, heatsink)
2. Clean dust from components
3. Improve case airflow
4. Reduce stress intensity
5. Apply new thermal paste
6. Consider better cooling solution

---

### System Crashes During Test

**Symptoms:** Blue screen, freeze, or restart

**Possible Causes:**
- Overheating
- Unstable overclock
- Faulty hardware
- Insufficient power supply
- Driver issues

**Solutions:**
1. Check temperatures before crash
2. Reset overclock settings
3. Test individual components
4. Update drivers
5. Check hardware health
6. Verify PSU capacity

---

### Memory Allocation Fails

**Symptoms:** "Memory allocation failed" error

**Solutions:**
1. Close other applications
2. Reduce allocation size
3. Check available RAM
4. Restart computer
5. Check for memory leaks
6. Test RAM with MemTest86

---

## FAQ

### Q: Is this safe for my computer?
**A:** Yes, when used properly. Follow safety guidelines, monitor temperatures, and use appropriate intensity levels. The tool includes safety features to prevent damage.

### Q: How long should I run stress tests?
**A:** 
- **Quick Test:** 15-30 minutes
- **Standard Test:** 1-2 hours
- **Thorough Test:** 4-8 hours
- **Burn-in Test:** 24+ hours

### Q: Will this damage my SSD?
**A:** Normal disk testing is safe. **Avoid** SSD Endurance Mode unless necessary, as it performs continuous writes that reduce SSD lifespan.

### Q: Can I stress test a laptop?
**A:** Yes, but be extra cautious with temperatures. Laptops have limited cooling. Use lower intensity and monitor closely.

### Q: What's a good temperature limit?
**A:**
- **CPU:** 85-90°C (safe), 95°C+ (danger)
- **GPU:** 80-85°C (safe), 90°C+ (danger)
- Set limits 5-10°C below maximum safe temperature

### Q: Why does my system slow down during testing?
**A:** This is normal! Stress testing uses maximum resources. Close other applications before testing.

### Q: Can I use this for benchmarking?
**A:** Yes! Export data and compare results over time or between systems.

### Q: Is network stress testing legal?
**A:** Only on your own private network with permission. Never use on public networks or without authorization.

### Q: How do I interpret the graphs?
**A:**
- **Flat lines:** Consistent performance
- **Spikes:** Thermal throttling or resource limits
- **Drops:** Potential issues or throttling
- **Trends:** Overall system behavior

### Q: What if I find hardware issues?
**A:**
1. Document the issue (screenshots, logs)
2. Test individual components
3. Check warranty status
4. Contact manufacturer support
5. Consider professional diagnosis

---

## Getting Help

### Resources
- **GitHub Issues:** [Report bugs](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/issues)
- **Documentation:** Check `docs/` folder
- **Logs:** Review `logs/` directory
- **Email:** itszeeshanrajput@gmail.com

### Before Asking for Help
1. Check this guide
2. Review error messages
3. Check logs
4. Try troubleshooting steps
5. Search existing issues

### When Reporting Issues
Include:
- Operating system and version
- Python version
- Hardware specifications
- Error messages
- Steps to reproduce
- Log files

---

## Best Practices Summary

✅ **DO:**
- Monitor temperatures constantly
- Start with lower intensity
- Use safety features
- Close other applications
- Ensure good cooling
- Save test profiles
- Export data for analysis
- Read warnings carefully

❌ **DON'T:**
- Ignore temperature warnings
- Use SSD endurance mode frequently
- Network stress on public networks
- Run tests on unstable systems
- Allocate all available RAM
- Ignore system warnings
- Test without proper cooling

---

## Conclusion

Fusion Stress Tester PRO is a powerful tool for system validation and performance testing. Use it responsibly, follow safety guidelines, and always monitor your system during testing.

**Remember:** The goal is to test your system safely, not to damage it!

Happy testing! 🚀

---

**Version:** 1.0.0  
**Last Updated:** February 25, 2026  
**Author:** Zeeshan Rajput (@404innovator)  
**License:** MIT
