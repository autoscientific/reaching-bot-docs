# ReachingBot Device Manager

!!! info "This is the legacy application"
    Device Manager (RBDM) is the original PySide6 desktop app. It is still
    supported, and is currently the **only** application that performs ML video
    scoring. For running sessions, see the
    [ReachingBot app](../app/index.md).

## Pages

- [Getting started](getting-started.md) — installing RBDM
- [Downloads](downloads.md) — installers and version history
- [Outcome classification](outcome-classification.md) — the ML video classifier and custom DeepLabCut models
- [Troubleshooting](troubleshooting.md) — common issues and fixes

Shared with the ReachingBot app:

- [Hardware setup and assembly](../hardware/setup.md)
- [Device drivers](../hardware/drivers.md)
- [Experiment config file](../reference/config-file.md)
- [Pellet detection](../reference/pellet-detection.md)
- [Video recording modes](../reference/video-recording-modes.md)
- [Motor API](../reference/motor-api.md)

## Should I still use it?

Yes, for two things:

- **Video scoring.** The outcome classifier and DeepLabCut pose estimation are
  not in the ReachingBot app.
- **An in-flight study.** Changing software versions in the middle of a study is
  not advisable without first testing.

The two apps read the same config files and write the same session folder
layout, so they can be used together — see
[Moving from Device Manager](../app/migrating.md).
