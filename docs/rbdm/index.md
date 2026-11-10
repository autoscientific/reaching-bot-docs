# ReachingBot Device Manager

!!! info "This is the legacy application"
    Device Manager (RBDM) is the original PySide6 desktop app. It is still
    supported, but the [ReachingBot app](../app/index.md) now covers the whole
    workflow, scoring included, and is the one to use for new work.

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

For most work, no — the [ReachingBot app](../app/index.md) does everything
Device Manager does, and its [Scoring](../app/scoring.md) produces identical
predictions.

Three reasons remain:

- **Scoring options the app leaves out** — the p-value setting, per-video
  trajectory CSVs, the labelled-video export, and
  [custom DeepLabCut models](outcome-classification.md#using-custom-deeplabcut-models)
  from the config.
- **An Intel Mac.** The ReachingBot app is Apple silicon only, and needs
  macOS 13 or later.
- **An in-flight study.** Changing software versions in the middle of a study is
  not advisable without first testing.

The two apps read the same config files and write the same session folder
layout, so they can be used together or interchangeably — see
[Moving from Device Manager](../app/migrating.md).
