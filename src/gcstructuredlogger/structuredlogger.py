from datetime import datetime

from pythonjsonlogger import jsonlogger


class StructuredJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(StructuredJsonFormatter, self).add_fields(log_record, record, message_dict)

        if log_record.get("exc_info"):
            log_record["stack_trace"] = log_record["exc_info"]
            log_record.pop("exc_info")

        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.now().isoformat()
        if log_record.get("severity"):
            log_record["severity"] = log_record["severity"].upper()
        else:
            log_record["severity"] = record.levelname

        if log_record["severity"] in ["ERROR", "CRITICAL"]:
            log_record[
                "@type"
            ] = "type.googleapis.com/google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent"
