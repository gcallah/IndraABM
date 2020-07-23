import React, { Component } from 'react';
import { Loader, Dimmer } from 'semantic-ui-react';
import { ListGroup, Button } from 'react-bootstrap';
import Col from 'react-bootstrap/Col';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';
import axios from 'axios';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import Carousel from './Carousel';
import sandpileImg from './images/Sandpile.jpg';
import sandpile1Img from './images/sandpile_2.png';
import mandelobrotImg from './images/mendelobrot_sq.jpg';
import './styles.css';
import config from '../config';

const CLEAR_REGISTRY_API = `${config.API_URL}registry/clear/`;

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      allItems: [],
      loadingData: false,
      apiFailed: false,
      loadingList: false,
      dataForCarousel: [
        { image: sandpileImg, title: 'by Seth Terashima' },
        { image: sandpile1Img, title: 'by Colt Browninga' },
        { image: mandelobrotImg, title: 'by Adam Majewski' },
      ],
    };
    this.api_server = config.API_URL;
  }

  async componentDidMount() {
    const { history } = this.props;
    try {
      this.setState({ loadingData: true });
      document.title = 'Home';
      const res = await axios.get(`${this.api_server}models`);
      this.setState({ allItems: res.data, loadingData: false });

      // clear any previous envFile stored in localstorage
      // also clear the registry in the backend.
      const envFileString = localStorage.getItem('envFile');
      if (envFileString !== null && envFileString !== undefined) {
        const envFile = JSON.parse(envFileString);
        /* eslint-disable */
        const { execution_key } = envFile;
        const clearExecutionRegistryResponse = await axios.get(
          `${CLEAR_REGISTRY_API}${execution_key}`,
        );
        // not doing anything with the response.
        // allow the frontend to continue functioning.
        // there should be a error reporting mechanism here to notify
        // admins that a particular key was not cleared.
      }
    } catch (e) {
      history.push('/errorCatching');
    }
  }

  handleClick = (id, name, source, graph) => {
    localStorage.setItem('menu_id', id);
    localStorage.setItem('name', name);
    localStorage.setItem('source', source);
    localStorage.setItem('graph', graph);
  };

  renderChooseModelProp = () => (
    <h1 className="small-header">Please choose a model: </h1>
  );

  render() {
    const {
      loadingData,
      dataForCarousel,
      allItems,
      apiFailed,
      loadingList,
    } = this.state;
    if (apiFailed) {
      return <h1>404 Error</h1>;
    }
    if (loadingData) {
      return (
        <Dimmer active inverted>
          <Loader size="massive">Loading...</Loader>
        </Dimmer>
      );
    }
    return (
      <div className="container">
        <div className="margin-bottom-80">
          <h1 className="text-left">Indra Agent-Based Modeling System</h1>
        </div>
        <div className="row">
          <Col sm={12} lg={4} className="mb-5">
            {this.renderChooseModelProp()}
            <Button
              variant="outline-primary"
              onClick={() => this.setState({ loadingList: true })}
            >
              Choose...
            </Button>
            {loadingList ? (
              <ListGroup>
                {/* Show the models if "active" is missing or is set to true */}
                {Object.keys(allItems).map((item) => (!('active' in allItems[item])
                  || allItems[item].active === true ? (
                    <OverlayTrigger
                      key={`${allItems[item].name}-tooltip`}
                      placement="right"
                      overlay={<Tooltip>{allItems[item].doc}</Tooltip>}
                    >
                      <Link
                        to={{
                          pathname: `/models/props/${allItems[item]['model ID']}`,
                        }}
                        className="text-primary p-3 list-group-item list-group-item-action link"
                        key={allItems[item].name}
                        onClick={() => this.handleClick(
                          allItems[item]['model ID'],
                          allItems[item].name,
                          allItems[item].source,
                          allItems[item].graph,
                        )}
                      >
                        {allItems[item].name}
                      </Link>
                    </OverlayTrigger>
                  ) : null))}
              </ListGroup>
            ) : null}
          </Col>
          <Col sm={12} lg={{ cols: 6, span: 6, offset: 2 }}>
            <Carousel
              speed={5000}
              autoplay
              className="col"
              data={dataForCarousel}
            />
          </Col>
        </div>
      </div>
    );
  }
}

Home.propTypes = {
  history: PropTypes.shape(),
};

Home.defaultProps = {
  history: {},
};

export default Home;
