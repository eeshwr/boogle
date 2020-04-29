import React from "react";
import "./layouts/wordlist.css";

class WordList extends React.Component {

  getlist = () => {
    return this.props.words.map((word, index) => <li key={index}>{word}</li>);
  };

  render() {
    return <nav><ul>{this.getlist()}</ul></nav>;
  }
}

export default WordList;
