<?php
	system ("irsend SEND_ONCE onkyo KEY_ON");

	// attempt to turn on hdmi switch.
	system ("irsend SEND_ONCE hdmi POWER");

	// turn off Apple TV
	system ("irsend SEND_ONCE appletv KEY_MENU");

	// attempt to turn on projector
	system ("irsend SEND_ONCE viewsonic KEY_POWER");
?>
