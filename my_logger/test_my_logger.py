
import logging
import io
import unittest

from my_logger.my_logger import get_logger, MyLogFormatter


class TestLogFormat(unittest.TestCase):

    logger_name = 'TestLogFormatApp'

    def setUp(self):

        self.formatter = MyLogFormatter()
        self.stream = io.StringIO()
        self.handler = logging.StreamHandler(self.stream)
        self.logger = get_logger(self.logger_name)

        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)

    def tearDown(self):
        pass

    def test_number_of_handlers(self):
        logger = get_logger(self.logger_name)
        self.assertEqual(1, len(logger.handlers))

    def test_debug(self):

        message = 'test debug message'
        with self.assertLogs(logger=self.logger_name, level='DEBUG') as cm:

            self.logger.debug(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\[D\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s\w*\]\s)')

    def test_info(self):

        message = 'test info message'
        with self.assertLogs(logger=self.logger_name) as cm:

            self.logger.info(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\[I\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s\w*\]\s)')

    def test_warning(self):

        message = 'test warning message'
        with self.assertLogs(logger=self.logger_name) as cm:
            self.logger.warning(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\[W\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s\w*\]\s)')

    def test_warning(self):

        message = 'test error message'
        with self.assertLogs(logger=self.logger_name) as cm:
            self.logger.error(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\[E\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s\w*\]\s)')

    def test_critical(self):

        message = 'test critical message'
        with self.assertLogs(logger=self.logger_name) as cm:
            self.logger.critical(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\[C\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s\w*\]\s)')

    def test_color(self):

        message = 'test color message'
        with self.assertLogs(logger=self.logger_name) as cm:

            self.logger.warning(message)
            self.handler.flush()

            log_message = self.handler.format(cm.records[-1]).strip()
            self.assertRegex(log_message, r'(\x1b)')
