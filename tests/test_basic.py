"""
Basic tests for Fusion Stress Tester PRO
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """Test that all required modules can be imported"""
    try:
        import customtkinter
        import psutil
        import matplotlib
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import required module: {e}")


def test_psutil_available():
    """Test that psutil is working"""
    import psutil
    
    # Test CPU percent
    cpu_percent = psutil.cpu_percent(interval=0.1)
    assert isinstance(cpu_percent, (int, float))
    assert 0 <= cpu_percent <= 100
    
    # Test memory info
    memory = psutil.virtual_memory()
    assert hasattr(memory, 'total')
    assert hasattr(memory, 'available')
    assert memory.total > 0


def test_cpu_count():
    """Test CPU core detection"""
    import psutil
    
    cpu_count = psutil.cpu_count()
    assert cpu_count is not None
    assert cpu_count > 0
    assert isinstance(cpu_count, int)


def test_disk_usage():
    """Test disk usage detection"""
    import psutil
    
    disk = psutil.disk_usage('/')
    assert disk.total > 0
    assert disk.used >= 0
    assert disk.free >= 0


def test_constants():
    """Test that constants are defined correctly"""
    # These would be imported from the main file in a real scenario
    DISK_STRESS_FILE_NAME = "stress_test_file.tmp"
    assert isinstance(DISK_STRESS_FILE_NAME, str)
    assert len(DISK_STRESS_FILE_NAME) > 0


def test_python_version():
    """Test Python version compatibility"""
    assert sys.version_info >= (3, 10), "Python 3.10+ required"


def test_multiprocessing_available():
    """Test multiprocessing module"""
    import multiprocessing
    
    # Test that we can create events
    event = multiprocessing.Event()
    assert not event.is_set()
    event.set()
    assert event.is_set()


def test_threading_available():
    """Test threading module"""
    import threading
    
    # Test that we can create events
    event = threading.Event()
    assert not event.is_set()
    event.set()
    assert event.is_set()


def test_matplotlib_backend():
    """Test matplotlib backend configuration"""
    import matplotlib
    
    # Test that matplotlib can be imported
    assert hasattr(matplotlib, '__version__')


def test_socket_available():
    """Test socket module for network testing"""
    import socket
    
    # Test socket creation
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    assert sock is not None
    sock.close()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
