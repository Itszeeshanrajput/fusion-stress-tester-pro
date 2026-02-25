# 🔥 Fusion Stress Tester PRO

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-informational.svg)
![License](https://img.shields.io/github/license/Itszeeshanrajput/fusion-stress-tester-pro.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-0.0.9-green.svg)

**Professional System Stress Testing & Performance Benchmarking Tool**

[Download](#-download) • [Features](#-features) • [Installation](#️-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 📥 Download

### Windows Executable (Recommended for Beginners)

**No Python installation required!**

[![Download Latest Release](https://img.shields.io/badge/Download-Windows%20EXE-blue?style=for-the-badge&logo=windows)](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/releases/latest)

**Quick Start:**
1. Download `FusionStressTesterPRO_v1.0.0_Windows.zip`
2. Extract all files
3. Double-click `FusionStressTesterPRO.exe`
4. Read `USER_GUIDE.md` for instructions

**System Requirements:**
- Windows 10/11 (64-bit)
- 4GB RAM minimum (8GB recommended)
- 200MB free disk space

### Run from Source (Advanced Users)

```bash
git clone https://github.com/Itszeeshanrajput/fusion-stress-tester-pro.git
cd fusion-stress-tester-pro
pip install -r requirements.txt
python fusion_stress_tester_pro_v0.0.9.py
```

---

## 🚀 Overview

**Fusion Stress Tester PRO** is a comprehensive system stability and performance benchmarking tool designed to push your hardware to its limits. Built with Python and CustomTkinter for a modern, intuitive GUI, this application allows you to stress test various system components individually or simultaneously.

### Supported Components

- **💻 CPU** - Multi-core processor utilization and thermal testing
- **🧠 RAM** - Memory allocation and read/write operations
- **💾 Disk I/O** - Storage device performance testing (HDD/SSD)
- **🎮 GPU** - Graphics processing unit computational stress (NVIDIA CUDA)
- **🌐 Network** - UDP flood and bandwidth testing

### Advanced Features

✨ Live performance graphing and real-time monitoring  
🛡️ Automatic safety thresholds (temperature, RAM, disk space)  
📊 Data export to CSV for analysis  
⚙️ Configurable test profiles  
☁️ Cloud API reporting (alpha)



---

## ✨ Features

### 🎨 User Interface
- **Modern GUI** - Built with CustomTkinter for sleek, responsive design
- **Real-time Monitoring** - Live display of all system metrics
- **Interactive Graphs** - Visualize performance data over time
- **Dark/Light Themes** - Customizable appearance

### 🔧 Testing Capabilities
- **Multi-Component Stress** - Test CPU, RAM, Disk, GPU, and Network simultaneously
- **Adjustable Intensity** - Fine-tune load on each component
- **Custom Test Profiles** - Save and load test configurations
- **Batch Testing** - Run multiple test scenarios automatically

### 🛡️ Safety Features
- **Temperature Monitoring** - Real-time CPU/GPU temperature tracking
- **Automatic Shutoff** - Configurable safety thresholds
- **Resource Protection** - Prevent system damage with smart limits
- **Warning System** - Visual and audio alerts for critical conditions

### 📊 Data & Analytics
- **CSV Export** - Export detailed performance data
- **Performance Reports** - Generate comprehensive test summaries
- **Historical Data** - Track system performance over time
- **Cloud API (Alpha)** - Optional cloud reporting integration

---



## 🖥️ Installation

### Quick Start (Windows)

#### Step 1: Download the Project

**Option A: Download ZIP (Recommended for beginners)**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location

**Option B: Clone with Git**
```bash
git clone https://github.com/Itszeeshanrajput/fusion-stress-tester-pro.git
cd fusion-stress-tester-pro
```

#### Step 2: Install Python

**Check if Python is installed:**
```bash
python --version
```

If you see `Python 3.10` or higher, you're good to go! Otherwise:

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **⚠️ IMPORTANT:** Check "Add Python to PATH" during installation
4. Restart your terminal/command prompt

#### Step 3: Install Dependencies

Open terminal/command prompt in the project folder:

```bash
cd path/to/fusion-stress-tester-pro
pip install -r requirements.txt
```

#### Step 4: GPU Support (Optional - NVIDIA Only)

For GPU stress testing with NVIDIA cards:

```bash
# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install NVIDIA monitoring tools
pip install pynvml
```

**Note:** GPU features require NVIDIA GPU with CUDA support. AMD/Intel GPUs are not currently supported.



---



## 🚀 Usage

### Running the Application

```bash
python fusion_stress_tester_pro_v0.0.9.py
```

### Quick Guide

1. **Configure Tests**
   - Select components to stress (CPU, RAM, Disk, GPU, Network)
   - Adjust intensity sliders for each component
   - Set test duration and parameters

2. **Set Safety Limits**
   - Navigate to "Safety & Monitoring" tab
   - Configure temperature thresholds
   - Set RAM and disk space limits
   - Enable automatic shutoff

3. **Start Testing**
   - Click "Start All Stress Tests" for comprehensive testing
   - Or use individual component buttons for targeted tests
   - Monitor real-time metrics in the dashboard

4. **View Results**
   - Check performance graphs for visual analysis
   - Export data to CSV for detailed review
   - Save test profiles for future use

### Test Profiles

**Light Stress** - 30-50% intensity, good for stability testing  
**Medium Stress** - 60-80% intensity, standard benchmarking  
**Heavy Stress** - 90-100% intensity, maximum performance testing



---



## ⚠️ Important Safety Information

### Before You Start

**🔥 Temperature Warning**
- Stress testing generates significant heat
- Ensure proper cooling and ventilation
- Monitor temperatures continuously
- Stop testing if temperatures exceed safe limits (typically 85-90°C for CPU)

**💾 SSD Endurance Mode**
- Continuous writes reduce SSD lifespan
- Use sparingly and only when necessary
- Not recommended for daily use
- Consider using HDD for disk stress tests

**🌐 Network Testing**
- UDP flood can cause network congestion
- May be flagged as malicious by ISPs
- **Only use on private networks**
- Obtain permission before testing on shared networks

**⚡ Power Supply**
- Ensure adequate PSU capacity
- Full system stress requires significant power
- Monitor for system instability

**🛡️ Liability**
- Use at your own risk
- Author not responsible for hardware damage
- Always enable safety features
- Start with lower intensity levels



---



## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Areas for Contribution

- 🐛 Bug fixes and stability improvements
- ✨ New stress testing features
- 📊 Additional monitoring metrics
- 🎨 UI/UX enhancements
- 📝 Documentation improvements
- 🧪 Test coverage expansion

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact & Support

**Developer:** Zeeshan Rajput (@404innovator)

**Email:** itszeeshanrajput@gmail.com

**GitHub:** [@Itszeeshanrajput](https://github.com/Itszeeshanrajput)

### Get Help

- 🐛 [Report a Bug](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/issues)
- 💡 [Request a Feature](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/issues)
- 📖 [Read the Docs](https://github.com/Itszeeshanrajput/fusion-stress-tester-pro/wiki)

---

## 🌟 Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Powered by [psutil](https://github.com/giampaolo/psutil)
- GPU support via [PyTorch](https://pytorch.org/)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ by [Zeeshan Rajput](https://github.com/Itszeeshanrajput)

</div>

