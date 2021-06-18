
import {StyleSheet} from 'react-native';
// import { Dimensions } from 'react-native';

// const windowWidth = Dimensions.get('window').width;
// const windowHeight = Dimensions.get('window').height;

const styles = StyleSheet.create({


    signInInput: {
        width: '75%',
        backgroundColor: '#f9f9f9',
        borderRadius: 25,
        margin: 5,
        justifyContent: 'flex-start',
        paddingHorizontal: 20,
        flexDirection: 'row',
        alignItems: 'center',
    },

    container: { 
        flex: 1,
        backgroundColor: '#FFFFFF',
        alignItems: 'center',
        justifyContent: 'center',
    },

    SignInContainer: {
        flex: 1,
        height: '100%',
        width: '100%',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#FFFFFF',
        padding: 10,
    },

    SignInButton: {
        width: '75%',
        margin: 5,
        paddingHorizontal: 20,
        backgroundColor: 'grey',
        borderRadius: 25,
        margin: 20,
    },
    SignInButtonText: {
        padding: 10,
        fontSize: 18,
        fontWeight: 'bold',
        color: 'white',
        alignSelf: 'center',
    },


    SignInText: {
        padding: 20,
        marginLeft: 20,
        paddingLeft: 25,
    },

    SignUpText: {
        color: 'darkslategrey',
        fontWeight:'100',
    },
    
    SignUpTextClickable: {
        color: 'darkslategrey',
        fontWeight: 'bold',
    },

    SignUpTextContainer: {
        position: 'absolute',
        bottom: '5%',
        flexDirection:'row',
    },
    SignUpFormTextInput: {
        width: '100%',
        backgroundColor: '#f9f9f9',
        borderRadius: 2,
        margin: 5,
        justifyContent: 'center',
        paddingHorizontal: 20,

    },
    SignUpFormText: {
        color: 'darkslategrey',
        margin: 5,
        justifyContent: 'center',
        paddingHorizontal: 20,
        fontWeight: '700',

    },
    NextButton: {
        width: '60%',
        marginTop: 40,
        margin: 20,
        backgroundColor: 'grey',
        borderRadius: 25,
    },
    PreviousButton: {
        width: '60%',
        marginTop: 40,
        margin: 20,
        backgroundColor: 'grey',
        borderRadius: 25,
        

    },
    SignUpNavigationContainer: {
        height:'25%',
        width: '100%',
        borderRadius: 25,
        flexDirection: 'row-reverse',
    },
    SignUpFormContainer: {
        paddingTop: 10,
        height: '75%',
        width: '100%',
    },
    DateInput: {
        paddingTop: 10,
        // width: windowWidth/2,
    },




});

export default styles;