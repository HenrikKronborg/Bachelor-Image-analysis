<?php
Header("content-type: image/jpeg");
/*
$img = imagecreatefrompng('filter.png');
imagefilter($img, IMG_FILTER_GRAYSCALE); //first, convert to grayscale
imagefilter($img, IMG_FILTER_CONTRAST, -100); //then, apply a full contrast
*/
$bilde = ImageCreateFromPng("filter.png"); 

$bredde = imagesx($bilde);
$hoyde = imagesy($bilde);

for ($i = 0; $i < $bredde; $i++) {
	for ($j = 0; $j < $hoyde; $j++) {
		$rgb = ImageColorAt($bilde, $i, $j); 
		
		$rod = ($rgb >> 16) & 0xFF;

		if($rod > 0x7F) {
			$farge = 0x00;
		}
		else {
			$farge =0xFF;
		}
		
		$val = imagecolorallocate($bilde, $farge, $farge, $farge);
		
		imagesetpixel($bilde, $i, $j, $val);
	}
}

imagepng($bilde);

?>