import React, { Component} from 'react';



export default class LegendsPage extends Component {
  constructor(props){
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }


  componentDidMount(){
    fetch("api/Legend_IVT/")
      .then(response => {
        if(response.status > 400){
          return this.setState(() => {
            return { placeholder: "Что-то пошло не так!"};
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }


  render(){
    return (
      <div style={{'overflow':'auto'}}>
        <p>Легенды ИВТ</p>
        <p>ааааааааааааа</p>
          <p>Список Легенд</p>
          <ul>
            {this.state.data.map(Legend_IVT => {
              return(
                <li key={Legend_IVT.id}>
                  {Legend_IVT.name} {Legend_IVT.surname}-<img src = { Legend_IVT.photo }/>
                </li>
              );
            })}
          </ul>
      </div>
      )
  }
}
