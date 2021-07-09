
import {StyleSheet, useWindowDimensions} from 'react-native';

const windowWidth = useWindowDimensions().width;
const windowHeight = useWindowDimensions().height;

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
        marginTop: windowHeight*0.2,
        paddingTop: windowHeight*0.1,
        width: windowWidth*0.8,
        height: windowHeight*0.4,
        alignSelf: 'center',
    },
    DatePicker: {
        paddingTop: 10,
        marginTop: windowHeight*0.4,
        width: windowWidth,
        height: windowHeight,
        flexDirection:'column',
        justifyContent: 'center',
        alignItems: 'center',
        alignSelf: 'center',
    },
    GenderPicker: {
        backgroundColor: 'white',
        opacity: 0.8,
    },
    DatePickerClose: {
        width: '40%',
        marginTop: 40,
        flexDirection:'column',
        backgroundColor: 'grey',
        borderRadius: 25,
        alignContent: 'center',
        textAlign: 'center',
        alignSelf: 'center',
    },
    DatePickerCloseText: {
        padding: 10,
        fontSize: 18,
        fontWeight: 'bold',
        color: 'white',
        alignSelf: 'center',
    },



});

export default styles;