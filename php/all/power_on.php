<?php
	system ("irsend SEND_ONCE onkyo KEY_ON");

	// attempt to turn on hdmi switch.
	system ("irsend SEND_ONCE hdmi POWER");

	// turn off Apple TV
	system ("irsend SEND_ONCE appletv KEY_MENU");
?>
