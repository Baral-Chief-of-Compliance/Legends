import React, { Component } from 'react';
import {useParams} from 'react-router-dom';
import axios from 'axios';
import OnePostDetail from './OnePostDetail';




 export default class OnePostPage extends Component {

  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/Post/2/')
      .then(response => {
        debugger;
        const posts = response.data;
        this.setState({ posts });
      })
  }


  render(){
    return(
      <div>
        <div>
          Пост под номером
        </div>
        <div>
          <OnePostDetail {...this.props} />
        </div>
      </div>
    )
  }
}
