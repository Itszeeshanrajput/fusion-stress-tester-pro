"""
Tests for stress worker functions
"""
import pytest
import multiprocessing
import threading
import time
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _simple_cpu_worker(stop_event):
    """Simplified CPU worker for testing (module-level for pickling)"""
    iterations = 0
    while not stop_event.is_set() and iterations < 100:
        _ = 1 + 1
        iterations += 1


def test_cpu_stress_worker_concept():
    """Test CPU stress worker concept (without GUI)"""
    stop_event = multiprocessing.Event()
    
    # Start worker in a process
    process = multiprocessing.Process(target=_simple_cpu_worker, args=(stop_event,))
    process.start()
    
    # Let it run briefly
    time.sleep(0.1)
    
    # Stop it
    stop_event.set()
    process.join(timeout=2)
    
    assert not process.is_alive()


def test_ram_allocation_concept():
    """Test RAM allocation concept"""
    # Allocate a small amount of memory
    allocation_mb = 10
    bytes_to_allocate = allocation_mb * 1024 * 1024
    
    try:
        allocated = bytearray(bytes_to_allocate)
        assert len(allocated) == bytes_to_allocate
        del allocated
    except MemoryError:
        pytest.skip("Not enough memory for test")


def test_threading_event():
    """Test threading event for worker control"""
    stop_event = threading.Event()
    
    assert not stop_event.is_set()
    stop_event.set()
    assert stop_event.is_set()
    stop_event.clear()
    assert not stop_event.is_set()


def test_multiprocessing_event():
    """Test multiprocessing event for worker control"""
    stop_event = multiprocessing.Event()
    
    assert not stop_event.is_set()
    stop_event.set()
    assert stop_event.is_set()
    stop_event.clear()
    assert not stop_event.is_set()


def test_file_operations():
    """Test file operations for disk stress"""
    test_file = "test_stress_file.tmp"
    
    try:
        # Write test
        with open(test_file, 'wb') as f:
            data = os.urandom(1024)  # 1KB
            f.write(data)
            f.flush()
        
        # Verify file exists
        assert os.path.exists(test_file)
        assert os.path.getsize(test_file) == 1024
        
    finally:
        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)


def test_worker_state_management():
    """Test worker state management"""
    workers = {
        "cpu": [],
        "ram": None,
        "disk": None,
        "gpu": None,
        "network": None
    }
    
    assert isinstance(workers, dict)
    assert "cpu" in workers
    assert isinstance(workers["cpu"], list)


def test_stop_events_creation():
    """Test creation of stop events for all workers"""
    stop_events = {
        "cpu": multiprocessing.Event(),
        "ram": threading.Event(),
        "disk": threading.Event(),
        "gpu": threading.Event(),
        "network": threading.Event()
    }
    
    # Verify all events are created
    for key, event in stop_events.items():
        assert event is not None
        assert not event.is_set()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
