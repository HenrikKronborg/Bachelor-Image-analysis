<?php
include("Net/SFTP.php");

$sftp = new Net_SFTP("158.39.162.206");
if (!$sftp->login("bachelor", "9Gruppe")) {
	exit("0");
}
else {
	echo 1;
}

$sftp->chdir("/home/bachelor/Desktop");
unlink("../referanse.png");
$sftp->get("referanse.png", "../referanse.png");
?>