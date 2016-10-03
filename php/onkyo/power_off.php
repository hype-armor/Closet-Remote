<?php
	system ("irsend SEND_ONCE onkyo KEY_OFF");
	header('Location: ' . $_SERVER['HTTP_REFERER']);
?>
