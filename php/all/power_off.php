<?php
	system ("irsend SEND_ONCE onkyo KEY_OFF");

	// attempt to turn on hdmi switch.
	system ("irsend SEND_ONCE hdmi POWER");

	// turn off projector 
	system ("irsend SEND_ONCE viewsonic KEY_POWER");
	sleep(2);
	system ("irsend SEND_ONCE viewsonic KEY_POWER");

	// turn off Apple TV
	system ("irsend SEND_START appletv KEY_PLAY");
    sleep(10);
	system ("irsend SEND_STOP appletv KEY_PLAY");
?>
