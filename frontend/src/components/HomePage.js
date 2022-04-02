import React, {Component} from 'react';
import CreatPostPage from './CreatPostPage';
import LegendsPage from './LegendsPage';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";


export default class HomePage extends Component {
  constructor(props){
    super(props);
  }

  render(){
    return (
      <Router>
        <Routes>
          <Route path="/" element = {<HomePage/>} />
          <Route path="/create" element={<CreatPostPage/>} />
          <Route path="/legends" element={<LegendsPage/>} />
        </Routes>
    </Router>
  );
  }
}
