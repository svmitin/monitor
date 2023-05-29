install:
	mkdir /opt/monitor
	cp monitor.py /opt/monitor/
	cp monitor.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl start monitor

remove:
	systemctl stop monitor
	rm -rf /opt/monitor
	rm /opt/monitor/monitor.py
	rm /etc/systemd/system/monitor.service
	systemctl daemon-reload
