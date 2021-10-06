import React, { useState } from "react";
import { useHistory } from "react-router-dom";

import axios from "axios"
import './Signup.css'


const SignUpComponent = () => {
    let history = useHistory();

    const [status, setStatus] = useState("Submit");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus("Sending...");
        const { fullname, email, password } = e.target.elements;
        let details = {
          "fullname": fullname.value,
          "email": email.value,
          "password": password.value,
          "role": "user"
          }
        // console.log(details);

        axios({
          method  : 'post',
          url : "http://localhost:8000/user/signup",
          data : details
        })
        .then((res)=>{
          setStatus("Submit");
          console.log(res.data);
          if (res.data["code"] == 404){
            console.log(res.data['fullname']);
            alert(res.data['error'] + " " + res.data['message'])

          }
          else {
              setStatus("Submit");
              console.log(res);
              alert("Welcome " + res.data['fullname'])
            
            localStorage.setItem("userID", res.data['user_id']);
            localStorage.setItem("access_token", res.data['access_token']);
            localStorage.setItem("fullname", res.data['fullname']);
            localStorage.setItem("email", res.data['email']);
            localStorage.setItem("is_authenticated", true);
            localStorage.setItem("token_expired", false);
            window.location.reload();

            history.push("/dashboard");
          }

        })
        .catch((err) => {
          console.log("err");
          alert("Error:  " + err)
          throw err
        });
          

      };


    return (
        <div>


            <div className="container">
            <h2>Sign up Form</h2>
            <br/>

                <form onSubmit={handleSubmit} >
                    <label htmlFor="fullname">Fullname</label>
                    <input type="text" id="fullname" name="fullname" placeholder="Your fullname.."/>

                    <label htmlFor="email">Email</label>
                    <input type="text" id="email" name="email" placeholder="Your email.."/>

                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Your subject.."/>

                    <button type="submit">{status}</button>
                </form>

            </div>

        </div>
    )
}

export default SignUpComponent
