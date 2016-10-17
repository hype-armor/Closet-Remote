<?php
	system ("irsend SEND_ONCE hdmi INPUT2");
    sleep(1);
    system ("irsend SEND_ONCE hdmi SURROUND");
    system ("irsend SEND_ONCE onkyo KEY_VIDEO2");
?>