import React from 'react';
import SignIn  from './screens/sign_in.js';
import Hives  from './screens/hives.js';
import SignUp  from './screens/sign_up.js';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';


export default function App() {
    return ( 
    <NavigationContainer>
    <Stack.Navigator initialRouteName = 'SignIn' screenOptions = {{headerShown : false}}>       
    <Stack.Screen name = 'SignIn' component = {SignIn} />
    <Stack.Screen name = 'Hives' component = {Hives} />
    <Stack.Screen name = 'SignUp' component = {SignUp} />

    </Stack.Navigator>
    </NavigationContainer>
    );
}

const Stack = createStackNavigator();
