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
