# Pellet detection

Pellet detection is handled by the camera on your ReachingBot. An algorithm scans a Region of Interest (ROI) of each captured frame for the pellet, filtered by area.

This applies to both applications — they configure the same detector on the same
firmware.

To accommodate the different pellets you might use with the devices, you can configure the detection parameters from within the software.

## Pellet size

The unit is pixels² and may require some tweaking to get right. There’s some pre-set values for common 20 mg and 45 mg pellets but you can confirm this by displaying the camera feed on a connected device and visually confirming that the pellet is being detected.

=== "ReachingBot app"

    Set the **Detection area** — a smallest and largest value — in the
    [Session parameters](../app/devices.md#session-parameters) panel on the
    Devices view. It applies to every session started from that page and to the
    camera feed, and is not saved into the config.

    Click **Feed** on an idle device to check it.

=== "Device Manager (legacy)"

    Set the pellet size in the software, then click **Display Feed** on a
    connected device to check it.

## Pellet detection ROI

The region of interest (ROI) defines the area within each captured frame where the algorithm scans for the pellet. Confining it tightly around where the pellet will sit in its final position gives the most reliable detection.

The ROI is defined by four offsets, each a fraction of the frame:

| Key | Default | Edge |
| --- | --- | --- |
| `y1_offset` | `0.61` | Top, as a fraction of frame height |
| `y2_offset` | `0.98` | Bottom |
| `x1_offset` | `0.6` | Left, as a fraction of frame width |
| `x2_offset` | `0.875` | Right |

All four must be set together — see [Experiment config file](config-file.md).

=== "ReachingBot app"

    The ROI is **per device** and editable in the app: open a device's row in
    the [Configuration builder](../app/configuration-builder.md#per-device-settings)
    and edit the four offsets there, at any point.

=== "Device Manager (legacy)"

    As of version 2.4.0 of ReachingBot Device Manager, the ROI can be configured
    in the `experiment_name.yaml` file by editing the four offsets by hand.

After tweaking the values, the ROI is denoted by the white rectangle in the camera feed.

## Checking detection

Good pellet detection is a white circle around the pellet, inside the white ROI rectangle, that tracks it steadily and doesn’t flicker. If it flickers or the circle never appears:

- Check the detection area brackets your pellet's actual size in the frame
- Check the ROI actually covers where the pellet sits
- Check the camera position setting matches the hardware (`Opposite motor` vs `Same side as motor`) — otherwise the ROI is mirrored
- Increase the contrast between pellet and background using the supplied dark backdrop
