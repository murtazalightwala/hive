import React from 'react';
import { StyleSheet, Text, View, } from 'react-native';
import styles from './styles.js';


class Hives extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {styles.container}> 
            <Header />
            <TopTabBar />
            <HivesBody />
            <BottomTabBar />


        </View>
    }
}

class Header extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Logo />
            <SearchIcon />
            <HamIcon />

        </View>
    }
}
class TopTabBar extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>This is top tab bar</Text>

        </View>
    }
}
class HivesBody extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>This is Hives Body</Text>

        </View>
    }
}

class BottomTabBar extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>This is bottom tab bar</Text>

        </View>
    }
}

class Logo extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>Logo</Text>

        </View>
    }
}


class SearchIcon extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>SI</Text>

        </View>
    }
}
class HamIcon extends React.Component {
    constructor(props) {
        super(props);
    }

    render()
    {
        return <View style = {this.props.style}> 
            <Text>HI</Text>

        </View>
    }
}

export default Hives;