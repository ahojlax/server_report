import os
import datetime
from win32com.client import GetObject
from server_report.report_utils import write_html
from server_report.logger import logger  # Make sure logger.py is in your project

def check_service_status(service_name):
    try:
        wmi = GetObject('winmgmts:')
        result = wmi.ExecQuery(f"Select * from Win32_Service where Name='{service_name}'")
        return list(result)[0].State if result else None
    except Exception as e:
        logger.error(f"Error querying service '{service_name}': {e}")
        return None

def analyze_log_file(log_path):
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
            return content.count("error"), content.count("warn")
    except Exception as e:
        logger.warning(f"Could not read log file '{log_path}': {e}")
        return None, None

def perform_service_check(path, services):
    write_html('<tr><td align=center colspan=5><br><h3>Test Results</h3></td></tr>', path)
    write_html('<tr><td><b>Datetime</b></td><td><b>Service Name</b></td><td><b>Test Task</b></td><td><b>Result</b></td><td><b>Details</b></td></tr>', path)

    for svc in services:
        now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        service_name = svc['name']
        log_path = svc['log']

        status = check_service_status(service_name)

        if status is None:
            write_html(f"<tr><td>{now}</td><td>{service_name}</td><td align=center><font color=red>Test - Failed</font></td><td>Service Not Found.</td></tr>", path)
            continue

        if status != "Running":
            write_html(f"<tr><td>{now}</td><td>{service_name}</td><td align=center><font color=red>Test - Failed</font></td><td>Service Not Running</td></tr>", path)
        else:
            write_html(f"<tr><td>{now}</td><td>{service_name}</td><td>Service is Up and Running</td><td align=center><font color=green>&#9745;</font></td><td><font color=green>OK</font></td></tr>", path)

        if os.path.exists(log_path):
            err_count, warn_count = analyze_log_file(log_path)
            if err_count is None:
                write_html(f"<tr><td>{now}</td><td>{service_name}</td><td>Log file unreadable</td><td align=center><font color=red>Test - Failed</font></td><td>Read Error</td></tr>", path)
            elif err_count > 0:
                write_html(f"<tr><td>{now}</td><td>{service_name}</td><td>Check log file for errors</td><td align=center><font color=red>Test - Failed</font></td><td>Errors: {err_count}<br/>Warnings: {warn_count}</td></tr>", path)
            else:
                write_html(f"<tr><td>{now}</td><td>{service_name}</td><td>Check log file for errors</td><td align=center><font color=green>&#9745;</font></td><td>Errors: 0<br/>Warnings: {warn_count}</td></tr>", path)
        else:
            logger.warning(f"Log file not found for service '{service_name}' at {log_path}")
            write_html(f"<tr><td>{now}</td><td>{service_name}</td><td>Log file does not exist</td><td align=center><font color=red>Test - Failed</font></td><td>File Not Found.</td></tr>", path)
