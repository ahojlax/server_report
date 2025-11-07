import datetime
import psutil
import socket
from report_utils import write_html

def perform_health_check(path):
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('C:\\')

    write_html('<table border=2 width=100% cellpadding=1 cellspacing=5 align=center><tr align=center bgcolor=saffron><td colspan=5><h1>server status report</h1></td></tr>', path)
    write_html('<tr><td align=center colspan=5><br><h3>Resource Monitor - Health Check Results</h3></td></tr>', path)
    write_html('<tr align=center><td><b>Server Name</b></td><td><b>Server Uptime</b></td><td><b>CPU Utilization</b></td><td><b>Memory Utilization</b></td><td><b>Disk Space (Available)</b></td></tr>', path)

    server_name = socket.gethostname()
    uptime_str = f"{uptime.days} Days : {uptime.seconds//3600} Hrs : {(uptime.seconds//60)%60} Mins"

    write_html(f"<tr align=center><td><b>{server_name}</b></td><td>{uptime_str}</td><td>{cpu}%</td><td>{memory.percent}%</td><td>{100 - disk.percent}%</td></tr>", path)
