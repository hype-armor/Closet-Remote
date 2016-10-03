<?php
	system ("irsend SEND_ONCE onkyo KEY_POWER");
	header('Location: ' . $_SERVER['HTTP_REFERER']);
?>
