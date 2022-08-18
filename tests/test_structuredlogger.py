import json
import logging
import unittest
from datetime import datetime
from io import StringIO

from src.gcstructuredlogger import structuredlogger


class TestStructuredLogger(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(f"logging-test-{datetime.now().timestamp()}")
        self.logger.setLevel(logging.DEBUG)
        self.buffer = StringIO()

        self.logHandler = logging.StreamHandler(self.buffer)
        self.logHandler.setFormatter(structuredlogger.StructuredJsonFormatter())
        self.logger.addHandler(self.logHandler)

    def test_set_severity(self):
        self.logger.debug("DEBUG")
        self.logger.info("INFO")
        self.logger.warning("WARNING")
        self.logger.error("ERROR")
        self.logger.critical("CRITICAL")
        self.logger.fatal("CRITICAL")

        ndjson = self.buffer.getvalue()
        log_json = json.loads("[{}]".format(ndjson.replace("\n", ",")[:-1]))
        for log in log_json:
            self.assertEqual(log["message"], log["severity"])

    def test_set_stack_trace(self):
        try:
            1 / 0
        except ZeroDivisionError as e:
            self.logger.error(e, exc_info=True)

        log_json = json.loads(self.buffer.getvalue())
        self.assertIn("ZeroDivisionError: division by zero", log_json["stack_trace"])

    def test_set_types_if_error_occurred(self):
        self.logger.debug("DEBUG")
        self.logger.info("INFO")
        self.logger.warning("WARNING")
        self.logger.error("ERROR")
        self.logger.critical("CRITICAL")
        self.logger.fatal("CRITICAL")

        ndjson = self.buffer.getvalue()
        log_json = json.loads("[{}]".format(ndjson.replace("\n", ",")[:-1]))
        for log in log_json:
            if log["severity"] in ["DEBUG", "INFO", "WARNING"]:
                self.assertIsNone(log.get("@type"))
            else:
                self.assertEqual(
                    log["@type"],
                    "type.googleapis.com/google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent",
                )
