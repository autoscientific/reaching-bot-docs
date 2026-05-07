# Pellet Detection

Pellet detection is handled by the camera on your ReachingBot. An algorithm scans a Region of Interest (ROI) of each captured frame for the pellet, filtered by area.

To accommodate the different pellets you might use with the devices, you can configure the detection parameters from within the software.

*Pellet size*

The unit is pixels$^2$ and may require some tweaking to get right. There’s some pre-set values for common 20 mg and 45 mg pellets but you can confirm this by clicking “Display Feed” on a connected device and visually confirming that the pellet is being detected.

*Pellet detection ROI*

As of version 2.4.0 of ReachingBot Device Manager, the region of interest (ROI) for pellet detection can now be configured in the `experiment_name.yaml` file. This allows users to define a specific area within each captured frame where the algorithm scans for the pellet. By adjusting the ROI parameters in the configuration file, users can customize the detection area to best suit their experimental setup and pellet size. It’s best to configure the zone to be as confined around where the pellet will sit in its final position.

Again, after tweaking the values `y1_offset`, `y2_offset`, `x1_offset` and `x2_offset` the ROI will be denoted by the white rectangle in the frame after clicking “Display Feed” on a connected device.
