# Plants monitor

## Plan

Goal: to control and monitor our plant growing setup.

### Hub

- UI to integrate controls, webcam feeds and sensor reading graphs
- API to proxy commands to devices, to accept sensor readings from devices
- clickhouse - to host logs and sensor readings
- grafana - to visualize data from clickhouse
- nginx to glue it all together

### Device

- script to report sensor readings to hub
- API to accept commands from hub
- webcam server
