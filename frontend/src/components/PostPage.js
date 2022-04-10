import React, { Component } from 'react';


export default class PostPage extends Component {
  constructor(props){
    super(props);
    this.state = {
      data: []
    };
  }


  componentPhoto(){
    fetch("api/Post/")
      .then(response => {
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data
          };
        });
      });
  }

  render(){
    return(
      <div>
        <div>
          Посты
        </div>
        <div>
          {this.state.data.map(Photo=>{
            return(
              <div key={ Photo.id }>
                 { Photo.name } <img src = { Photo.img }/>
              </div>
            );
          })}
        </div>
      </div>
    )
  }
}
