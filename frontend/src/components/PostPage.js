import React, { Component } from 'react';
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
      .then(res => {
        const posts = res.data;
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
          {this.state.posts.map(post => <div>{ post.name } <img src = { post.img }/></div>)}
        </div>
      </div>
    )
  }
}
