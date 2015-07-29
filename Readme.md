# Ava

Records mouse coordinates when they change.

Started out as an experiment to visualise data that an everyday computer usage generates.

### Windows:

1. Install win32gui (good luck!)
2. Set launch.vbs as a Basic Task in Scheduled Task to launch on restart.

### OSX
1. Get MouseTools.app and place in the same folder
2. From same folder, launch Terminal and : 
	```nohup python track.pyw &```