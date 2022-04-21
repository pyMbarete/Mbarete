var files = new Array();
function registrar (name,pwd,size,fecha,id){
  this.name = name;
  this.pwd = pwd;
  this.size = size;
  this.fecha = fecha;
  this.id = id;
  return this;
  }
files[0] = new registrar("cara_frontal.png","mbarete_1",26337,17-02-22 19:52:24,0); 
files[1] = new registrar("48289380Y_TFG_14412834227804295580822753741684.pdf","mbarete_2",8176746,17-02-22 19:52:24,1); 
files[2] = new registrar("imagenes.docx","mbarete_3",1,17-02-22 19:52:24,2); 
