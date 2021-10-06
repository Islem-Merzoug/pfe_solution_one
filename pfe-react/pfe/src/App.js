import React from 'react';
import './App.css';
import jwt from 'jsonwebtoken';
import Navbar from './components/Navbar';
import Header from './components/Header';
import Footer from './components/Footer';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages';
import ModelDetails from './pages/modelDetails';
import About from './pages/about';
import Services from './pages/services';
import Contact from './pages/contact';
import SignUp from './pages/signup';
import StepOne from './components/StepOne';
import Dashboard from './pages/dashboard';
import SignIn from './pages/signin';

const App = () => {
  console.log("is_authenticated: ",localStorage.getItem("is_authenticated"));
  console.log("token_expired: ",localStorage.getItem('token_expired'));
  console.log("email: ",localStorage.getItem('email'));

  var isExpired = false;
  const token = localStorage.getItem('access_token');
  var decodedToken=jwt.decode(token, {complete: true});
  var dateNow = new Date();

  if (token){
    if(decodedToken.expires < dateNow.getTime()) {
      isExpired = true;
      localStorage.setItem("token_expired", true);

    }else {
      localStorage.setItem("token_expired", false);
    }
  }
  else {
    console.log('please sign in');

  }
  


  return (

    <Router>
        <Navbar />
        {/* <Header /> */}
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/modelDetails' component={ModelDetails} />
          <Route path='/stepOne' component={StepOne} />
          <Route path='/about' component={About} />
          <Route path='/services' component={Services} />
          <Route path='/contact-us' component={Contact} />
          <Route path='/dashboard' component={Dashboard} />
          <Route path='/sign-in' component={SignIn} />
          <Route path='/sign-up' component={SignUp} />
        </Switch>
        <Footer />

    </Router>
  );
}

export default App;

