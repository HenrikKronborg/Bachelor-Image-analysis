window.onload = tegn;

function tegn() {
	var canvas, o, tillatTegning, lagDott,
		X = 0, forrigeX = 0,
		Y = 0, forrigeY = 0,
		storrelse = 20,
		farge = "red";
	
	function initialiser() {
		canvas = document.getElementById("tegneOmraade");
		o = canvas.getContext("2d");
		
		bredde = canvas.width;
		hoyde = canvas.height;
		
		var bilde = new Image();
		bilde.onload = function () {
			o.drawImage(bilde, 0, 0);
		}
		bilde.src = "filter.png?" + new Date().getTime();
				
		canvas.addEventListener("mousemove", function (e) {
			posisjon("musBeveg", e)
        }, false);
        canvas.addEventListener("mousedown", function (e) {
			posisjon("musNed", e)
        }, false);
        canvas.addEventListener("mouseup", function (e) {
			posisjon("musOpp", e)
        }, false);
        canvas.addEventListener("mouseout", function (e) {
			posisjon("musUt", e)
        }, false);
	}
	initialiser();
	
	function tegn() {
		o.beginPath();
		o.moveTo(forrigeX, forrigeY);
		o.lineTo(X, Y);
		o.strokeStyle = farge;
		o.lineWidth = storrelse;
		o.lineJoin = o.lineCap = "round";
		o.stroke();
		o.closePath();
	}
	
	function posisjon(retning, e) {
		forrigeX = X;
		forrigeY = Y;
		X = e.clientX - canvas.getBoundingClientRect().left;
		Y = e.clientY - canvas.getBoundingClientRect().top;
		
		if(retning == "musNed") {
			tillatTegning = true;
			lagDott = true;
			
			if(lagDott) {
				o.beginPath();
				o.fillStyle = farge;
				o.arc(X, Y, storrelse / 2, 0, 2 * Math.PI);
				o.fill();
				o.closePath();
				lagDott = false;
			}
		}
				
		if(retning == "musOpp") {
			tillatTegning = false;
		}
		
		if(retning == "musBeveg") {
			if(tillatTegning) {
				tegn();
			}
		}
	}
	
	var formPenStorrelseElementer = document.forms['formPenStorrelse'].elements['penStorrelse'];
	for (var i = 0, lengde = formPenStorrelseElementer.length; i < lengde; i++) {
		formPenStorrelseElementer[i].onclick = function() {
			storrelse = this.value;
		};
	}
	
	var formPenTypeElementer = document.forms['formPenType'].elements['penType'];
	for (var i = 0, lengde = formPenTypeElementer.length; i < lengde; i++) {
		formPenTypeElementer[i].onclick = function() {
			if(this.value == 1) {
				farge = "red";
				o.globalCompositeOperation = "source-over";  
			}
			else if(this.value == 2) {
				o.strokeStyle = "rgb(255, 255, 255)";
				o.globalCompositeOperation = "destination-out";  
				o.fillStyle = "rgba(255,0,0,0)";
			}
		};
	}
	
	document.getElementById("lagre").onclick = function() {
		var imageData = o.getImageData(0, 0, canvas.width, canvas.height);
		var pixels = imageData.data;
		var varsling = document.getElementsByClassName("varsling")[0];
		var varslingInnhold = document.getElementById("varslingInnhold");
		var farge = "#3498db";

		var l = bredde * hoyde;
		var arrayK = new Array(bredde);
		for(var i = 0; i < bredde; i++) {
			arrayK[i] = new Array(hoyde);
		}
		
		for (var i = 0; i < l; i++) {
			var r = pixels[i*4];
			
			var y = parseInt(i / bredde, 10);
			var x = i - y * bredde;
			
			if(r == 255) {
				arrayK[x][y] = "1";
			}
			else {
				arrayK[x][y] = "0";
			}
		}
		
		//console.table(arrayK);
		
		var xmlhttp;
		xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = lagreSSH;
		xmlhttp.open("POST", "phpseclib/lagreTilTX2.php", true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send("arr=" + arrayK + "&bilde=" + canvas.toDataURL());
		
		varsling.style.display = "block";
		varsling.setAttribute("style", "display:block; background:" + farge);
		varslingInnhold.innerHTML = "Laster..";
		
		function lagreSSH() {
			if(xmlhttp.readyState === 4 && xmlhttp.status === 200) {
				var respons = "";
				
				if(xmlhttp.responseText == 0) {
					respons = "Tilkobling mislyktes. Bildeområde er lagret på webserver. Forsøk å lagre til TX2 på nytt senere";
					farge = "#E74C3C";
				}
				else {
					respons = "Bildeområde er lagret til TX2";
					farge = "#2ECC71";
				}
				varsling.style.backgroundColor = farge;
				varslingInnhold.innerHTML = respons;
			}
		}
		
		return false;
	}
	
	document.getElementById("hent").onclick = function() {
		var varsling = document.getElementsByClassName("varsling")[0];
		var varslingInnhold = document.getElementById("varslingInnhold");
		var farge = "#3498db";
		
		var xmlhttp;
		xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = lagreSSH;
		xmlhttp.open("POST", "phpseclib/hentFraTX2.php", true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send();
		
		varsling.style.display = "block";
		varsling.setAttribute("style", "display:block; background:" + farge);
		varslingInnhold.innerHTML = "Laster..";
		
		function lagreSSH() {
			if(xmlhttp.readyState === 4 && xmlhttp.status === 200) {
				var respons = "";
				
				if(xmlhttp.responseText == 0) {
					respons = "Tilkobling mislyktes. Forsøk igjen senere";
					farge = "#E74C3C";
				}
				else {
					document.getElementById("tegneReferanse").src = "referanse.png?" + new Date().getTime();
					respons = "Referansebilde er oppdatert";
					farge = "#2ECC71";
				}
				varsling.style.backgroundColor = farge;
				varslingInnhold.innerHTML = respons;
			}
		}
		
		return false;
	}
	
	document.getElementById("lagreInnstillinger").onclick = function() {
		var varsling = document.getElementsByClassName("varsling")[0];
		var varslingInnhold = document.getElementById("varslingInnhold");
		var farge = "#3498db";
		
		var xmlhttp;
		xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = lagreSSH;
		xmlhttp.open("POST", "phpseclib/lagreInnstillinger.php", true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send("fps=" + document.querySelector('input[name="fps"]:checked').value + "&format=" + document.querySelector('input[name="format"]:checked').value);
		
		varsling.style.display = "block";
		varsling.setAttribute("style", "display:block; background:" + farge);
		varslingInnhold.innerHTML = "Laster..";
		
		function lagreSSH() {
			if(xmlhttp.readyState === 4 && xmlhttp.status === 200) {
				var respons = "";
				
				if(xmlhttp.responseText == 0) {
					respons = "Tilkobling mislyktes. Forsøk igjen senere";
					farge = "#E74C3C";
				}
				else {
					respons = "Innstillingene er lagret til TX2";
					farge = "#2ECC71";
				}
				varsling.style.backgroundColor = farge;
				varslingInnhold.innerHTML = respons;
			}
		}
		
		return false;
	}
	
	document.getElementById("toggleMeny").onclick = function() {
		$("#menySlide").slideToggle(300);
	}
	
	$('input[type=radio][name=format]').change(function() {
		$('input[name="fps"]').each(function () {
			$(this).toggleClass("fire");
			$(this).toggleClass("tre");
		});
		
		if(this.value == 1) {
			$("#knapp4Toggle").show();
			$("input[name=fps][value=4]").prop("checked",true);
		}
		
		if(this.value == 2) {
			$("#knapp4Toggle").hide();
			$("input[name=fps][value=3]").prop("checked",true);
		}
	});
	
	document.getElementById("lukkVarsling").onclick = function() {
		document.getElementsByClassName("varsling")[0].style.display = "none";
	}
	
	document.getElementById("rens").onclick = function() {
		o.clearRect(0, 0, bredde, hoyde);
	}
}