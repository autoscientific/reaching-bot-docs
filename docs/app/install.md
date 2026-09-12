# Installing the ReachingBot app

!!! warning "Installer links are not published yet"
    At the time of writing there is no published release of the ReachingBot app,
    and the source repository is private — so this page cannot yet link to
    installers the way the [Device Manager downloads page](../rbdm/downloads.md)
    does. Until builds are hosted publicly (the Device Manager installers are
    served from a CloudFront distribution), ask
    [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk) for a build.

Nothing else needs installing alongside the app. The Python backend is frozen
into the bundle, so an installed copy needs neither Python nor `uv` on the
machine.

Before installing, make sure the hardware is assembled and the
[device drivers](../hardware/drivers.md) are in place.

## Choosing an installer

| Platform | File |
| --- | --- |
| macOS, Apple silicon | `.dmg` (`aarch64`) |
| macOS, Intel | `.dmg` (`x86_64`) |
| Windows | `.msi`, or the `.exe` installer |
| Linux | `.deb`, or the `.AppImage` |

The two macOS builds are separate downloads rather than one universal binary:
the bundled Python backend is a native binary, so each architecture is built on
its own machine. Pick the one matching your Mac (Apple menu → About This Mac).

The Linux builds are produced on Ubuntu 22.04, which sets the oldest glibc — and
so the oldest distribution — they will run on.

## First launch on macOS and Windows

Builds are **not** signed with an Apple Developer ID or an Authenticode
certificate, so both operating systems will warn you the first time:

- **macOS** — right-click (or Control-click) the app and choose **Open**, then
  confirm. Double-clicking will be refused. You only need to do this once.
- **Windows** — on the SmartScreen prompt, choose **More info → Run anyway**.

## Versions

The version shown in the app matches the release tag it was built from
(for example tag `v0.2.0` → version `0.2.0`).

Unlike Device Manager, the app does not have to match a particular firmware
version to start, but session and camera behaviour do depend on the firmware
installed on each device. You can check and update firmware from the
[Devices view](devices.md#firmware).

## Next

- [Build a configuration](configuration-builder.md)
- [Run a session](devices.md)
