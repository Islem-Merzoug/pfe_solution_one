import React, {useState} from 'react';
import {
	BrowserRouter as Router,
	Switch,
	Route,
	useHistory,
	useParams
  } from "react-router-dom";

import {
	Btn, BtnInput, BtnDownload
} from './StepOneElements';
import { models } from "../../services/models";

function StepOne(){
	const history = useHistory();


	function BlogPost() {
		let { id } = useParams();
		let { fileName } = useParams();
		let { extentionName } = useParams();
		let finalExportLink = models[id].exportLink + "/" + fileName + "/" + extentionName
		return (

			<div style={{ margin : '3rem 3rem'}} >
					<div>
						<h1 style={{ display: 'flex', justifyContent: 'center' }} >{models[id].name}</h1>

						<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }} >
							{models[id].description}
						</div>
					</div>
					
					<br/>

					<div>

						{extentionName !== 'mp4' ? (
							<img 
								style={{    marginLeft: 'auto',
											marginRight: 'auto',
											display: 'block',
											borderStyle: 'solid', 
											borderColor: 'black',
											width: '50%'
										}}  
							src={finalExportLink} alt='Output' />

						) : (
							<video 
								style={{    marginLeft: 'auto',
											marginRight: 'auto',
											display: 'block',
											borderStyle: 'solid', 
											borderColor: 'black',
											width: '75%'
										}}  
											controls >
								<source src={finalExportLink} type="video/mp4"/>
							</video> 

						)}
						
						<div style={{ textAlign : 'center', padding : '20px'  }} >
							<a style={{ borderStyle: 'solid', borderColor: 'black', padding : '10px' }} href={finalExportLink} download>Download</a>
							<br/>
							<br/>
							<Btn onClick={() => { history.push('/modelDetails/' + id) }}>Retry again</Btn>
						</div>
					
					</div>
			</div>
		);
	  }



	return(

		<Router>
			<Switch>
				<Route path="/stepOne/:id/:fileName/:extentionName">
					<BlogPost />
				</Route>
			</Switch>
		</Router>


	)
}

export default StepOne;