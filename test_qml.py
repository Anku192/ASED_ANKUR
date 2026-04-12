import unittest
import subprocess


class TestQML(unittest.TestCase):

    def test_script_runs(self):
        """Check if qml.py runs without error"""
        result = subprocess.run(
            ["docker", "run", "--rm", "qml-app"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)

    def test_output_exists(self):
        """Check if output is printed"""
        result = subprocess.run(
            ["docker", "run", "--rm", "qml-app"],
            capture_output=True,
            text=True
        )
        self.assertTrue(len(result.stdout) > 0)


if __name__ == "__main__":
    unittest.main()