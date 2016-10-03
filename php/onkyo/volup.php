<?php
	system ("irsend SEND_ONCE onkyo KEY_VOLUMEUP");
	header('Location: ' . $_SERVER['HTTP_REFERER']);
?>
