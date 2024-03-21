import unittest
from task1 import log_message


class TestLogMessage(unittest.TestCase):

    def setUp(self):
        self.log_file = "test_application.log"

    def tearDown(self):
        # Clear the log file after each test
        open(self.log_file, "w").close()

    def test_write_to_log_file(self):
        # Test writing to the log file
        message = "Test message"
        log_level = "INFO"
        expected_output = f"[{log_level}] {message}\n"
        log_message(self.log_file, message, log_level)
        with open(self.log_file, "r") as file:
            content = file.read()
        self.assertIn(expected_output, content)

    def test_long_message(self):
        # Test long message
        message = "A" * 1000
        log_message(self.log_file, message, "INFO")
        with open(self.log_file, "r") as file:
            content = file.read()
        self.assertIn(message, content)

    def test_special_characters(self):
        # Test special characters in message
        message = "!@#$%^&*()"
        log_message(self.log_file, message, "INFO")
        with open(self.log_file, "r") as file:
            content = file.read()
        self.assertIn(message, content)

    def test_existing_log_file(self):
        # Test existing log file
        initial_content = "Initial content\n"
        with open(self.log_file, "w") as file:
            file.write(initial_content)
        message = "Test message"
        log_message(self.log_file, message, "INFO")
        with open(self.log_file, "r") as file:
            content = file.readlines()
        self.assertIn(initial_content.strip(), content[0])
        self.assertIn(f"[INFO] {message}", content[1])


if __name__ == '__main__':
    unittest.main()
