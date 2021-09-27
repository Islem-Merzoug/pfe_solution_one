import React from "react";
import { useHistory } from "react-router-dom";
import './Card.css'


import {
  CardWrapper,
  CardHeader,
  CardHeading,
  CardBody,
  CardFieldset,
  CardButton,
  CardImage,
  CardDescription
} from "./CardElements";

function Card(props) {
  const history = useHistory();

  return (
    <div className="App">
          <CardWrapper>
            <CardImage src={props.image} />

            <CardHeader>
              <CardHeading>{props.name}</CardHeading>
            </CardHeader>

            <CardBody>
              
              <CardDescription>{props.description.substring(0, 100)} ...</CardDescription>

              <CardFieldset>
                <CardButton type="button" onClick={ () => { history.push(props.detailLink) }}>Try it now</CardButton>
              </CardFieldset>
              
            </CardBody>
          </CardWrapper>
    </div>
  );
}

export default Card;