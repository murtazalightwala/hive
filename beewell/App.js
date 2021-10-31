import React from 'react';
import {AsyncStorage } from 'react-native';
import {LoginNavigatorStack, LoginNavigatorStack as SignUp, SignUpNavigatorStack}  from './navigators/index.js';
import { createStackNavigator } from '@react-navigation/stack';


const RootNav = createStackNavigator();

class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            user: null,
        }
    }


render() {
    return ( 
 this.state.user == null ? (<LoginNavigatorStack />) : (<SignUpNavigatorStack />)


 

 );

    }
}

export default App;