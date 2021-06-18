import React from 'react';
import {GeneralInfoView, MedicalDetailsView, EmergencyContactView, IsinHealthCareView }  from '../screens/screens_index.js';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';


 function SignUpNavigatorStack() {
    return ( 
        <NavigationContainer>
    <SignUpStack.Navigator initialRouteName = 'General Info' screenOptions = {{headerShown : false}}>       
    <SignUpStack.Screen name = 'General Info' component = {GeneralInfoView} />
    <SignUpStack.Screen name = 'Medical Details' component = {MedicalDetailsView} />
    <SignUpStack.Screen name = 'Emergency Contact' component = {EmergencyContactView} />
    <SignUpStack.Screen name = 'Is in Healthcare' component = {IsinHealthCareView} />

    </SignUpStack.Navigator>
    </NavigationContainer>
    );
}

const SignUpStack = createStackNavigator();

export default SignUpNavigatorStack ; 