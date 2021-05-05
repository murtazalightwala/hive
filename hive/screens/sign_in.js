import React from 'react';
import {Text, View, Button } from 'react-native';
import styles from './styles.js'; 

class SignIn extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {styles.SignInContainer}> 
            <SignInButton navigation = {this.props.navigation} />
            <SignUpText navigation = {this.props.navigation}/>

        </View>
    }
}

class SignInButton extends React.Component {

    constructor(props) {
        super(props);
    

    this.SignInButtonPress = this.SignInButtonPress.bind(this);


    }

    SignInButtonPress() {

        this.props.navigation.navigate('Hives')
        }
    
    
        


    render()
    {
        return <Button style = {styles.SignInButton} onPress = {this.SignInButtonPress} title = "Sign In" />
    }
}


class SignUpText extends React.Component {

    constructor(props) {
        super(props);
    
        this.SignUpButtonPress = this.SignUpButtonPress.bind(this);
    }

    SignUpButtonPress() {

        this.props.navigation.navigate('SignUp')
        }


render()
{
    return <Text style = {styles.SignUpText} onPress = {this.SignUpButtonPress}> Sign Up </Text>
}
}


export default SignIn;

