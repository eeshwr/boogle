import React from "react";
import "./App.css";
import Board from "./components/Board";
import TextBox from "./components/TextBox";
import WordList from "./components/WordList";
import Timer from "./components/Timer";
import StartButton from "./components/StartButton";

class App extends React.Component {

  state = {
    emptyBoard: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']],
    boardState: [['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']],
    newBoard: [],
    correct_words: [],
    words: [],
    seconds: '00',
    minutes: '00',
    buttonText: "New Game",
    disabled: true
  };

  addWord = word => {
    var value = this.state.correct_words.find(element => {
      return element.trim().toUpperCase() === word.trim().toUpperCase()
    });
    if (value) {
      this.setState({ words: [...this.state.words, word.trim()] });
    }
    else {
      alert("Invalid word");
    }
  };

  tick = () => {
    var min = Math.floor(this.secondsRemaining / 60);
    var sec = this.secondsRemaining - min * 60;

    this.setState({
      minutes: min,
      seconds: sec
    });

    if (sec < 10) {
      this.setState({
        seconds: "0" + this.state.seconds
      });
    }

    if (min < 10) {
      this.setState({
        minutes: "0" + min
      });
    }

    if ((min === 0) & (sec === 0)) {
      clearInterval(this.intervalHandle);
      this.setState({ disabled: true, buttonText: "New Game" });
    }

    this.secondsRemaining--;
  };

  handleClick = async () => {

    var buttonValue = this.state.buttonText;

    if (buttonValue === "New Game") {
      buttonValue = "Start Game";
      const url = "http://localhost:5000/load_boogle";
      const response = await fetch(url, { mode: "cors" });
      const data = await response.json();
      this.setState({
        newBoard: data.board,
        boardState: this.state.emptyBoard,
        correct_words: data.correct_words,
        words: [],
        disabled: true,
        minutes: '00',
        seconds: '00'
      });

    }
    else if (buttonValue === "Start Game") {
      this.intervalHandle = setInterval(this.tick, 1000);
      this.state.minutes = '01';
      let time = this.state.minutes;
      this.secondsRemaining = time * 60;
      buttonValue = "Stop Game";
      this.setState({ boardState: this.state.newBoard, disabled: false });
    }
    else if (buttonValue === "Stop Game") {
      clearInterval(this.intervalHandle);
      buttonValue = "New Game";
      this.setState({ disabled: true });
    }

    this.setState({ buttonText: buttonValue });
  };

  render() {
    return (
      <div className="App">
        <div className="title">Boogle</div>
        <div className="left">
          <div>
            <Board boardState={this.state.boardState} />
          </div>
          <div>
            <TextBox addWord={this.addWord} disabled={this.state.disabled} />
          </div>
        </div>
        <div className="right">
          <div>
            <StartButton handleClick={this.handleClick} buttonText={this.state.buttonText} />
          </div>
          <Timer minutes={this.state.minutes} seconds={this.state.seconds} />
          <div>Score : {this.state.words.reduce((total, word) => total + word.length, 0)}</div>
          <div>
            Correct words:
            <WordList words={this.state.words} />
          </div>
        </div>
      </div >
    );
  }
}

export default App;
