
import React from "react";
import {
  Box,
  Container,
  Row,
  Column,
  FooterLink,
  Heading,
} from "./FooterElements";
  
const Footer = () => {
  return (
    <Box>
      <div style={{ color: "#256ce1", 
                    textAlign: "center", 
                    margin: "1.5rem"
              }}> 
        <img style={{ width: '80px' }} src={'/images/unknown.png'} alt='IMEDscripts' />         
      </div>
      <Container>
        <Row>
          <Column>
            <Heading>About Us</Heading>
            <FooterLink href="#">Aim</FooterLink>
            <FooterLink href="#">Vision</FooterLink>
            <FooterLink href="#">Testimonials</FooterLink>
          </Column>
          <Column>
            <Heading>Services</Heading>
            <FooterLink href="#">Writing</FooterLink>
            <FooterLink href="#">Internships</FooterLink>
            <FooterLink href="#">Coding</FooterLink>
            <FooterLink href="#">Teaching</FooterLink>
          </Column>
          <Column>
            <Heading>Contact Us</Heading>
            <FooterLink href="#">Uttar Pradesh</FooterLink>
            <FooterLink href="#">Ahemdabad</FooterLink>
            <FooterLink href="#">Indore</FooterLink>
            <FooterLink href="#">Mumbai</FooterLink>
          </Column>
          <Column>
            <Heading>Social Media</Heading>
            <FooterLink href="#">
              <i className="fab fa-facebook-f">
                <span style={{ marginLeft: "10px" }}>
                  Facebook
                </span>
              </i>
            </FooterLink>
            <FooterLink href="#">
              <i className="fab fa-instagram">
                <span style={{ marginLeft: "10px" }}>
                  Instagram
                </span>
              </i>
            </FooterLink>
            <FooterLink href="#">
              <i className="fab fa-twitter">
                <span style={{ marginLeft: "10px" }}>
                  Twitter
                </span>
              </i>
            </FooterLink>
            <FooterLink href="#">
              <i className="fab fa-youtube">
                <span style={{ marginLeft: "10px" }}>
                  Youtube
                </span>
              </i>
            </FooterLink>
          </Column>
        </Row>
      </Container>

      <h2 style={{ color: "#fff", textAlign: "center", margin: "0 1.5rem" }} >Nos Partenaires</h2>

      <div style={{ color: "#256ce1", 
                    textAlign: "center", 
                    margin: "1.5rem"
              }}> 
        <img style={{ maxHeight: '80px', margin: "0 1.5rem" }} src={'/images/LogoUnivBejaia.png'} alt='IMEDscripts' />         
        <img style={{ maxHeight: '80px', margin: "0 1.5rem" }} src={'/images/limed.png'} alt='IMEDscripts' />  
        <img style={{ maxHeight: '80px', margin: "0 1.5rem" }} src={'/images/cerist.png'} alt='IMEDscripts' />
        <img style={{ maxHeight: '80px', margin: "0 1.5rem" }} src={'/images/cropped-icon-epb.png'} alt='IMEDscripts' />         
        <img style={{ maxHeight: '80px', margin: "0 1.5rem" }} src={'/images/LOGOGlob.png'} alt='IMEDscripts' />         

       
      </div>


    </Box>
  );
};
export default Footer;