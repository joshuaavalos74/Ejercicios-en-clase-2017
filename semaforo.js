function Semaforo(state){
	var divSemaforo= document.createElement("div");
	divSemaforo.className="principal";
	var divRojo = document.createElement("div");
	divRojo.className= "rojo";
	var divAmarillo = document.createElement("div");
	divAmarillo.className= "amarillo"
	var divVerde = document.createElement("div");
	divVerde.className= "verde"

	divSemaforo.appendChild(divRojo);
	divSemaforo.appendChild(divAmarillo);
	divSemaforo.appendChild(divVerde);

	if (state == 0){
		divRojo.style.opacity= 1.0;
	};
	if (state ==2) {
		divAmarillo.style.opacity=1.0;
	};

	if (state==1){
		divVerde.style.opacity=1.0;
	}

	return divSemaforo;
}

function render (mountPoint, component, state){
	mountPoint.innerHTML= "";
	mountPoint.appendChild(component(state));
}

var color= 0;

var root= document.getElementById("root");

render(root, Semaforo, color)

var botonazo= document.getElementById("btn");

botonazo.onclick= function(){
	color++;
	if (color>2) {
		color=0;
	};
	render(root, Semaforo, color);
}