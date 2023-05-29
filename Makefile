install:
	mkdir /opt/monitor
	cp monitor.py /opt/monitor/
	cp monitor.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl monitor start

remove:
	rm -rf /opt/monitor
	rm /opt/monitor/monitor.py
	rm /etc/systemd/system/monitor.service
	systemctl daemon-reload
