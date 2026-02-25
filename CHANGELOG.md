# Changelog

All notable changes to Fusion Stress Tester PRO will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-25

### 🎉 Major Release - Complete Modernization

#### Added
- **Type Hints** - Full type annotations for Python 3.14+ compatibility
- **Modern Syntax** - Updated to Python 3.14 best practices (match/case, walrus operator, f-strings)
- **Better Error Handling** - Comprehensive exception handling with detailed error messages
- **Logging System** - Professional logging with file output and rotation
- **Configuration File** - JSON-based configuration for persistent settings
- **Export Formats** - Added JSON export in addition to CSV
- **Performance Metrics** - Enhanced monitoring with more detailed statistics
- **Safety Improvements** - Better temperature monitoring and automatic shutoff
- **UI Enhancements** - Improved layout and user experience
- **Documentation** - Comprehensive user guide and API documentation

#### Changed
- **Code Structure** - Refactored for better maintainability and readability
- **Performance** - Optimized stress testing algorithms for better efficiency
- **UI Layout** - Modernized interface with better organization
- **Error Messages** - More descriptive and helpful error messages
- **Dependencies** - Updated to latest stable versions

#### Fixed
- **Memory Leaks** - Fixed potential memory leaks in RAM stress test
- **Thread Safety** - Improved thread synchronization
- **GPU Detection** - Better CUDA availability detection
- **Disk I/O** - Fixed file cleanup issues in endurance mode
- **Network Stress** - Improved UDP flood stability
- **Tab Indentation** - Fixed inconsistent indentation (line 118)
- **Resource Cleanup** - Ensured proper cleanup on application exit

#### Security
- **API Key Storage** - Added warnings about secure credential storage
- **Network Safety** - Enhanced warnings for network stress testing
- **File Permissions** - Proper file permission handling

---

## [0.0.9] - Previous Version

### Initial Features
- CPU stress testing with multiprocessing
- RAM allocation stress testing
- Disk I/O stress testing with SSD endurance mode
- GPU stress testing (NVIDIA CUDA)
- Network UDP flood testing
- Real-time monitoring and graphing
- Safety thresholds
- Profile save/load functionality
- CSV data export
- Cloud API reporting (alpha)

---

## Migration Guide from 0.0.9 to 1.0.0

### Breaking Changes
None - fully backward compatible!

### New Features to Try
1. Check out the new logging system in `logs/` directory
2. Configure persistent settings in `config.json`
3. Export data in JSON format for better analysis
4. Use improved error messages for troubleshooting

### Recommended Actions
1. Update Python to 3.10+ (3.14 recommended)
2. Update dependencies: `pip install -r requirements.txt --upgrade`
3. Review new safety features in Settings tab
4. Check out the new User Guide in `docs/`
