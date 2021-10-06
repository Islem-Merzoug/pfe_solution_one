// import React, {useEffect, useState} from 'react';
// import { useHistory } from "react-router-dom";

// import {
//   Nav,
//   NavLink,
//   Bars,
//   NavMenu,
//   NavBtn,
//   NavBtnLink
// } from './NavbarElements';

// const Navbar = () => {
//   const [open, setOpen] = useState(false);

//   let history = useHistory();

//   useEffect(() => {
//     console.log('is_authenticated:', localStorage.getItem("is_authenticated"))
//   }, [])

//   return (
//     <>
//       <Nav>
//         <NavLink to='/'>
//           {/* <img src={'/images/logo.svg'} alt='IMEDscripts' /> 
//               <h1> IMEDscripts </h1> */}
         
//           <img src={'/images/unknown.png'} style={{height: "3rem"}} alt='IMEDscripts' />

//         </NavLink>



//         <Bars open={open} setOpen={setOpen}  />


//         <NavMenu>
//           <NavLink to='/' activeStyle>
//            Products
//           </NavLink>
//           <NavLink to='/about' activeStyle>
//             About
//           </NavLink>
//           {/* <NavLink to='/services' activeStyle>
//             Services
//           </NavLink> */}
//           <NavLink to='/contact-us' activeStyle>
//             Contact Us
//           </NavLink>

          

//           { localStorage.getItem("is_authenticated") ? (

//             <NavLink to='/dashboard' activeStyle>
//             Profil
//             </NavLink>

//             ) : (
//             <p> </p>
//           )}


//         </NavMenu>

//         { !localStorage.getItem("is_authenticated") ? (

//             <NavBtn>
//               <NavBtnLink to='/sign-in'>Sign In</NavBtnLink>
//               <NavBtnLink to='/sign-up'>Sign Up</NavBtnLink>
//             </NavBtn>
//             ) : (
//             <NavBtn>

//               <button onClick={() => { 

//                 localStorage.clear();
//                 console.log("Signed Out");
//                 window.location.reload();

//                 history.push("/sign-in");

//               }}>Sign Out</button>

//             </NavBtn>
//         )}


//       </Nav>

      
//     </>
//   );
// };

// export default Navbar;






import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";
import { useHistory } from "react-router-dom";

import {
  Nav,
  Bars,
  NavMenu,
  NavBtn,
  NavBtnLink
} from './NavbarElements';

function NavBar() {
  const [click, setClick] = useState(false);
  let history = useHistory();
  let is_authenticated = true
  let token_expired = true

  is_authenticated = (localStorage.getItem("is_authenticated") == "true") ? (is_authenticated = true) : (is_authenticated = false)
  token_expired = (localStorage.getItem("token_expired") == "false") ? (token_expired = false) : (token_expired = true)


  // if (localStorage.getItem("is_authenticated") == "true") {
  //   is_authenticated = true
  // } else {
  //   is_authenticated = false
  // }

  // if (localStorage.getItem("token_expired") == "false") {
  //   token_expired = false
  // } else {
  //   token_expired = true
  // }

  console.log("______________________________");
  console.log("is_authenticated: ", is_authenticated);
  console.log("token_expired: ", token_expired);

  const handleClick = () => setClick(!click);
  return (
    <>
      <nav className="navbar">
        <div className="nav-container">
          <NavLink exact to="/" className="nav-logo">
            <img src={'/images/unknown.png'} style={{height: "3rem"}} alt='IMEDscripts' />

          </NavLink>

          <ul className={click ? "nav-menu active" : "nav-menu"}>
            <li className="nav-item">
              <NavLink
                exact
                to="/"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Products
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/about"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                About
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/contact-us"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Contact Us
              </NavLink>

            </li>

            <li className="nav-item">
            { is_authenticated && !token_expired  ? (
                  <NavLink
                  exact
                  to="/dashboard"
                  activeClassName="active"
                  className="nav-links"
                  onClick={handleClick}
                  >
                  Profil
                  </NavLink>

                  ) : (
                  <p> haha </p>
                )}
            </li>

            <li className="nav-item">
            { !is_authenticated || token_expired ? (
                  // <NavLink
                  // exact
                  // to="/sign-in"
                  // activeClassName="active"
                  // className="nav-links"
                  // onClick={handleClick}
                  // >
                  // Sign Un
                  // </NavLink>
                  <button onClick={() => { 
                    history.push("/sign-in");
                  }}>Sign In</button>

                  ) : (
                  <p> </p>
                )}
            </li>

            <li className="nav-item">
            { !is_authenticated || token_expired ? (

                  // <NavLink
                  //   exact
                  //   to="/sign-up"
                  //   activeClassName="active"
                  //   className="nav-links"
                  //   onClick={handleClick}
                  //   >
                  //   Sign Up
                  // </NavLink>

                  <button onClick={() => { 
                    history.push("/sign-up");
                  }}>Sign Up</button>

                  ) : (
                  
                  <button onClick={() => { 
                    localStorage.clear();
                    // localStorage.setItem("is_authenticated", false);
                    // localStorage.setItem("token_expired", true);
                    console.log("Signed Out");
                    window.location.reload();
                    history.push("/sign-in");
                  }}>Sign Out</button>
                )}

            </li>





          </ul>
          <div className="nav-icon" onClick={handleClick}>
            <i className={click ? "fas fa-times" : "fas fa-bars"}></i>
          </div>
        </div>
      </nav>
    </>
  );
}

export default NavBar;