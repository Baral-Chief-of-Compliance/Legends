import React, {Component} from 'react';
import CreatPostPage from './CreatPostPage';
import LegendsPage from './LegendsPage';
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
        <Router>
            <Switch>
              <Route exact path="/">
                <p>Пошёл нахуй</p>
              </Route>
              <Route path="/create" component = {CreatPostPage} />
              <Route path="/legends" component = {LegendsPage} />
            </Switch>
        </Router>
  );
  }
}
