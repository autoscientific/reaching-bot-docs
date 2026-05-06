# ReachingBot: Documentation

Table of Contents

# Getting Started

### Installation of ReachingBot Device Manager

A link to the latest ReachingBot device manager software can be downloaded and installed from the [Downloads Page](https://www.notion.so/Downloads-2d33df1f8acd4d5b9f688063dc2d0fa3?pvs=21).

Follow the on-screen instructions until the desktop application is installed. Windows and Mac OSX installers are available. Please note that the Mac OSX installer is not backwards compatible and requires firmware version 3>.

A walkthrough of ReachingBot Device Manager can be found [here](https://youtu.be/fuWDxj7Tz7A).

[https://youtu.be/fuWDxj7Tz7A](https://youtu.be/fuWDxj7Tz7A)

### Connection layout

ReachingBots are connected to your PC via the supplied powered USB hub. Connect each ReachingBot to one of the 7 USB ports on the powered hub that are blue. These ports can supply power to the devices and also allow your PC to communicate with them too. The bottom most three can only supply power so should not be used. 

You can also connect your ReachingBot directly to your PC using the supplied USB A - USB C cable , but, be mindful that your PC may not be able to supply its required power, and lead to unstable behaviour. For this reason, it is recommended that the supplied powered USB hub is used.

![Group 9.png](ReachingBot%20Documentation/Group_9.png)

### Before you begin

Your ReachingBot may arrive disassembled for safe travel. Please screw together the components indicated by the red arrows in the image above before continuing.

![rb_screw_arrow.jpg](ReachingBot%20Documentation/rb_screw_arrow.jpg)

### Chamber assembly

Chambers are made from clear acrylic panels that assemble together using the supplied M3 x 20 mm screws and square nuts. Use [this video](https://www.youtube.com/watch?v=szwCmlw77bg) as a visual guide on how to assemble these chambers. In order to increase the contrast between the pellets and the background from with the camera frame, a dark backdrop is also supplied, which can be inserted into the front panel.

[https://www.youtube.com/watch?v=szwCmlw77bg](https://www.youtube.com/watch?v=szwCmlw77bg)

The chamber remains in a fixed position relative to the dispensing unit. The dispensing unit can be moved via the guides within the aluminium base and fixed together with the clamps. 

Note, when the dispenser is positioned in the “shaping” position, i.e. as close to the front panel of the chamber as possible, the backdrop will need to be positioned within the chamber. This can be re-positioned to the outside of the chamber once the animal learns to grasp for pellets with the dispenser in its furthest position if the user wishes to do so.

### Drivers

Before the ReachingBot Device Manager can recognise your devices, you will first need to change the device drivers. You will only need to do this once for any given PC you chose to use with your devices. You will also only need to do this for one ReachingBot, not each one.

For a visual demonstration on how to do this, watch [this YouTube video](https://www.youtube.com/watch?v=XaTmG708Mss) from the 7:20 minute mark.

1. **Download the correct drivers**

You can do this by navigating to [this](https://www.catalog.update.microsoft.com/Search.aspx?q=USB+RNDIS+Gadget) page and downloading the driver pictured in the below screenshot:

![Screenshot 2024-01-08 at 14.10.19.png](ReachingBot%20Documentation/Screenshot_2024-01-08_at_14.10.19.png)

Download and unpack its contents in a known location on your PC. 

1. **Navigate to the Device Manager on your PC and find where the ReachingBot is connected**

It should be listed as a COM port, i.e. **COM3**

1. **Right click this device and choose “Update driver”** under advanced settings. It will give you the option to either locate the driver automatically over the internet, or manually.

Chose manually, and navigate to the folder where you previously downloaded the driver.

This will now update the drivers for the ReachingBots and you will be able to connect to them from within the ReachingBot Device Manager software.

# Pellet Detection

Pellet detection is handled by the camera on your ReachingBot. An algorithm scans a Region of Interest (ROI) of each captured frame for the pellet, filtered by area. 

To accommodate the different pellets you might use with the devices, you can configure the detection parameters from within the software. 

*Pellet size*

The unit is pixels$^2$ and may require some tweaking to get right. There’s some pre-set values for common 20 mg and 45 mg pellets but you can confirm this by clicking “Display Feed” on a connected device and visually confirming that the pellet is being detected.

*Pellet detection ROI*

As of version 2.4.0 of ReachingBot Device Manager, the region of interest (ROI) for pellet detection can now be configured in the `experiment_name.yaml` file. This allows users to define a specific area within each captured frame where the algorithm scans for the pellet. By adjusting the ROI parameters in the configuration file, users can customize the detection area to best suit their experimental setup and pellet size. It’s best to configure the zone to be as confined around where the pellet will sit in its final position. 

Again, after tweaking the values `y1_offset`, `y2_offset`, `x1_offset` and `x2_offset` the ROI will be denoted by the white rectangle in the frame after clicking “Display Feed” on a connected device.

# Outcome classification: *things to note*

ReachingBot Device Manager comes equipped with a machine-learning based video outcome classifier that makes a prediction of what happened during the short video snippets recorded. Currently, the possible outcomes are as follows: 

| **Outcome** | **Description** |
| --- | --- |
| Hit | The animal successfully takes the pellet, bringing it to its mouth without dropping it at any point in the video trial and eats the pellet in full. |
| Miss | The pellet was displaced from the pedestal but is knocked away or dropped in the retraction phase. Even if the mouse successfully takes the pellet, brings it to its mouth but then drops it, this will count as a miss. |
| PelletNotTaken | This is an edge case, but occasionally videos may be recorded wrongly with pellets remaining on the pedestal |
| PelletNotPresentInVideo | Occasionally, a video will be recorded where there isn’t a pellet present at the start of the video. |

(Please also see [our paper published in J Neuro Methods](https://pubmed.ncbi.nlm.nih.gov/37331430/) for more detail)

For the best chance of optimal prediction accuracy, move the dispenser to the furthest position away from the slot so as not to allow animals to cheat and grasp for pellets with their tongue.

Finally, ensure the the front panel is as clear as possible so as to give the camera the best chance as possible to “see” the mouse having taken or dropped the pellet.

## Using custom DeepLabCut models

From RBDM version 2.5.0>, we added the ability to use custom DeepLabCut models. That is, models that have been fine-tuned by **auto***s*cientic based on videos that you have collected.

The way to point your RBDM to the model you’d like to use is by specifying it in the config.yaml file, like so:

```yaml
PoseEstimationModel: /path/to/folder/DLC_autoscientific_reachingBot_resnet_50_iteration-6_shuffle-1
```

***n.b.** It’s the path to the entire folder that you should specify*

Please note: because of the nature of machine learning models, prediction accuracy cannot be guaranteed, and is up to the user to confirm that the prediction accuracy of video outcomes are maintained. 

The outcome classifier depends on the integrated DeepLabCut model working well. If the environment that you have set your ReachingBots differ significantly from the environment the model was initially trained, this may lead to inaccurate feature tracking. You can confirm this by choosing a video from the interface below within the RBDM software, clicking the “**create a labelled video”** radio button, and then **“Process Video”.** If you find that the model does not work well, it may need to be re-trained.

We cannot guarantee the models we train using DeepLabCut will track the features of rodents reliably enough for kinematic/trajectory analysis. Users are encouraged to train their own models for this purpose.

![Screenshot 2024-03-29 at 21.11.26.png](ReachingBot%20Documentation/Screenshot_2024-03-29_at_21.11.26.png)

Please reach out to [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk) if alterations need to be made and we can explore this together.

# Video recording modes (experimental)

*Continuous video recording is an experimental release of the software and may be unstable, please report any issues to* [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk).

As of RBDM 2.5.1 and firmware version 2.5.0-pre-release, we have released a new mode of video acquisition, in addition to ‘segmented’ mode.

With the above versions of the software, “continuous” video capture can be enabled by adding the following line to the config file of each device you’d like to have shoot in this mode:

```yaml
Devices:
  ReachingBot1:
    camera_position: Same side as motor
    x1_offset: 0.6
    x2_offset: 0.875
    y1_offset: 0.61
    y2_offset: 0.98
    fps: 100
    shooting_mode: continuous
```

By default, when new config files are created with RBDM 2.5.1, `shooting_mode` is added, and `segmented` is specified.

**Segmented:** Only the frames captured before and after the pellet is displaced from the pellet are encoded to video.

**Continuous:** All frames throughout the session are captured into 1 minute chunks. By the end of the session, all 1 minute chunks are saved to your host PC as they did before.

***n.b.*** 

1. Due to the fact these videos are larger files, they take longer to encode. At the end of a given session, it will take around 40 seconds for the last 1 minute video to save before they are all downloaded to your PC. 
2. We have only attempted `continuous` shooting mode with a frame capture rate of 100 FPS (the same as segmented), altering the FPS value may lead to unexpected results and is not recommended for now.

### **Why would you choose one over the other?**

**”Segmented”** mode creates an array of videos at the end of each session that confines the video to what happens only around when the pellet is displaced. This means that you have shorter, space efficient video files, that, in theory, should only capture the components of the session where most activity is happening. Also, when segmented mode is used, videos largely follow the same format, which facilitates the classification of these videos into “hits” or “misses”.

However, this relies heavily on robust pellet detection, if the experimental conditions change significantly that might alter how well the pellet detection works, videos may not be captures in a way that is satisfactory.

**”Continuous”** mode captures all frames. This means, say, if you have an injured animal that makes reach attempts that can’t quite displace the pellet (which wouldn’t trigger a video recording in segmented video), this information is captured. Furthermore, the issue outlined previously, with pellet detection becoming compromised, all frames are captures regardless.

Pipelines to segment and analyse these videos are still being created.

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