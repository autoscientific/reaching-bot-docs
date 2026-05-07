# Troubleshooting

1. ***I’ve updated the device drivers, but when I click “Scan Devices”, no devices are found***

    This may be down to you computer’s firewall configuration, try again but having disabled your firewall protections.

2. ***My devices appear when I run “Scan Devices”, but when I load the config file that was made using the setup tab, the devices appear as “Not connected”***

    This is likely due to the config file missing some parameters, ensure that the username and password are entered. These will be supplied to you by email. If you do not have this information, please email **info@autoscientific.co.uk**

3. ***When I run a session, pellets are picked up by the arm, but not being registered as dispensed.***
    1. Always check that your camera is configured correctly via the config file. By default, your ReachingBot will be configured such that the camera is “Opposite motor”. Ensure that this option is selected when creating your config.yaml file.
    2. Ensure that good pellet detection happens by clicking on the **“Display Feed”** button under the camera column. Good pellet detection is when a white circle appears around the pellet within the region of interest outlined by the white rectangle in the camera feed, and that it doesn’t flicker.
    3. Failing the above, it may also be possible that the device has no space left having accumulated too many videos. In this case, the videos need to be deleted (see below).
4. ***I can’t run a session and the device reports an OSError: No Space Left On Device***

    Your device has run out of disk space. Navigate to **Videos** in the task bar and click **“Delete Videos On Connected Devices”.** This action will permanently delete the videos stored on your devices. Note: a copy of each video is automatically transferred to your control computer after each session ends.


For additional help and support, email: **info@autoscientific.co.uk**
