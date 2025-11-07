import os
import datetime
from win32com.client import GetObject
from report_utils import write_html


def perform_service_check(path, services):
    write_html('<tr><td align=center colspan=5><br><h3>Test Results</h3></td></tr>', path)
    write_html('<tr><td><b>Datetime</b></td><td><b>Service Name</b></td><td><b>Test Task</b></td><td><b>Result</b></td><td><b>Details</b></td></tr>', path)

    wmi = GetObject('winmgmts:')
    for svc in services:
        service = wmi.ExecQuery(f"Select * from Win32_Service where Name='{svc['name']}'")
        now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')

        if not service:
            write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td align=center><font color=red>Test - Failed</font></td><td>Service Not Found.</td></tr>", path)
            continue

        status = list(service)[0].State
        if status != "Running":
            write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td align=center><font color=red>Test - Failed</font></td><td>Service Not Running</td></tr>", path)
        else:
            write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td>Service is Up and Running</td><td align=center><font color=green>&#9745;</font></td><td><font color=green>OK</font></td></tr>", path)

        if os.path.exists(svc['log']):
            with open(svc['log'], 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
                err_count = content.count("error")
                warn_count = content.count("warn")
                if err_count > 0:
                    write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td>Check log file for errors</td><td align=center><font color=red>Test - Failed</font></td><td>Errors: {err_count}<br/>Warnings: {warn_count}</td></tr>", path)
                else:
                    write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td>Check log file for errors</td><td align=center><font color=green>&#9745;</font></td><td>Errors: 0<br/>Warnings: {warn_count}</td></tr>", path)
        else:
            write_html(f"<tr><td>{now}</td><td>{svc['name']}</td><td>Log file does not exist</td><td align=center><font color=red>Test - Failed</font></td><td>File Not Found.</td></tr>", path)
