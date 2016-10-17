<?php
	system ("irsend SEND_ONCE onkyo KEY_OFF");

	// attempt to turn on hdmi switch.
	system ("irsend SEND_ONCE hdmi POWER");

	// turn off Apple TV
	system ("irsend SEND_START appletv KEY_PLAY");
    sleep(5);
	system ("irsend SEND_STOP appletv KEY_PLAY");
?>
