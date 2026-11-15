# Experiment config file

Both the [ReachingBot app](../app/index.md) and the legacy
[Device Manager](../rbdm/getting-started.md) are driven by one YAML file per
experiment. They read and write the **same** schema, so a config built in either
application opens in the other.

The file is normally created for you — by the app's
[Configuration builder](../app/configuration-builder.md), or Device Manager's
Setup tab — but it is plain YAML and can be edited by hand.

## Where it lives

The builder writes `{project folder}/{experiment name}.yaml` and creates a
`ReachingBotVideos` folder next to it, which becomes `VideoDirectory`.

## Example

```yaml
Animals:
  M-2271: Right
  M-2272: To be determined
Devices:
  reachingbot-461d06b2:
    connection:
      transport: ssh
      username: your-device-username
      password: your-device-password
    camera_position: Opposite motor
    motor_type: MG996R
    shooting_mode: segmented
    fps: 100
    y1_offset: 0.61
    y2_offset: 0.98
    x1_offset: 0.6
    x2_offset: 0.875
DownloadCSV: false
PoseEstimationModel: default
VideoDirectory: /path/to/project/ReachingBotVideos
```

## Top-level keys

| Key | Notes |
| --- | --- |
| `Animals` | Map of animal ID → paw preference (`To be determined`, `Left` or `Right`) |
| `Devices` | Map of device hostname → the per-device block below |
| `DownloadCSV` | When `true`, CSVs are downloaded alongside the videos |
| `PoseEstimationModel` | `default`, or a path to a custom DeepLabCut model. Read by Device Manager only — the ReachingBot app's [Scoring](../app/scoring.md) always uses its built-in model |
| `VideoDirectory` | Where downloaded sessions are written locally |

## Per-device keys

| Key | Default | Notes |
| --- | --- | --- |
| `connection.transport` | `ssh` | |
| `connection.username` | — | Device SSH user. Supplied to you by email |
| `connection.password` | — | Device SSH password. Required |
| `ip_address` | — | Optional host or IP address. Left out when blank, in which case the ReachingBot app reaches the device at `<hostname>.local`. **Ignored by Device Manager**, which always reaches devices by hostname |
| `camera_position` | `Opposite motor` | Or `Same side as motor`, which flips the frame |
| `motor_type` | `MG996R` | Or `MG90S` for the legacy motors. Sets the default servo positions, used until the device has a saved [servo calibration](../app/devices.md#servo-calibration) |
| `shooting_mode` | `segmented` | Or `continuous` — see [Video recording modes](video-recording-modes.md) |
| `fps` | `100` | Camera frame rate |
| `y1_offset` | `0.61` | [Pellet-detection ROI](pellet-detection.md), top edge as a fraction of frame height |
| `y2_offset` | `0.98` | ROI bottom edge |
| `x1_offset` | `0.6` | ROI left edge as a fraction of frame width |
| `x2_offset` | `0.875` | ROI right edge |

The four ROI offsets are all-or-nothing: supply all four, or none, in which case
the device falls back to its own defaults.

!!! warning "The config holds a password"
    The device password is stored in plain text. Treat the config file as a
    credential — keep it out of shared drives and version control.

## What is *not* in the config

Session parameters — trial count, time limit and pellet detection area — are
**not** saved in the config. Nor is a device's servo calibration, which is
stored on the device itself. In the ReachingBot app
they are set per run in the
[Session parameters](../app/devices.md#session-parameters) panel.

!!! note "Compatibility"
    Changing software versions in the middle of a study is not advisable without
    first testing, and some keys need a minimum firmware version — `shooting_mode`
    in particular. Check the [Device Manager downloads](../rbdm/downloads.md)
    notes for the version pairings.
