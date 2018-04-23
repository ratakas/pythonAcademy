import React from "react";

import Footer from "./Footer";
import Header from "./Header";

export default class Layout extends React.Component {
  constructor() {
    super();
    this.state = {
      title: "Welcome",
      value: 'Please write an essay about your favorite DOM element.',
      nombre: '',
      apellido: '',
      email:'',
      numTintas:0,
      ancho:0,
      largo:0,
      tipoImp:'0',
      tipoPapel:'',
      maquinaImp:'',
      pDesperdicioPapel:0.0,
      pUtilidad:0.0,
      numEtiquetas:0
    };

    
  }

  changeTitle(title) {
    this.setState({title});
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleChangeSelect(event){
    this.setState({tipoImp: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.nombre);
    
    if (this.state.tipoImp== '0') {
      const area= this.state.ancho*this.state.largo

      const costoPapel= 

      x= (area * this.state.numEtiquetas * costopapel) + ( tiempo de impresion * costo operador)

      Digital: ((área de la etiqueta) * cantidad de etiquetas * costo del papel) + (tiempo de impresión * costo por hora del operador)
    }

    event.preventDefault();


  }


  render() {
    return (
      <div>

      <Header changeTitle={this.changeTitle.bind(this)} title={this.state.title} />

     

      <div class="row">
      <div class="col-md-6">
        <form onSubmit={this.handleSubmit.bind(this)} >
          <div class="col-md-6">
              <div class="form-group">
                <label for="nombre"> Nombres</label>
                <input type="text" class="form-control" name="nombre" onChange={this.handleInputChange.bind(this)}/>
              </div>
              <div class="form-group">
                <label for="apellido"> Apellidos</label>
                <input type="text" class="form-control"  name="apellido" onChange={this.handleInputChange.bind(this)}/>
              </div>
              <div class="form-group">
                <label for="email">Correo Electronico:</label>
                <input type="email" class="form-control" name="email" onChange={this.handleInputChange.bind(this)}/>
              </div>

            {/*Cotización*/}

            <div class="form-group">
                <label for="numTintas"> Cantidad de Tintas</label>
                <input type="text" class="form-control" name="numTintas" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="ancho"> Ancho</label>
                <input type="text" class="form-control" name="ancho" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="largo"> Largo</label>
                <input type="text" class="form-control" name="largo" onChange={this.handleInputChange.bind(this)}/>
            </div>

          </div>
          <div class="col-md-6">

            <div class="form-group">
                <label for="tipoImp"> Tipo de Impresion</label>
                <select class="form-control" value={this.state.tipoImp} onChange={this.handleChangeSelect.bind(this)}>
                  <option value="0">digital</option>
                  <option value="1">flexográfica</option>
                  <option value="2">formas continuas</option>
              </select>
            </div>
            <div class="form-group">
                <label for="tipoPapel"> Tipo de papel</label>
                <input type="text" class="form-control" name="tipoPapel" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="maquinaImp">Maquina Imprimir</label>
                <input type="text" class="form-control" name="maquinaImp" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="pDesperdicioPapel"> Porcentae Desperdicio de Papel</label>
                <input type="text" class="form-control" name="pDesperdicioPapel" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="pUtilidad"> Porcentaje utilidad</label>
                <input type="text" class="form-control" name="pUtilidad" onChange={this.handleInputChange.bind(this)}/>
            </div>
            <div class="form-group">
                <label for="numEtiquetas"> Cantidad Etiquetas</label>
                <input type="text" class="form-control" name="numEtiquetas" onChange={this.handleInputChange.bind(this)}/>
            </div>
          </div>



        <button type="submit" class="btn btn-default">Submit</button>
        </form>

      </div>
      </div>
      <div class="col-md-6">

      </div>  



      </div>  
      
      );
  }
}
