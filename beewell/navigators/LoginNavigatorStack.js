import React from 'react';
import {Hives, SignIn, SignUp, GeneralInfoView, MedicalDetailsView, EmergencyContactView, IsinHealthCareView }  from '../screens/screens_index.js';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';



 function LoginNavigatorStack() {
    return ( 
    <NavigationContainer>
    <Stack.Navigator initialRouteName = 'Sign In' screenOptions = {{headerShown : false}}>       
    <Stack.Screen name = 'Sign In' component = {SignIn} />
    <Stack.Screen name = 'Hives' component = {Hives} />
    <Stack.Screen name = 'General Info' component = {GeneralInfoView} />
    <Stack.Screen name = 'Medical Details' component = {MedicalDetailsView} />
    <Stack.Screen name = 'Emergency Contact' component = {EmergencyContactView} />
    <Stack.Screen name = 'Is in Healthcare' component = {IsinHealthCareView} />


    </Stack.Navigator>
    </NavigationContainer>
    );
}

const Stack = createStackNavigator();

export default LoginNavigatorStack ; 