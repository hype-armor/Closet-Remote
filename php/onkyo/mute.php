<?php
	system ("irsend SEND_ONCE onkyo KEY_MUTE");
	header('Location: ' . $_SERVER['HTTP_REFERER']);
?>
