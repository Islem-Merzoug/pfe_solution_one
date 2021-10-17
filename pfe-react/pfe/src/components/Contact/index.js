import React, { useState } from "react";
import './Contact.css'


const Contact = () => {
    const [status, setStatus] = useState("Submit");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus("Sending...");
        const { email, message, subject } = e.target.elements;
        let details = {
            "email": {
              "email": [
                email.value
              ]
            },
            "content": {
              "message": message.value,
              "subject": subject.value
            }
          }
        console.log(details);

        let response = await fetch("http://34.136.35.194:8000/email", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify(details),
        });
        setStatus("Submit");
        let result = await response.json();
        alert(result.message);
      };


      // return (
      //   <form onSubmit={handleSubmit}>
      //     <div>
      //       <label htmlFor="name">Name:</label>
      //       <input type="text" id="name" required />
      //     </div>
      //     <div>
      //       <label htmlFor="email">Email:</label>
      //       <input type="email" id="email" required />
      //     </div>
      //     <div>
      //       <label htmlFor="message">Message:</label>
      //       <textarea id="message" required />
      //     </div>
      //     <button type="submit">{status}</button>
      //   </form>
      // );


      // const onChangeContact = (event) => {
      //   console.log("Detect Type Value:",event.target.value);
      //   }

        
    return (
        <div>


            <div className="container">
            <h2>Contact Form</h2>
            <br/>

                <form onSubmit={handleSubmit} >
                    <label htmlFor="email">Email</label>
                    <input type="text" id="email" name="email" placeholder="Your email.."/>

                    <label htmlFor="subject">subject</label>
                    <input type="text" id="subject" name="subject" placeholder="Your subject.."/>

                    <label htmlFor="message">Message</label>
                    <textarea id="message" name="message" placeholder="Write something.." style={{height: "200px"}}></textarea>

                    <button type="submit">{status}</button>
                </form>

            </div>

        </div>
    )
}

export default Contact
