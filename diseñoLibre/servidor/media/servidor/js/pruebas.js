<!--
document.write("<h1>Gracias por Visitar el Sitio</h1>");

var videoAncho = 500;
var videoAlto = 200;
var exten = new Array();
exten[0] = '.mp4';
exten[1] = '.mkv';
exten[2] = '.wmv';
exten[3] = '.png';
exten[4] = '.jpg';
exten[5] = '.jpeg';
exten[6] = '.mp3';
exten[7] = '.pdf';
exten[8] = '.webm';
var formato = false;
var ret = -1;
var fleng = files.length;
var ext = ' ' ;
var text = '<ul>';
for (i=0; i< fleng; i++){
	formato = false
	for (t=0 ; t<exten.length ; t++){
		ret = -1
		ret = files[i].name.indexOf(exten[t])
		if ( ret > -1 ){ formato = true ; ext = exten[t]}
		}
	if ( formato == true ){
		text += "<h2>"+files[i].name+"</h2>"
		switch(ext) {
			case '.mp4':
				text += '<video width="'+videoAncho+'" preload=none heigth="'+videoAlto+'" controls="controls">'
				text += '<source src="'+files[i].pwd+'" type="video/mp4" />'
				text += 'Your browser does not support the video tag.'
				text += '</video>'
			break;
			case '.mkv':
				text += '<video width="'+videoAncho+'" preload=none heigth="'+videoAlto+'" controls="controls">'
				text += '<source src="'+files[i].pwd+'" type="video" />'
				text += 'Your browser does not support the video tag.'
				text += '</video>'
			break;
			case '.webm':
				text += '<video width="'+videoAncho+'" preload=none heigth="'+videoAlto+'" controls="controls">'
				text += '<source src="'+files[i].pwd+'" type="video/webm" />'
				text += 'Your browser does not support the video tag.'
				text += '</video>'
			break;
			case '.wmv':
				text += '<video width="'+videoAncho+'" preload=none heigth="'+videoAlto+'" controls="controls">'
				text += '<source src="'+files[i].pwd+'" type="video/wmv" />'
				text += 'Your browser does not support the video tag.'
				text += '</video>';
			break;
			case '.mp3':
				text +=  '<audio controls>'
				text +=  '<source src="'+files[i].pwd+'" preload=none type="audio/mpeg"/>'
				text +=  '<p>Your fle does not support the audio element</p>'
				text +=  '</audio>'
			break;
			default:
				text +=  '<a href ="'+files[i].pwd+'"> <img src="ver.jpg" width="'+videoAncho+'"  alt=" el archivo no puede ser mostrado " /> </ a>'
			break;
			}
			text += "<br>"	
		}
	}
text += '</ul>';
document.write(text);
//-->
