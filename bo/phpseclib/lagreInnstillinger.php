<?php
include("Net/SFTP.php");

$sftp = new Net_SFTP("158.39.162.206");
if (!$sftp->login("bachelor", "9Gruppe")) {
	exit("0");
}
else {
	echo 1;
}

if($_POST['format'] == 1) {
	$format = "GRAY8";
	if($_POST['fps'] == 1) { $fps = 3.75; }
	if($_POST['fps'] == 2) { $fps = 7.5; }
	if($_POST['fps'] == 3) { $fps = 15; }
	if($_POST['fps'] == 4) { $fps = 30; }
}
elseif($_POST['format'] == 2) {
	$format = "YUY2";
	if($_POST['fps'] == 1) { $fps = 3.75; }
	if($_POST['fps'] == 2) { $fps = 7.5; }
	if($_POST['fps'] == 3) { $fps = 15; }
}

$sftp->chdir("/home/bachelor/Desktop");
$sftp->put("config.txt",
			"1024\n768\n" .
			$format . "\n" . 
			$fps);
?>