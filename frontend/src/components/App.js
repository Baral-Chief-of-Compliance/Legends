import React, {Component} from 'react';
import { render } from 'react-dom';
import HomePage from './HomePage';
import LegendsPage from './LegendsPage';
import CreatPostPage from './CreatPostPage';



export default class App extends Component {
  constructor(props){
    super(props);
  }

  render(){
    return <HomePage />
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);
