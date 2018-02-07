<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta name="description" content="">
	<meta name="author" content="">

	<title>Filter</title>
	
	<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />
	<link href="stil.css" rel="stylesheet">
	
	<script type="text/javascript" src="script.js"></script>
</head>

<body>
	<div class="kontainer">
		<div class="rad">
			<h1>Hessdalen - Kontrollpanel</h1>
			
			<div class="innholdVenstre">
				<ul class="meny">
					<li class="padding">
						Størrelse
						<form action="" id="formPenStorrelse" class="pen-container">
						<label>
							<input type="radio" class="none" name="penStorrelse" value="6">
							<span class="pen liten"></span>
						</label>
						<label>
							<input type="radio" class="none" name="penStorrelse" value="20" checked>
							<span class="pen middels"></span>
						</label>
						<label>
							<input type="radio" class="none" name="penStorrelse" value="60">
							<span class="pen stor"></span>
						</label>
						</form>
					</li>
					<li>
						<form action="" id="formPenType" class="knappGruppe">
							<input type="radio" class="knapp" name="penType" id="penType1" value="1" checked>
							<label for="penType1">Tegn</label>
							<input type="radio" class="knapp" name="penType" id="penType2" value="2">
							<label for="penType2">Viskelær</label>
						</form>
					</li>
					<li><a id="hent">Hent nytt referansebilde</a></li>
					<li><a id="lagre">Lagre</a></li>
					<li class="rens"><a id="rens" class="siste">Rens filter</a></li>
				</ul>
				
				<div class="varsling">
					<span class="lukk" id="lukkVarsling">&times;</span>
					<div id="varslingInnhold"></div>
				</div>
				
				<ul class="meny">
					<li><a id="toggleMeny">Endre innstillinger</a></li>
					<div id="menySlide">
						<form action="" id="innstillinger">
							<li>
								<div class="paddingK">Framerate</div>
								<input type="radio" class="knapp fire ingenB" name="fps" id="fps1" value="1">
								<label for="fps1">3.75</label>
								<input type="radio" class="knapp fire" name="fps" id="fps2" value="2">
								<label for="fps2">7.5</label>
								<input type="radio" class="knapp fire" name="fps" id="fps3" value="3">
								<label for="fps3">15</label>
								<div id="knapp4Toggle">
									<input type="radio" class="knapp fire" name="fps" id="fps4" value="4" checked>
									<label for="fps4">30</label>
								</div>
							</li>
							<div class="clear"></div>
							<li>
								<div class="paddingK">Format</div>
								<input type="radio" class="knapp ingenB" name="format" id="format1" value="1" checked>
								<label for="format1">Gråskala</label>
								<input type="radio" class="knapp" name="format" id="format2" value="2">
								<label for="format2">Farger</label>
							</li>
							<div class="clear"></div>
							<li><a id="lagreInnstillinger" class="siste">Lagre</a></li>
						</form>
					</div>
				</ul>
			</div>
			
			<div class="innholdHoyre">
				<div class="canvasContainer">
					<img id="tegneReferanse" src="referanse.png" />
					<canvas id="tegneOmraade" width="720" height="576"></canvas>
				</div>
				<img id="tegneResultat" />
			</div>
		</div>
	</div>
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</body>
</html>