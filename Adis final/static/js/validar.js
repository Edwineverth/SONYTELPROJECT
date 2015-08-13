function validar(f){
	var cedula=f.document.formulario.cedula;
	if(cedula==null){
		alert("entro")
		return false;
	}

	return true;
}