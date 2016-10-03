<?php
	system ("irsend SEND_ONCE onkyo KEY_VOLUMEDOWN");
	header('Location: ' . $_SERVER['HTTP_REFERER']);
?>
