import React, {Component} from 'react';
import { Link } from 'react-router-dom';


export default class CreatPostPage extends Component {
  constructor(props){
    super(props);
  }

  render(){
    return (
      <div className='create-post-page'>
        <div className='create-post-page-label'>
          Создание поста
        </div>
        <div>
          <Link to="/">
            <button type="button">
              Нажми на меня
            </button>
          </Link>
        </div>

      </div>
    )
  }
}
