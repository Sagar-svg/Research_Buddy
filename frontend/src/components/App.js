import Header from "./Header";
import Vidcontainer from "./Vidcontainer";
import Fileupload from "./Fileupload";
import {useState} from 'react';
import './App.css'


import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component {
    
    state = { list: [] }

    onSearch = (search) =>{
        fetch(`http://localhost:8000/api/${search.search}/`)
        .then((response) => response.json())
        .then(vidList => {
            this.setState({list: vidList.videos});
            //console.log(vidList.videos);
        });
       

    }


    render() {
        return (
            <div className='container'>
                <Header onSearch = {this.onSearch}/>
                <Fileupload />
                <div className='vidcontainer'>
                    <Vidcontainer  vidList={this.state.list}/>
                    
                </div>
            </div>
        );
    }
};


ReactDOM.render(<App />, document.getElementById('app'));

