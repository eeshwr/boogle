import React from "react";
import "./layouts/TextBox.css";

class TextBox extends React.Component {
  onEnterKey = e => {
    if (e.key === "Enter") {
      this.props.addWord(e.target.value);
      e.target.value = " ";
    }
  };

  render() {
    return (
      <div>
        <input
          type="text"
          name="word"
          className="input-res"
          placeholder="type here"
          disabled={this.props.disabled}
          onKeyDown={this.onEnterKey}
        />
      </div>
    );
  }
}

export default TextBox;
