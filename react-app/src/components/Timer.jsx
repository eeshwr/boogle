import React from "react";
class Timer extends React.Component {
    render() {
        return <div>Timer : {this.props.minutes}:{this.props.seconds}</div>;
    }
}

export default Timer;