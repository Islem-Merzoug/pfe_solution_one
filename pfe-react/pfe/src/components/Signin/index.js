import React, { useState } from "react";
import axios from 'axios'
import './Signin.css'
import { useHistory } from "react-router-dom";


const SignInComponent = () => {
    let history = useHistory();


    const [status, setStatus] = useState("Submit");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus("Sending...");
        const { email, password } = e.target.elements;
        let details = {
            "email": email.value,
            "password": password.value
          }
        // console.log(details);

        axios({
          method  : 'post',
          url : "http://34.136.35.194:8000/user/signin",
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

            history.push("/dashboard");
            window.location.reload();

          }


          

        })
        .catch((err) => {
          console.log("err");
          alert("Error:  " + err)
          throw err
        });

        // let response = await fetch("http://localhost:8000/user/signin", {
        //   method: "POST",
        //   headers: {
        //     "Content-Type": "application/json;charset=utf-8",
        //   },
        //   body: JSON.stringify(details),
        // });
        // setStatus("Submit");
        // let result = await response.json();
        // console.log(result);
        // localStorage.setItem("userID", result.user_id);
        // localStorage.setItem("access_token", result.access_token);
        // localStorage.setItem("is_authenticated", true);
        // localStorage.setItem("session_expired", false);
        // console.log(localStorage.getItem("userID"))

      };
        
    return (
        <div>


            <div className="container">
            <h2>Sign in Form</h2>
            <br/>

                <form onSubmit={handleSubmit} >
                    <label htmlFor="email">Email</label>
                    <input type="text" id="email" name="email" placeholder="Your email.."/>

                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Your password.."/>

                    <button type="submit">{status}</button>
                </form>

            </div>

        </div>
    )
}

export default SignInComponent
