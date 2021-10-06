import React, { useState, useEffect } from 'react'
import './DashboardTable.css'
import axios from "axios";

function DashboardTable() {
    const [files, setfiles] = useState([])
    
	const getAllFiles = () => {
        axios({
            method: 'get',
            url: 'http://localhost:8000/get_files/' + localStorage.getItem("userID")
        })
        .then((res)=>{
			// console.log(res['data']['data'][0]);
            setfiles(res['data']['data'][0])
		})
		.catch((err) => {
			console.log("err");
			throw err
		});
    }

    useEffect(() => {
            getAllFiles();
    }, [])
            // console.log(files);

    return (
        <div>

            <div className="container">

                <h2>User Information</h2>
                <h4>Fullname</h4>
                { localStorage.getItem("fullname") }  
                <br/>

                <h4>Email</h4>
                { localStorage.getItem("email") }
                <br/>
                <br/>

            <table>

                <tr>

                    <th> File Name </th>
                    <th> Prediction Date </th>
                    <th> File Type </th>
                    <th> Prediction Service </th>
                    <th> Download Link </th>
                    
                </tr>
                {
                files.map((model, i) =>
                    <tr key={i} >
                        <td> { model.name } </td>
                        <td> { model.date.substring(0, 10) } at { model.date.substring(11, 19) }  </td>
                        <td> { model.type } </td>
                        <td> { model.service } </td>
                        <td>
                            <a href={ model.outputLink }> Download</a>
                        </td>
                    </tr>
                    )
                }
            </table>

            </div>
            
        </div>
    )
}

export default DashboardTable
