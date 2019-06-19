import React, { Component } from "react";
import { Loader, Card, Dimmer } from "semantic-ui-react";
import axios from 'axios';
import { Link } from 'react-router-dom';

class ModelDetail extends Component {
  api_server = 'https://indrasnet.pythonanywhere.com/';

  state = {
    msg: '',
    model_detail: {},
    loadingData: false,
  }

  async componentDidMount() {
    this.setState({ loadingData: true });
    document.title = "Title";
    const res = await axios.get(this.api_server + 'models/props/' + this.props.id)
    console.log("Getting from models/props/id -PROPS: ")
    this.setState({ model_detail: res.data });
    console.log(this.state.model_detail)
    this.setState({ loadingData: false });
  }

  renderModelDetail= () => {
      console.log("DEBUGGING in renderModelDetail")
      return (
        <div>
          <Card key={this.props.id}>
            <Link to={{
              pathname: `/models/props/` + this.props.id,
              state: {
                msg: 'Linking the ModelDetail',
                model_detail: this.state.model_detail
              }
            }}>
            </Link>
          </Card>
        </div>
      );
    return <Card.Content>{this.state.model_detail}</Card.Content>;
  }

  render() {
    if (this.state.loadingData) {
      return (
        <Dimmer active inverted>
          <Loader size='massive'>Loading...</Loader>
        </Dimmer>
      );
    }

    console.log("This is in ModelDetail: ")
    console.log(this.props.id)

    return (
      <div>
        <br />
        <br /><br />
        <p> List of properties </p>
        {this.state.model_detail && this.renderModelDetail()}
        <br /><br />
      </div>
    );
  }
}

export default ModelDetail;