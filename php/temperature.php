<?php
$cpuUsage = exec('top -bn1 | grep "Cpu(s)" | \
           sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk \'{print 100 - $1"%"}\'');
$memUsage = round(floatval(exec('top -bn1 | awk \'FNR == 4 {print $3/($3+$5)*100}\'')),0);

$cpuTempSensor = exec('cat /sys/class/thermal/thermal_zone0/temp');
$airTempSensor = exec('cat /sys/bus/w1/devices/28-0000079e4172/w1_slave');

$cpuTemp = round(floatval($cpuTempSensor) / 1000, 0);

$airTemp = round(floatval(explode("=",$airTempSensor)[1]) / 1000, 0);

echo 'CPU: ';
echo $cpuUsage;
echo ' ';
echo 'MEM: ';
echo $memUsage;
echo '% ';
echo $cpuTemp;
echo '°C ';
echo ' Air: ';
echo $airTemp;
echo '°C';
?>