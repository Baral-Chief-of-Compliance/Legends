import React, {Component} from 'react';
import { render } from 'react-dom';
import CreatPostPage from './CreatPostPage';
import LegendsPage from './LegendsPage';
import PostPage from './PostPage';
import OnePostPage from './OnePostPage';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Switch,
  Redirect,
} from "react-router-dom";


export default class HomePage extends Component {
  constructor(props){
    super(props);

  }


  render(){
    return (
      <div>
        <Router>
            <Switch>
              <Route exact path="/">
                <p>Пошёл нахуй</p>
              </Route>
              <Route path="/create" component = {CreatPostPage} />
              <Route path="/legends" component = {LegendsPage} />
              <Route exact path="/posts" component = {PostPage} />
              <Route path="/posts/:id" component = {OnePostPage}/>
            </Switch>
        </Router>
      </div>
  );
  }
}
