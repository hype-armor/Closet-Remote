<?php
$output = exec('cat /sys/bus/w1/devices/28-0000079e4172/w1_slave');
$temp = (explode("=",$output));
$floatTemp = floatval($temp[1]);
echo round($floatTemp / 1000, 2);
?>