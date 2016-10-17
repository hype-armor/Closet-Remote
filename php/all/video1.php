<?php
	system ("irsend SEND_ONCE hdmi INPUT1");
    sleep(1);
    system ("irsend SEND_ONCE hdmi STEREO");
    system ("irsend SEND_ONCE onkyo KEY_VIDEO1");
?>