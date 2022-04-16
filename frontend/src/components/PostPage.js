import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import axios from 'axios';


export default class PostPage extends Component {
  constructor(props){
    super(props);
    this.state = {
      posts: []
    };
  }


  componentDidMount(){
    axios.get('api/Post')
      .then(response => {
        const posts = response.data;
        this.setState({ posts });
      })
  }

  render(){
    return(
      <div>
        <div>
          Посты
        </div>
        <div>
          {this.state.posts.map(post => <div key = { post.id }> <NavLink to = {'/posts/'+post.id}>{ post.name }</NavLink> <img src = { post.img }/></div>)}
        </div>
      </div>
    )
  }
}
