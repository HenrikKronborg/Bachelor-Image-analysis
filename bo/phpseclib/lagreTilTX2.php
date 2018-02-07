<?php
/*
include("Net/SSH2.php");

$ssh = new Net_SSH2("158.39.162.210");
if (!$ssh->login("pi", "9Gruppe")) {
    exit("Login Failed");
}

//$ssh->enablePTY();
$variabelen = $_POST["arr"];
$ssh->exec("cd Desktop; echo "" . $variabelen . "" > config.txt");

*/
//$ssh->write("testtest\n");
//$ssh->read();

/*
include("Net/SFTP.php");

$sftp = new Net_SFTP("158.39.162.210");
if (!$sftp->login("pi", "9Gruppe")) {
	exit("Login Failed");
}

$img = str_replace("data:image/png;base64,", "", $_POST["b"]);
$img = str_replace(" ", "+", $img);
$fileData = base64_decode($img);
$fileName = "photo.png";
file_put_contents("../filter.png", $fileData);

$sftp->chdir("/home/pi/Desktop");
$sftp->put("filter.png", "../filter.png", NET_SFTP_LOCAL_FILE);
*/


$img = str_replace("data:image/png;base64,", "", $_POST["bilde"]);
$img = str_replace(" ", "+", $img);
$fileData = base64_decode($img);
file_put_contents("../filter.png", $fileData);

include("Net/SFTP.php");

$sftp = new Net_SFTP("158.39.162.206");
if (!$sftp->login("bachelor", "9Gruppe")) {
	exit("0");
}
else {
	echo 1;
}

$sftp->chdir("/home/bachelor/Desktop");
$sftp->put("filter.png", "../filter.png", NET_SFTP_LOCAL_FILE);
//$sftp->put("config.txt", $_POST["arr"]);
?>