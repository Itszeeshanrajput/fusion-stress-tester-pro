import unittest
import os
import json
import tkinter as tk
from unittest.mock import patch
import sys

# Add the root directory to the Python path to allow importing the main script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fusion_stress_tester import StressTesterApp

class TestProfileLoading(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Create a dummy profile file
        self.profile_data = {
            "intensity_level": "Hard",
            "cpu_cores_to_stress": "4",
            "ram_allocation_mb": "2048",
            "disk_file_size_mb": "1024",
            "ssd_endurance_mode": True,
            "network_target_ip": "192.168.1.1",
            "network_target_port": "8080",
            "network_packet_size": "2048",
            "cpu_temp_limit": "95",
            "ram_free_threshold": "1.0",
            "disk_free_threshold": "5.0",
            "safety_monitoring_active": False,
            "cloud_api_reporting_active": True
        }
        self.test_profile_path = "test_profile.json"
        with open(self.test_profile_path, 'w') as f:
            json.dump(self.profile_data, f)

        # We need a root Tkinter window to run the app
        self.root = tk.Tk()
        self.root.withdraw() # Hide the main window
        self.app = StressTesterApp()

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(self.test_profile_path):
            os.remove(self.test_profile_path)

        # Destroy the app window
        self.app.destroy()

    def test_load_profile_fix(self):
        """
        This test verifies that loading a profile correctly updates all UI elements
        without raising an error, confirming the bug is fixed.
        """
        # With the fix, loading the profile should not raise an error and should show an info message.
        with patch('tkinter.messagebox.showerror') as mock_showerror, \
             patch('tkinter.messagebox.showinfo') as mock_showinfo:

            self.app.load_profile(file_path=self.test_profile_path)

            # Assert that no error message was shown
            mock_showerror.assert_not_called()

            # Assert that the success info message was shown
            mock_showinfo.assert_called_once_with("Load Profile", f"Test profile loaded successfully from:\n{self.test_profile_path}")

        # Assert that the values from the profile have been set correctly.
        self.assertEqual(self.app.intensity_selector.get(), self.profile_data["intensity_level"])
        self.assertEqual(self.app.cpu_cores_entry.get(), self.profile_data["cpu_cores_to_stress"])
        self.assertEqual(self.app.ram_mb_entry.get(), self.profile_data["ram_allocation_mb"])
        self.assertEqual(self.app.disk_mb_entry.get(), self.profile_data["disk_file_size_mb"])

        # Check the state of the checkboxes (1 for selected, 0 for not)
        self.assertEqual(self.app.ssd_endurance_checkbox.get(), 1 if self.profile_data["ssd_endurance_mode"] else 0)
        self.assertEqual(self.app.enable_cloud_api_checkbox.get(), 1 if self.profile_data["cloud_api_reporting_active"] else 0)

        self.assertEqual(self.app.target_ip_entry.get(), self.profile_data["network_target_ip"])
        self.assertEqual(self.app.target_port_entry.get(), self.profile_data["network_target_port"])
        self.assertEqual(self.app.packet_size_entry.get(), self.profile_data["network_packet_size"])
        self.assertEqual(self.app.cpu_temp_limit_entry.get(), self.profile_data["cpu_temp_limit"])
        self.assertEqual(self.app.ram_free_threshold_entry.get(), self.profile_data["ram_free_threshold"])
        self.assertEqual(self.app.disk_free_threshold_entry.get(), self.profile_data["disk_free_threshold"])
        self.assertEqual(self.app.safety_monitoring_active.get(), self.profile_data["safety_monitoring_active"])

if __name__ == "__main__":
    unittest.main()