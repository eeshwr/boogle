
import React from "react";
import "./layouts/button.css";

class StartButton extends React.Component {
    render() {
        return <button className="button roundButton" onClick={this.props.handleClick}>{this.props.buttonText}</button>;
    }
}
export default StartButton;