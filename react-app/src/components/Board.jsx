import React from "react";
import "./layouts/Board.css";
import "./layouts/grid.css";

/* class Board extends React.Component {
  createBoard = () => {
    const table = this.props.boardState.map((row, indx) => (
      <tr key={indx}>
        {row.map((column, index) => (
          <th key={index}>
            <h1>{column}</h1>
          </th>
        ))}
      </tr>
    ));
    return <tbody>{table}</tbody>;
  };

  render() {
    return <table>{this.createBoard()}</table>;
  }
} */


/* <button className="button roundButton" id="myBtn"
              onClick={async () => {
                var x = document.getElementById("myBtn");
                if (x.innerHTML === "New Game") {
                  const url = "http://localhost:5000/load_boogle";
                  const response = await fetch(url, { mode: "cors" });
                  const data = await response.json();
                  this.setState({ newBoard: data.board, boardState: this.state.emptyBoard, correct_words: data.correct_words, words: [] });
                  x.innerHTML = "Start Game";
                }
                else if (x.innerHTML === "Start Game") {
                  this.setState({ boardState: this.state.newBoard });
                  x.innerHTML = "Stop Game";

                }
                else if (x.innerHTML === "Stop Game") {
                  x.innerHTML = "New Game";
                }
              }}
            ></button> */





class Board extends React.Component {
  createBoard = () => {
    const table = this.props.boardState.map((row, index) => (
      <div className="row" key={index}>
        {row.map((column, index) => (
          <div className="box">
            <div className="inner" key={index}>
              <h1>{column}</h1>
            </div>
          </div>
        ))}
      </div>
    ));
    return table;
  };

  render() {
    return <div className="grid">{this.createBoard()}</div>;
  }
}

export default Board;
