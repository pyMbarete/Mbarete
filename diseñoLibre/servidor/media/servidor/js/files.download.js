var files = new Array();
function registrar (name,pwd,size,fecha,id){
  this.name = name;
  this.pwd = pwd;
  this.size = size;
  this.fecha = fecha;
  this.id = id;
  return this;
  }
files[0] = new registrar("BLES02014.rar","media/servidor/download/BLES02014.rar",8100855906,1632953535.54993,0); 
files[1] = new registrar("midireccionIP.txt","media/servidor/download/midireccionIP.txt",0,1633571567.5226216,1); 
