# ReachingBot app

The ReachingBot app is the current desktop application for running reaching
tasks on a fleet of ReachingBots. It replaces the
[ReachingBot Device Manager](../rbdm/getting-started.md) for everything except
ML video scoring.

It is a single window with three views:

| View | What it does |
| --- | --- |
| [Devices](devices.md) | The fleet: connect, tune session parameters, run and stop sessions, preview the camera, download videos, update firmware, serve the motor API |
| [Configuration builder](configuration-builder.md) | Build the experiment YAML: name the study, set device login, scan for and add ReachingBots, add animals |
| [Inspect](inspect.md) | Read the results CSVs from sessions you have downloaded |

## What is different from Device Manager

- **Per-device settings are editable.** Motor type, shooting mode, camera FPS,
  camera view and the pellet-detection ROI can be changed per device from its
  row in the Configuration builder, at any point. Device Manager hardcoded most
  of these.
- **Sessions stream live.** Device output is forwarded to the app as it
  happens, with trial progress and elapsed time on the device card, rather than
  being polled.
- **No ML scoring.** The video outcome classifier and the DeepLabCut pose
  estimation are not part of this app — see [Scoring](#scoring) below.
- **Same config files.** Both apps read and write the same experiment YAML, so
  a config made in one opens in the other. See
  [Experiment config file](../reference/config-file.md).
- **Linux is supported**, alongside macOS and Windows.

[Moving from Device Manager](migrating.md) covers this in more detail.

## Scoring

The ML scoring pipeline is **not** part of this app. Scoring pulled in `torch`,
`ultralytics`, `onnxruntime`, `scikit-learn`, `pandas` and `opencv` — together
they turned a 22-package backend into a 199-package one and would have added
gigabytes to every installer.

To score videos, run the videos through
[ReachingBot Device Manager](../rbdm/outcome-classification.md). Videos
downloaded by the ReachingBot app land in the same directory layout, so Device
Manager can read them.

## Getting started

1. [Hardware setup and assembly](../hardware/setup.md)
2. [Device drivers](../hardware/drivers.md)
3. [Install the app](install.md)
4. [Build a configuration](configuration-builder.md)
5. [Run a session](devices.md)
