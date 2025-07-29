\# 🔥 Fusion Stress Tester PRO v0.0.9



!\[Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)

!\[CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-informational.svg)

!\[Stress Testing](https://img.shields.io/badge/Stress%20Testing-System%20Stability-orange.svg)

!\[License](https://img.shields.io/github/license/YOUR\_GITHUB\_USERNAME/fusion-stress-tester-pro.svg)



---



\## 🚀 Overview



The \*\*Fusion Stress Tester PRO\*\* is a robust and comprehensive system stability and performance benchmarking tool designed to push your hardware to its limits. Built with Python and `CustomTkinter` for a modern and intuitive graphical user interface, this application allows users to individually or simultaneously stress test various components of their system, including:



\* \*\*CPU\*\*: Multi-core processor utilization.

\* \*\*RAM\*\*: Memory allocation and read/write operations.

\* \*\*Disk I/O\*\*: Read/write operations on storage devices (with a caution for SSD endurance).

\* \*\*GPU\*\*: Graphics processing unit computational stress (requires NVIDIA CUDA-compatible GPU with PyTorch).

\* \*\*Network\*\*: UDP flood testing.



The "PRO" version includes advanced features such as live performance graphing, automatic safety monitoring (for CPU temperature, RAM, and disk space), cloud API reporting (alpha), and configurable test profiles for reproducible benchmarks.



---



\## ✨ Features



\* \*\*Intuitive GUI\*\*: Built with CustomTkinter for a modern look and feel.

\* \*\*Multi-Component Stress\*\*: Simultaneously stress CPU, RAM, Disk, GPU, and Network.

\* \*\*Adjustable Intensity\*\*: Control the load on your system components.

\* \*\*Live Monitoring\*\*: Real-time display of CPU, RAM, Disk, Temperature, GPU, and Network statistics.

\* \*\*Safety Thresholds\*\*: Configure automatic stop limits for CPU temperature, free RAM, and free disk space to prevent hardware damage.

\* \*\*Performance Graphing\*\*: Visualize system metrics over time with interactive plots.

\* \*\*Data Export\*\*: Export performance data to CSV for in-depth analysis.

\* \*\*Test Profiles\*\*: Save and load custom test configurations.

\* \*\*Cloud API Reporting (Alpha)\*\*: Option to send live metrics to a custom cloud endpoint.

\* \*\*Multi-threading/Multi-processing\*\*: Efficient utilization of system resources for stress generation.



---



\## 🖥️ Installation Guide for Windows Beginners



Follow these steps to get Fusion Stress Tester PRO up and running on your Windows PC.



\### Step 1: Download the Project

You have two options:

 Download ZIP (Easiest)\*\*


\### Step 2: Install Python (If You Don't Have It)



You need Python 3.x installed on your system.



1\.  \*\*Check if Python is installed:\*\*

&nbsp;   \* Open your command prompt (search for `cmd` in the Start Menu).

&nbsp;   \* Type `python --version` and press Enter.

&nbsp;   \* If it shows `Python 3.x.x` (e.g., `Python 3.11.9`), you already have it, skip to Step 3.

&nbsp;   \* If it says "python is not recognized...", or shows `Python 2.x.x`, you need to install Python 3.



2\.  \*\*Install Python 3:\*\*

&nbsp;   \* Go to the official Python download page for Windows: \[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

&nbsp;   \* Download the latest "Windows installer" (e.g., "Windows installer (64-bit)").

&nbsp;   \* Run the downloaded installer.

&nbsp;   \* \*\*VERY IMPORTANT:\*\* On the first screen of the installer, \*\*check the box that says "Add python.exe to PATH"\*\* (or similar wording). This step is crucial for easily running Python commands.

&nbsp;   \* Click "Install Now" and follow the prompts to complete the installation.

&nbsp;   \* After installation, close your current command prompt and open a new one. Type `python --version` again to confirm it shows `Python 3.x.x`.



\### Step 3: Open the Project in Command Prompt



Now, navigate your command prompt into the project folder.



1\.  Open a new command prompt (search for `cmd` in the Start Menu).

2\.  Use the `cd` (change directory) command to go into your project folder.

&nbsp;   \* \*\*If you downloaded the ZIP:\*\*

&nbsp;       Type `cd` followed by the path to your extracted folder. For example, if you extracted it to your Desktop, it might be:

&nbsp;       ```bash

&nbsp;       cd C:\\Users\\YourUsername\\Desktop\\fusion-stress-tester-pro-main

&nbsp;       ```

&nbsp;       (Replace `YourUsername` with your actual Windows username).

&nbsp;   \* \*\*If you cloned with Git:\*\*

&nbsp;       Type `cd` followed by the path to your cloned folder. For example:

&nbsp;       ```bash

&nbsp;       cd C:\\Users\\YourUsername\\Desktop\\fusion-stress-tester-pro

&nbsp;       ```

&nbsp;       (Replace `YourUsername` with your actual Windows username).

&nbsp;   \* Press Enter. You should see your command prompt now showing the path to your project folder.



\### Step 4: Install Project Dependencies



Now, install all the necessary Python libraries that your script needs.



1\.  In your command prompt (which should be inside your project folder from Step 3), run:

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```

&nbsp;   This will download and install all required packages listed in the `requirements.txt` file directly into your system's Python environment. This might take a few moments.



\### Step 5: For GPU Stress (Optional - NVIDIA CUDA only)



If you have an NVIDIA GPU and want to use the GPU stress testing features, you'll need to install PyTorch with CUDA support.



\* Ensure you have an NVIDIA GPU with appropriate drivers and CUDA Toolkit installed.

\* Follow the instructions on the official PyTorch website to install PyTorch with CUDA support: \[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

\* \*\*Example (check your specific CUDA version on PyTorch site, e.g., CUDA 11.8):\*\*

&nbsp;   ```bash

&nbsp;   pip install torch torchvision torchaudio --index-url \[https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)

&nbsp;   pip install pynvml # For detailed NVIDIA GPU monitoring

&nbsp;   ```

&nbsp;   \*If PyTorch or pynvml are not installed, GPU stress testing and detailed GPU monitoring will be disabled.\*



---



\## 🚀 Usage



Once all installation steps are complete, you can run the application.



1\.  \*\*Open your command prompt\*\* and \*\*navigate to your project folder\*\* (as in Step 3 of Installation).

2\.  \*\*Run the application:\*\*

&nbsp;   ```bash

&nbsp;   python fusion\_stress\_tester\_pro\_v0.0.9.py

&nbsp;   ```

3\.  \*\*Configure Tests\*\*: Use the "Stress Control" panel to select which components to stress and set their intensity or parameters.

4\.  \*\*Start/Stop\*\*: Click "Start All Stress Tests" to begin, or use individual "Start/Stop" buttons for specific components.

5\.  \*\*Monitor\*\*: Observe real-time metrics and performance graphs on the respective tabs.

6\.  \*\*Safety\*\*: Keep an eye on the "Safety \& Monitoring" tab and consider enabling automatic safety stops.



---



\## ⚠️ Important Considerations



\* \*\*Use with Caution\*\*: Stress testing can push your hardware to its limits, potentially causing high temperatures or instability. Always monitor your system and use safety features.

\* \*\*SSD Endurance Mode\*\*: Using "SSD Endurance Mode" for disk stress involves continuous writes, which can reduce the lifespan of Solid State Drives (SSDs). Use this feature with extreme care.

\* \*\*Network Stress\*\*: The UDP flood feature can cause network congestion and may be seen as malicious activity by network administrators or ISPs. Use only on private networks or with explicit permission.

\* \*\*Cloud API\*\*: The Cloud API reporting is an alpha feature. Replace the placeholder endpoint and API key with your actual details.



---



\## 🤝 Contributing



Contributions are welcome! If you have suggestions for improvements, bug reports, or want to add new features, please feel free to:



1\.  Fork the repository.

2\.  Create a new branch (`git checkout -b feature/YourFeature`).

3\.  Make your changes.

4\.  Commit your changes (`git commit -m 'Add new feature'`).

5\.  Push to the branch (`git push origin feature/YourFeature`).

6\.  Open a Pull Request.



---



\## 📄 License



This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file for details.



---



\## 📧 Contact



For any questions or inquiries, please contact:



\* \*\*Your Name/Handle\*\*: \[Your GitHub Username](https://github.com/YOUR\_GITHUB\_USERNAME)

\* \*\*Email\*\*: \[your.email@example.com](mailto:your.email@example.com)

