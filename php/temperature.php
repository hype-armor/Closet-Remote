<?php
$cpuTempSensor = exec('cat /sys/class/thermal/thermal_zone0/temp');
$airTempSensor = exec('cat /sys/bus/w1/devices/28-0000079e4172/w1_slave');

$cpuTemp = round(floatval($cpuTempSensor) / 1000, 0);

$airTemp = round(floatval(explode("=",$airTempSensor)[1]) / 1000, 0);

echo 'CPU: ';
echo $cpuTemp;
echo ' Air: ';
echo $airTemp;
?>