import styled from "styled-components";


export const CardWrapper = styled.div`
  overflow: hidden;
  padding: 0 0 2rem;
  margin: 1rem auto 0;
  width: 15rem;
  box-shadow: 0 0 1.2rem rgba(0, 0, 0, 0.05), 0 0rem 2.5rem rgba(0, 0, 0, 0.08);
  border-radius: 2em;
  border: 0.4rem solid red;
  border-color: #000;
`;

export const CardImage = styled.img`
  width: 100%;
  // hight: 5rem;
`;

export const CardHeader = styled.header`
  padding-top: 0.8rem;
  padding-bottom: 0.8rem;
`;

export const CardHeading = styled.h1`
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
`;

export const CardBody = styled.div`
  padding-right: 1rem;
  padding-left: 1rem;
`;

export const CardDescription = styled.div`
  padding-bottom: 0.7rem;

  font-size: 1rem;
  color: gray;
  text-align: left;
`;




export const CardFieldset = styled.fieldset`
  position: relative;
  padding: 0;
  margin: 0;
  border: 0;

  & + & {
    margin-top: 24px;
  }

  &:nth-last-of-type(2) {
    margin-top: 32px;
  }

  &:last-of-type {
    text-align: center;
  }
`;




export const CardButton = styled.button`
  display: block;
  width: 100%;
  padding: 12px 0;
  font-family: inherit;
  font-size: 0.9rem;
  font-weight: 700;
  color: #fff;
  background-color: #256ce1;
  border: 0;
  border-radius: 2rem;
  box-shadow: 0 0.9rem 0.9rem rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.02, 0.01, 0.47, 1);

  &:hover {
    box-shadow: 0 1rem 1rem rgba(0, 0, 0, 0.16);
    transform: translate(0, -5px);
  }
`;
