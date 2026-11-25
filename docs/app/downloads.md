# ReachingBot app downloads

Installers for the current ReachingBot app. For the legacy Device Manager, see
its own [Downloads page](../rbdm/downloads.md).

Before installing, read [Install](install.md) — it covers the macOS and Windows
first-launch prompts, which you will hit, and the platform requirements
(**Apple silicon and macOS 13 or later**; there is no Intel Mac build).

!!! info "Downloads need a username and password"
    The installers are available to ReachingBot customers only. When you click a
    download, your browser asks for a username and password: use the ones
    Autoscientific sent you. If you don't have them, or they no longer work,
    email [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk).

<!-- app-releases -->

## Which file

| Platform | File |
| --- | --- |
| macOS, Apple silicon | `.dmg` |
| Windows | `.msi`, or the `.exe` installer |
| Linux | `.deb`, or the `.AppImage` |

Nothing else needs installing alongside the app — Python and the scoring models
ship inside it, which is why the downloads are large.

!!! note "Match the firmware"
    As with Device Manager, changing software versions in the middle of a study
    is not advisable without first testing. Session and camera behaviour depend
    on the firmware installed on each device, which you can check and update
    from the [Devices](devices.md#firmware) view.
