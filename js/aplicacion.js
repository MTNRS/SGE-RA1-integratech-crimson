async function cargarJson(ruta) {
  const respuesta = await fetch(ruta);
  if (!respuesta.ok) throw new Error(`No se pudo cargar ${ruta}`);
  return respuesta.json();
}

function textoSeguro(valor) {
  const elemento = document.createElement("span");
  elemento.textContent = valor;
  return elemento.innerHTML;
}

async function mostrarSistemas() {
  const sistemas = await cargarJson("datos/sistemas.json");
  const tarjetas = document.querySelector("#tarjetas");
  const tabla = document.querySelector("#tabla-sistemas");

  tarjetas.innerHTML = sistemas.map(sistema => `
    <article class="tarjeta">
      <h3>${textoSeguro(sistema.nombre)}</h3>
      <p><strong>${textoSeguro(sistema.tipo)}</strong></p>
      <p>${textoSeguro(sistema.caracteristicas)}</p>
      <a href="${textoSeguro(sistema.fuente)}" target="_blank" rel="noopener">Fuente oficial</a>
    </article>
  `).join("");

  tabla.innerHTML = sistemas.map(sistema => `
    <tr>
      <td>${textoSeguro(sistema.nombre)}</td>
      <td>${textoSeguro(sistema.licencia)}</td>
      <td>${textoSeguro(sistema.sistema_operativo)}</td>
      <td>${textoSeguro(sistema.gestor_datos)}</td>
    </tr>
  `).join("");
}

async function mostrarVerificacion() {
  const contenedor = document.querySelector("#resultado");
  try {
    const resultado = await cargarJson("resultado_verificacion.json");
    const clase = resultado.correcto ? "correcto" : "error";
    contenedor.innerHTML = `<strong class="${clase}">${resultado.correcto ? "Configuración correcta" : "Revisión necesaria"}</strong>`;
    resultado.comprobaciones.forEach(comprobacion => {
      const linea = document.createElement("p");
      linea.className = `comprobacion ${comprobacion.correcto ? "correcto" : "error"}`;
      linea.textContent = `${comprobacion.correcto ? "✓" : "✗"} ${comprobacion.nombre}: ${comprobacion.detalle}`;
      contenedor.appendChild(linea);
    });
  } catch (error) {
    contenedor.textContent = "Ejecuta el verificador desde un servidor local para actualizar el resultado.";
  }
}

mostrarSistemas().catch(error => document.querySelector("#tarjetas").textContent = error.message);
mostrarVerificacion();
